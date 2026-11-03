/**
 * JD CÂMARAS FRIAS — LP A (Versão Direta)
 * lp.js: Lógica de negócio, formulário em etapa única, Consent Mode v2, Atribuição jd_attrib,
 * lead_id único, envio seguro ao Webhook n8n (HTTP 2xx) e WhatsApp com código de referência (ref).
 * Zero dependências externas.
 */

// Política de privacidade própria da JD
const PRIVACY_URL = 'https://www.facebook.com/privacy/policy/?locale=pt_BR';

// Endpoint de envio do webhook
const LEAD_ENDPOINT = 'https://n8n-n8n.6djmf0.easypanel.host/webhook-test/2d504637-993c-408d-8679-9741149bb883';

// Número de WhatsApp oficial da JD
const WHATSAPP_NUMBER = '5562999940769';

(function () {
  'use strict';

  // 1. TÍTULO DINÂMICO POR PARÂMETRO ?h=
  const VARIANTS = {
    preco: {
      h1: 'Receba o preço da sua câmara fria sob medida',
      sub: 'A JD calcula pelo tamanho, pela temperatura e pelo uso e envia o orçamento pelo WhatsApp.'
    },
    mini: {
      h1: 'Mini câmara fria sob medida para o seu espaço',
      sub: 'Para quem tem pouco espaço e precisa de frio. Informe o que vai armazenar e as medidas e receba o orçamento da JD.'
    },
    walkin: {
      h1: 'Câmara fria para bebidas: walk-in cooler sob medida, entregue e instalada',
      sub: 'Informe o que vai armazenar e as medidas do espaço e receba o orçamento da JD.'
    },
    congelados: {
      h1: 'Câmara de congelados (-18 °C) sob medida, com instalação pela JD',
      sub: 'Informe o que vai armazenar e as medidas do espaço e receba o orçamento da JD.'
    },
    resfriados: {
      h1: 'Câmara de resfriados (0 a +15 °C) sob medida, com instalação pela JD',
      sub: 'Informe o que vai armazenar e as medidas do espaço e receba o orçamento da JD.'
    }
  };

  const DEFAULT_HEADLINE = {
    h1: 'Câmara fria sob medida, projetada e instalada para o seu negócio',
    sub: 'Mini câmaras, câmaras expositoras, resfriados e congelados. Informe o que você vai armazenar e as medidas do espaço e receba o orçamento da JD.'
  };

  let activeVariantKey = 'padrao';

  function applyDynamicHeadline() {
    const params = new URLSearchParams(window.location.search);
    const hParam = (params.get('h') || '').toLowerCase().trim();

    const h1El = document.getElementById('hero-title');
    const subEl = document.getElementById('hero-subtitle');
    const variantInput = document.getElementById('lp-field-titulo_variante') || document.getElementById('lp-field-titulo-variante');

    if (hParam && VARIANTS[hParam]) {
      activeVariantKey = hParam;
      if (h1El) h1El.textContent = VARIANTS[hParam].h1;
      if (subEl) subEl.textContent = VARIANTS[hParam].sub;
    } else {
      activeVariantKey = 'padrao';
      if (h1El) h1El.textContent = DEFAULT_HEADLINE.h1;
      if (subEl) subEl.textContent = DEFAULT_HEADLINE.sub;
    }

    if (variantInput) {
      variantInput.value = activeVariantKey;
    }
  }

  // 2. DATA LAYER HELPER
  window.dataLayer = window.dataLayer || [];

  function pushTrackingEvent(eventName, extraData) {
    const payload = Object.assign({
      event: eventName,
      lp_version: 'A',
      titulo_variante: activeVariantKey
    }, extraData || {});
    window.dataLayer.push(payload);
  }

  // 3. ESTADO DE CONSENTIMENTO (Consent Mode v2)
  const CONSENT_STORAGE_KEY = 'jd_consent_v1';
  const CONSENT_EXPIRATION_MS = 365 * 24 * 60 * 60 * 1000; // 12 meses

  function getConsentStatus() {
    try {
      const raw = localStorage.getItem(CONSENT_STORAGE_KEY);
      if (!raw) return { ads: 'pending', analytics: 'pending' };
      const data = JSON.parse(raw);
      if (!data || typeof data.ts !== 'number' || (Date.now() - data.ts > CONSENT_EXPIRATION_MS)) {
        return { ads: 'pending', analytics: 'pending' };
      }
      return {
        ads: data.ads === true ? 'granted' : (data.ads === false ? 'denied' : 'pending'),
        analytics: data.analytics === true ? 'granted' : (data.analytics === false ? 'denied' : 'pending')
      };
    } catch (e) {
      return { ads: 'pending', analytics: 'pending' };
    }
  }

  // 4. ATRIBUIÇÃO (jd_attrib) COM REGRAS DE CONSENTIMENTO E ÚLTIMO CLIQUE
  const ATTRIB_STORAGE_KEY = 'jd_attrib';
  const ATTRIB_EXPIRATION_MS = 90 * 24 * 60 * 60 * 1000; // 90 dias

  const ATTRIB_PARAMS = [
    'utm_source',
    'utm_medium',
    'utm_campaign',
    'utm_term',
    'utm_content',
    'matchtype',
    'device',
    'network',
    'gclid',
    'gbraid',
    'wbraid'
  ];

  let currentAttrib = {};

  function loadStoredAttrib() {
    let stored = null;
    const consent = getConsentStatus();

    // Se publicidade estiver CONCEDIDA, lê de localStorage com validade de 90 dias
    if (consent.ads === 'granted') {
      try {
        const raw = localStorage.getItem(ATTRIB_STORAGE_KEY);
        if (raw) {
          const parsed = JSON.parse(raw);
          if (parsed && typeof parsed.ts === 'number') {
            if (Date.now() - parsed.ts < ATTRIB_EXPIRATION_MS) {
              stored = parsed;
            } else {
              localStorage.removeItem(ATTRIB_STORAGE_KEY);
            }
          }
        }
      } catch (e) { /* noop */ }
    }

    // Se não encontrou no localStorage, tenta no sessionStorage
    if (!stored) {
      try {
        const rawSession = sessionStorage.getItem(ATTRIB_STORAGE_KEY);
        if (rawSession) {
          stored = JSON.parse(rawSession);
        }
      } catch (e) { /* noop */ }
    }

    return stored || {};
  }

  function saveAttrib(attribObj) {
    const consent = getConsentStatus();
    attribObj.ts = Date.now();

    if (consent.ads === 'granted') {
      try {
        localStorage.setItem(ATTRIB_STORAGE_KEY, JSON.stringify(attribObj));
      } catch (e) { /* noop */ }
    } else {
      try {
        sessionStorage.setItem(ATTRIB_STORAGE_KEY, JSON.stringify(attribObj));
      } catch (e) { /* noop */ }
    }
  }

  function initAttribution() {
    const params = new URLSearchParams(window.location.search);
    const stored = loadStoredAttrib();
    const merged = {};

    ATTRIB_PARAMS.forEach(function (param) {
      const urlVal = params.get(param);
      if (urlVal !== null && urlVal !== '') {
        merged[param] = urlVal;
      } else if (stored[param]) {
        merged[param] = stored[param];
      } else {
        merged[param] = '';
      }

      // Preenche os campos ocultos do formulário
      const input = document.getElementById('lp-field-' + param);
      if (input) {
        input.value = merged[param];
      }
    });

    currentAttrib = merged;
    saveAttrib(merged);

    // Landing Page completa (com query params e hash)
    const lpUrlInput = document.getElementById('lp-field-landing_page') || document.getElementById('lp-field-landing-page');
    if (lpUrlInput) {
      lpUrlInput.value = window.location.href;
    }

    updateHiddenConsentFields();
  }

  function updateHiddenConsentFields() {
    const consent = getConsentStatus();
    const inputAds = document.getElementById('lp-field-consent_ads');
    const inputAnalytics = document.getElementById('lp-field-consent_analytics');
    if (inputAds) inputAds.value = consent.ads;
    if (inputAnalytics) inputAnalytics.value = consent.analytics;
  }

  // 5. GERAÇÃO E PERSISTÊNCIA DO LEAD_ID
  let currentLeadId = null;
  let formStartedTracked = false;
  let step1CompletedTracked = false;
  let leadSubmittedSuccessfully = false;

  function generateUUID() {
    if (typeof crypto !== 'undefined' && typeof crypto.randomUUID === 'function') {
      try {
        return crypto.randomUUID();
      } catch (e) { /* fallback */ }
    }
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
      const r = Math.random() * 16 | 0;
      const v = c === 'x' ? r : (r & 0x3 | 0x8);
      return v.toString(16);
    });
  }

  function getOrCreateLeadId() {
    if (!currentLeadId) {
      currentLeadId = generateUUID();
      const input = document.getElementById('lp-field-lead_id');
      if (input) input.value = currentLeadId;
    }
    return currentLeadId;
  }

  // 6. NORMALIZAÇÃO DO TELEFONE (E.164 SEM PII EXTRA)
  function normalizePhoneE164(rawPhone) {
    if (!rawPhone) return '';
    let digits = String(rawPhone).replace(/\D/g, '');
    digits = digits.replace(/^0+/, '');
    if (!digits.startsWith('55')) {
      digits = '55' + digits;
    }
    if (digits.length === 12 || digits.length === 13) {
      return '+' + digits;
    }
    return '';
  }

  // 7. TIMEZONE COM FUSO HORÁRIO -03:00 (ISO 8601)
  function getIsoTimestampSaoPaulo() {
    const now = new Date();
    const utcMs = now.getTime() + (now.getTimezoneOffset() * 60000);
    const spMs = utcMs - (3 * 3600000); // UTC - 3 hours
    const spDate = new Date(spMs);

    const pad = function (n, z) { z = z || 2; return ('00' + n).slice(-z); };
    const yyyy = spDate.getFullYear();
    const MM = pad(spDate.getMonth() + 1);
    const dd = pad(spDate.getDate());
    const HH = pad(spDate.getHours());
    const mm = pad(spDate.getMinutes());
    const ss = pad(spDate.getSeconds());
    const ms = pad(spDate.getMilliseconds(), 3);

    return yyyy + '-' + MM + '-' + dd + 'T' + HH + ':' + mm + ':' + ss + '.' + ms + '-03:00';
  }

  // 8. CÓDIGO DE REFERÊNCIA WHATSAPP (ref)
  function generateWhatsAppRef() {
    if (leadSubmittedSuccessfully && currentLeadId) {
      // 6 primeiros caracteres em maiúsculas do lead_id
      const clean = currentLeadId.replace(/[^a-zA-Z0-9]/g, '').toUpperCase();
      return clean.slice(0, 6);
    }
    const chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'; // Sem 0, O, 1, I
    let ref = '';
    for (let i = 0; i < 6; i++) {
      ref += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return ref;
  }

  // 9. MÁSCARA DE TELEFONE (XX) XXXXX-XXXX
  function applyPhoneMask(input) {
    if (!input) return;
    input.addEventListener('input', function () {
      let v = this.value.replace(/\D/g, '');
      if (v.length > 11) v = v.slice(0, 11);

      if (v.length > 6) {
        this.value = '(' + v.slice(0, 2) + ') ' + v.slice(2, 7) + '-' + v.slice(7);
      } else if (v.length > 2) {
        this.value = '(' + v.slice(0, 2) + ') ' + v.slice(2);
      } else if (v.length > 0) {
        this.value = '(' + v;
      }
    });

    input.addEventListener('keypress', function (e) {
      if (!/\d/.test(e.key) && e.key !== 'Backspace' && e.key !== 'Delete' && e.key !== 'Tab') {
        e.preventDefault();
      }
    });
  }

  // 10. VALIDAÇÃO DE CAMPOS COM ÍCONE + TEXTO
  const ERROR_ICON_SVG = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex-shrink:0;margin-top:1px;"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>';

  function setFieldError(field, hasError, customMessage) {
    if (!field) return;
    const group = field.closest('.jd-form__group');
    if (!group) return;

    let errorEl = group.querySelector('.jd-form__error');
    if (!errorEl) {
      errorEl = document.createElement('div');
      errorEl.className = 'jd-form__error';
      errorEl.style.display = 'flex';
      errorEl.style.alignItems = 'center';
      errorEl.style.gap = '6px';
      group.appendChild(errorEl);
    }

    if (hasError) {
      group.classList.add('is-error');
      field.classList.add('is-error');
      field.setAttribute('aria-invalid', 'true');
      const msg = customMessage || 'Preencha este campo.';
      errorEl.innerHTML = ERROR_ICON_SVG + '<span>' + msg + '</span>';
      errorEl.style.display = 'flex';
    } else {
      group.classList.remove('is-error');
      field.classList.remove('is-error');
      field.removeAttribute('aria-invalid');
      errorEl.innerHTML = '';
      errorEl.style.display = 'none';
    }
  }

  function validateInput(field) {
    if (!field) return true;
    const val = (field.value || '').trim();
    const isRequired = field.hasAttribute('required');

    if (isRequired && !val) {
      setFieldError(field, true, 'Preencha este campo.');
      return false;
    }

    if (field.type === 'tel' || field.id === 'lp-field-whatsapp') {
      const digits = val.replace(/\D/g, '');
      if (digits.length < 10) {
        setFieldError(field, true, 'Confira o WhatsApp com DDD. Exemplo: (32) 99999-9999');
        return false;
      }
    }

    if (field.id === 'lp-field-nome' && val.length < 3) {
      setFieldError(field, true, 'Preencha este campo.');
      return false;
    }

    // Validação de medidas opcionais se preenchidas
    if (field.id === 'lp-field-comprimento' && val) {
      const c = parseFloat(val);
      if (isNaN(c) || c < 1.0 || c > 30.0) {
        setFieldError(field, true, 'Comprimento entre 1m e 30m.');
        return false;
      }
    }
    if (field.id === 'lp-field-largura' && val) {
      const l = parseFloat(val);
      if (isNaN(l) || l < 1.0 || l > 25.0) {
        setFieldError(field, true, 'Largura entre 1m e 25m.');
        return false;
      }
    }
    if (field.id === 'lp-field-altura' && val) {
      const a = parseFloat(val);
      if (isNaN(a) || a < 1.5 || a > 8.0) {
        setFieldError(field, true, 'Altura entre 1.5m e 8m.');
        return false;
      }
    }

    setFieldError(field, false);
    return true;
  }

  // 11. MOTOR DO FORMULÁRIO EM ETAPA ÚNICA (LP A)
  function initLeadForm() {
    const form = document.getElementById('lp-form-lead');
    if (!form) return;

    const formBody = document.getElementById('lp-form-body');
    const formHeader = document.getElementById('lp-form-header');
    const btnSubmit = document.getElementById('lp-btn-submit');
    const successBlock = document.getElementById('lp-form-sucesso');
    const honeypot = document.getElementById('lp-field-website');
    const submitErrorWrap = document.getElementById('lp-submit-error');
    const btnRetry = document.getElementById('lp-btn-retry');

    const nomeField = document.getElementById('lp-field-nome');
    const phoneField = document.getElementById('lp-field-whatsapp');
    const tipoCamaraField = document.getElementById('lp-field-tipo_camara');
    const armazenarField = document.getElementById('lp-field-armazenar');
    const larguraField = document.getElementById('lp-field-largura');
    const comprimentoField = document.getElementById('lp-field-comprimento');
    const alturaField = document.getElementById('lp-field-altura');
    const cidadeField = document.getElementById('lp-field-cidade');
    const ufField = document.getElementById('lp-field-uf');

    function checkStep1Completion() {
      if (step1CompletedTracked) return;
      if (!nomeField || !phoneField) return;
      const isNomeValid = (nomeField.value || '').trim().length >= 3;
      const isPhoneValid = (phoneField.value || '').replace(/\D/g, '').length >= 10;
      if (isNomeValid && isPhoneValid) {
        step1CompletedTracked = true;
        const id = getOrCreateLeadId();
        pushTrackingEvent('lead_form_step1_complete', { lead_id: id });
      }
    }

    function handleFirstInteraction() {
      if (!formStartedTracked) {
        formStartedTracked = true;
        const id = getOrCreateLeadId();
        pushTrackingEvent('lead_form_start', { lead_id: id });
      }
    }

    form.addEventListener('focusin', handleFirstInteraction);
    form.addEventListener('input', handleFirstInteraction);

    const allFormInputs = form.querySelectorAll('input, select, textarea');
    allFormInputs.forEach(function (input) {
      input.addEventListener('blur', function () {
        if (this.hasAttribute('required') || this.value.trim().length > 0) {
          validateInput(this);
        }
        if (this === phoneField || this === nomeField) {
          checkStep1Completion();
        }
      });
      input.addEventListener('input', function () {
        if (this.classList.contains('is-error')) {
          setFieldError(this, false);
        }
      });
    });

    applyPhoneMask(phoneField);

    // Tentar de novo após erro de envio: reenvia com o MESMO lead_id
    if (btnRetry) {
      btnRetry.addEventListener('click', function (e) {
        e.preventDefault();
        if (submitErrorWrap) submitErrorWrap.style.display = 'none';
        handleFormSubmit();
      });
    }

    // Submissão do Formulário
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      handleFormSubmit();
    });

    if (btnSubmit) {
      btnSubmit.addEventListener('click', function (e) {
        e.preventDefault();
        handleFormSubmit();
      });
    }

    function showSuccessUI() {
      if (formBody) formBody.style.display = 'none';
      if (formHeader) formHeader.style.display = 'none';
      if (submitErrorWrap) submitErrorWrap.style.display = 'none';
      if (successBlock) {
        successBlock.classList.add('is-visible');
        successBlock.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }

    function showSuccessView(tipoCamara, armazenar, uf, rawPhone) {
      showSuccessUI();

      // Dispara lead_form_submit SOMENTE após resposta 2xx confirmada
      const normalizedPhone = normalizePhoneE164(rawPhone);
      window.dataLayer.push({
        event: 'lead_form_submit',
        lead_id: currentLeadId,
        event_id: currentLeadId,
        tipo_camara: tipoCamara,
        armazenar: armazenar,
        uf: uf,
        lp_version: 'A',
        titulo_variante: activeVariantKey,
        user_data: {
          phone_number: normalizedPhone
        }
      });
    }

    function handleFormSubmit() {
      // Honeypot anti-spam (descarte silencioso: interface de sucesso, SEM post e SEM dataLayer)
      if (honeypot && honeypot.value.trim() !== '') {
        showSuccessUI();
        return;
      }

      // Validação em ordem visual
      const fieldsToValidate = [
        nomeField,
        phoneField,
        tipoCamaraField,
        armazenarField,
        larguraField,
        comprimentoField,
        alturaField,
        cidadeField,
        ufField
      ];

      let allValid = true;
      let firstInvalid = null;

      fieldsToValidate.forEach(function (inp) {
        if (inp && !validateInput(inp)) {
          allValid = false;
          if (!firstInvalid) firstInvalid = inp;
        }
      });

      if (!allValid) {
        if (firstInvalid) {
          firstInvalid.focus();
          firstInvalid.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
        return;
      }

      // Assegura que o lead_id existe e é preservado em retentativas
      const leadId = getOrCreateLeadId();

      // Atualiza consentimento no momento do envio
      const consentStatus = getConsentStatus();
      updateHiddenConsentFields();

      // Recupera dados preenchidos
      const nomeVal = (nomeField ? nomeField.value : '').trim();
      const whatsappVal = (phoneField ? phoneField.value : '').trim();
      const tipoCamaraVal = (tipoCamaraField ? tipoCamaraField.value : '').trim();
      const armazenarVal = (armazenarField ? armazenarField.value : '').trim();
      const largVal = (larguraField && larguraField.value.trim() !== '') ? larguraField.value.trim() : '';
      const compVal = (comprimentoField && comprimentoField.value.trim() !== '') ? comprimentoField.value.trim() : '';
      const altVal = (alturaField && alturaField.value.trim() !== '') ? alturaField.value.trim() : '';
      const cidadeVal = (cidadeField ? cidadeField.value : '').trim();
      const ufVal = (ufField ? ufField.value : '').trim();

      const timestampEnvio = getIsoTimestampSaoPaulo();
      const timestampInput = document.getElementById('lp-field-timestamp_envio');
      if (timestampInput) timestampInput.value = timestampEnvio;

      // Monta Payload final do webhook com 28 campos exatos na ordem solicitada
      const payload = {
        tipo_evento: 'lead_form',
        lead_id: leadId,
        timestamp_envio: timestampEnvio,
        nome: nomeVal,
        whatsapp: whatsappVal,
        tipo_camara: tipoCamaraVal,
        armazenar: armazenarVal,
        largura: largVal,
        comprimento: compVal,
        altura: altVal,
        cidade: cidadeVal,
        uf: ufVal,
        utm_source: currentAttrib.utm_source || '',
        utm_medium: currentAttrib.utm_medium || '',
        utm_campaign: currentAttrib.utm_campaign || '',
        utm_term: currentAttrib.utm_term || '',
        utm_content: currentAttrib.utm_content || '',
        matchtype: currentAttrib.matchtype || '',
        device: currentAttrib.device || '',
        network: currentAttrib.network || '',
        gclid: currentAttrib.gclid || '',
        gbraid: currentAttrib.gbraid || '',
        wbraid: currentAttrib.wbraid || '',
        landing_page: window.location.href,
        lp_version: 'A',
        titulo_variante: activeVariantKey,
        consent_ads: consentStatus.ads,
        consent_analytics: consentStatus.analytics
      };

      const isDebug = new URLSearchParams(window.location.search).get('debug') === '1';

      if (isDebug) {
        console.group('🔍 [LP Debug Mode] Webhook Payload & Attribution (lp_version: A)');
        console.log('Webhook Payload (28 campos):', payload);
        console.log('Objeto jd_attrib:', currentAttrib);
        console.groupEnd();
        // Em modo debug, não envia para o servidor real
        return;
      }

      // Bloqueio de duplo envio
      if (btnSubmit) {
        btnSubmit.disabled = true;
        btnSubmit.classList.add('is-loading');
      }
      if (submitErrorWrap) submitErrorWrap.style.display = 'none';

      fetch(LEAD_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      })
        .then(function (res) {
          if (!res.ok) {
            throw new Error('HTTP ' + res.status);
          }
          return res.json().catch(function () { return {}; });
        })
        .then(function () {
          // HTTP 2xx confirmado com sucesso
          leadSubmittedSuccessfully = true;
          showSuccessView(tipoCamaraVal, armazenarVal, ufVal, whatsappVal);
        })
        .catch(function (err) {
          console.error('[LP Webhook Error]', err);
          if (btnSubmit) {
            btnSubmit.disabled = false;
            btnSubmit.classList.remove('is-loading');
          }
          if (submitErrorWrap) {
            submitErrorWrap.style.display = 'block';
            submitErrorWrap.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
          }
        });
    }
  }

  // 12. SCROLL SUAVE PARA O FORMULÁRIO COM FOCO INTELIGENTE
  function irParaFormulario(targetField) {
    const form = document.getElementById('lp-form-lead');
    if (!form) return;

    const rect = form.getBoundingClientRect();
    const headerHeight = window.innerWidth <= 768 ? 64 : 72;
    const isFormVisible = (rect.top >= headerHeight && rect.top <= window.innerHeight * 0.7);
    const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (!isFormVisible) {
      form.scrollIntoView({
        behavior: prefersReduced ? 'auto' : 'smooth',
        block: 'start'
      });
    }

    const focusTarget = targetField || document.getElementById('lp-field-nome');
    if (focusTarget) {
      if (!isFormVisible) {
        setTimeout(function () {
          focusTarget.focus({ preventScroll: true });
        }, prefersReduced ? 50 : 350);
      } else {
        focusTarget.focus({ preventScroll: true });
      }
    }
  }

  // 13. BOTÕES DE WHATSAPP COM CÓDIGO DE REFERÊNCIA (ref) E ORIGEM
  function initWhatsAppButtons() {
    const waButtons = document.querySelectorAll('[data-whatsapp-btn]');
    const isDebug = new URLSearchParams(window.location.search).get('debug') === '1';

    waButtons.forEach(function (btn) {
      const origem = btn.getAttribute('data-whatsapp-btn') || 'cta_final';

      // Atualiza o href estático inicial com número real para acessibilidade e crawlers
      const initialMsg = origem === 'erro'
        ? 'Olá! Tentei enviar o formulário pelo site da JD mas deu erro, gostaria de pedir meu orçamento por aqui.'
        : 'Olá! Gostaria de receber um orçamento de câmara fria da JD.';
      btn.href = 'https://wa.me/' + WHATSAPP_NUMBER + '?text=' + encodeURIComponent(initialMsg);
      btn.setAttribute('target', '_blank');
      btn.setAttribute('rel', 'noopener noreferrer');

      btn.addEventListener('click', function (e) {
        e.preventDefault();

        const ref = generateWhatsAppRef();
        const consentStatus = getConsentStatus();

        let baseMsg = '';
        if (origem === 'erro') {
          baseMsg = 'Olá! Tentei enviar o formulário pelo site da JD mas deu erro, gostaria de pedir meu orçamento por aqui.';
        } else {
          baseMsg = 'Olá! Gostaria de receber um orçamento de câmara fria da JD.';
        }

        // Limpa ref anterior se houvesse e anexa o novo
        baseMsg = baseMsg.replace(/\s*\(ref:\s*[A-Z0-9]+\)$/i, '');
        const fullMsg = baseMsg + ' (ref: ' + ref + ')';

        // Registro leve no mesmo webhook (keepalive: true, falha em silêncio)
        const waPayload = {
          tipo_evento: 'click_whatsapp',
          ref: ref,
          lead_id: currentLeadId || '',
          origem: origem,
          timestamp_envio: getIsoTimestampSaoPaulo(),
          utm_source: currentAttrib.utm_source || '',
          utm_medium: currentAttrib.utm_medium || '',
          utm_campaign: currentAttrib.utm_campaign || '',
          utm_term: currentAttrib.utm_term || '',
          utm_content: currentAttrib.utm_content || '',
          matchtype: currentAttrib.matchtype || '',
          device: currentAttrib.device || '',
          network: currentAttrib.network || '',
          gclid: currentAttrib.gclid || '',
          gbraid: currentAttrib.gbraid || '',
          wbraid: currentAttrib.wbraid || '',
          landing_page: window.location.href,
          lp_version: 'A',
          titulo_variante: activeVariantKey,
          consent_ads: consentStatus.ads,
          consent_analytics: consentStatus.analytics
        };

        if (isDebug) {
          console.group('🔍 [LP Debug Mode] WhatsApp Click Webhook Ping');
          console.log('Payload Webhook Click:', waPayload);
          console.log('Código ref:', ref);
          console.groupEnd();
        } else if (LEAD_ENDPOINT) {
          try {
            fetch(LEAD_ENDPOINT, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(waPayload),
              keepalive: true
            }).catch(function () { /* fail silently */ });
          } catch (err) { /* fail silently */ }
        }

        // dataLayer (1 disparo por clique)
        window.dataLayer.push({
          event: 'click_whatsapp',
          origem: origem,
          ref: ref,
          lead_id: currentLeadId || '',
          lp_version: 'A',
          titulo_variante: activeVariantKey
        });

        // Redirecionamento
        const waUrl = 'https://wa.me/' + WHATSAPP_NUMBER + '?text=' + encodeURIComponent(fullMsg);
        window.open(waUrl, '_blank', 'noopener,noreferrer');
      });
    });
  }

  // 14. DEMAIS CTAS DA PÁGINA (Cabeçalho, Por Que a JD, Produtos, etc.)
  function initHeaderAndNavCtas() {
    // CTA do Cabeçalho
    const ctaHeader = document.getElementById('cta-header');
    if (ctaHeader) {
      ctaHeader.addEventListener('click', function (e) {
        e.preventDefault();
        pushTrackingEvent('click_cta_header');
        irParaFormulario();
      });
    }

    // CTA da Dobra 2 (Por que a JD)
    const ctaPorque = document.getElementById('cta-porque-jd');
    if (ctaPorque) {
      ctaPorque.addEventListener('click', function (e) {
        e.preventDefault();
        pushTrackingEvent('click_cta_porque');
        irParaFormulario();
      });
    }

    // CTAs da Dobra 3 (Produtos)
    const PRODUTO_MAP = {
      'mini': 'Mini câmara',
      'expositora': 'Câmara expositora (walk-in cooler)',
      'resfriados': 'Câmara de resfriados (0 a +15 °C)',
      'congelados': 'Câmara de congelados (-18 °C)'
    };

    const cardCtas = document.querySelectorAll('[data-cta-produto]');
    cardCtas.forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        const prodKey = btn.getAttribute('data-cta-produto');
        const tipoNome = PRODUTO_MAP[prodKey] || prodKey;

        // Pré-seleciona o tipo no select do formulário
        const selectTipo = document.getElementById('lp-field-tipo_camara');
        if (selectTipo) {
          selectTipo.value = tipoNome;
          selectTipo.dispatchEvent(new Event('change', { bubbles: true }));
          if (selectTipo.classList.contains('is-error')) {
            setFieldError(selectTipo, false);
          }
        }

        pushTrackingEvent('click_cta_produto', { produto: prodKey });

        // Se o formulário já foi enviado com sucesso, não reabre
        const formSucesso = document.getElementById('lp-form-sucesso');
        if (formSucesso && formSucesso.classList.contains('is-visible')) {
          return;
        }

        const nomeField = document.getElementById('lp-field-nome');
        let targetField = nomeField;
        if (nomeField && (nomeField.value || '').trim().length >= 3) {
          const requiredIds = [
            'lp-field-whatsapp',
            'lp-field-tipo_camara',
            'lp-field-armazenar',
            'lp-field-cidade',
            'lp-field-uf'
          ];
          for (let i = 0; i < requiredIds.length; i++) {
            const f = document.getElementById(requiredIds[i]);
            if (f && !f.value.trim()) {
              targetField = f;
              break;
            }
          }
        }

        irParaFormulario(targetField);
      });
    });

    // CTA da Dobra 4 (Como Funciona)
    const ctaComo = document.getElementById('cta-como');
    if (ctaComo) {
      ctaComo.addEventListener('click', function (e) {
        e.preventDefault();
        pushTrackingEvent('click_cta_como');
        irParaFormulario();
      });
    }

    // CTA da Dobra 6B (CTA Final)
    const ctaFinal = document.getElementById('cta-final-btn');
    if (ctaFinal) {
      ctaFinal.addEventListener('click', function (e) {
        e.preventDefault();
        pushTrackingEvent('click_cta_final');
        irParaFormulario();
      });
    }
  }

  // 15. RASTREAMENTO DO FAQ (Dobra 6A)
  function initFAQ() {
    const faqBtns = document.querySelectorAll('.jd-faq__pergunta');
    faqBtns.forEach(function (btn, index) {
      btn.addEventListener('click', function () {
        setTimeout(function () {
          if (btn.getAttribute('aria-expanded') === 'true') {
            pushTrackingEvent('faq_open', { pergunta: String(index + 1) });
          }
        }, 0);
      });
    });
  }

  // 16. BANNER DE COOKIES (LGPD) + CONSENT MODE V2
  function initCookieBanner() {
    // Aplica PRIVACY_URL unificada em todos os links da página
    const privacyLinks = document.querySelectorAll('[data-privacy-link]');
    privacyLinks.forEach(function (link) {
      link.href = PRIVACY_URL;
    });

    const banner = document.getElementById('lp-cookie-banner');
    if (!banner) return;

    const btnAcceptAll = document.getElementById('lp-cookie-accept-all');
    const btnRejectAll = document.getElementById('lp-cookie-reject-all');
    const btnCustomize = document.getElementById('lp-cookie-customize');
    const panel = document.getElementById('lp-cookie-panel');
    const btnSave = document.getElementById('lp-cookie-save');
    const switchAnalytics = document.getElementById('lp-cookie-switch-analytics');
    const switchAds = document.getElementById('lp-cookie-switch-ads');
    const btnReopen = document.getElementById('lp-cookie-pref-btn');

    function syncSwitchesWithState(analyticsVal, adsVal) {
      if (switchAnalytics) {
        switchAnalytics.setAttribute('aria-checked', analyticsVal ? 'true' : 'false');
      }
      if (switchAds) {
        switchAds.setAttribute('aria-checked', adsVal ? 'true' : 'false');
      }
    }

    function toggleSwitch(switchEl) {
      if (!switchEl || switchEl.disabled) return;
      const current = switchEl.getAttribute('aria-checked') === 'true';
      switchEl.setAttribute('aria-checked', current ? 'false' : 'true');
    }

    function openCustomPanel() {
      const consent = getConsentStatus();
      const analyticsVal = consent.analytics === 'granted';
      const adsVal = consent.ads === 'granted';
      syncSwitchesWithState(analyticsVal, adsVal);

      if (panel) {
        panel.removeAttribute('hidden');
      }
      if (btnCustomize) {
        btnCustomize.setAttribute('aria-expanded', 'true');
      }
      banner.classList.add('is-visible');
    }

    function saveConsentDecision(analyticsGranted, adsGranted) {
      const data = {
        analytics: Boolean(analyticsGranted),
        ads: Boolean(adsGranted),
        ts: Date.now()
      };

      try {
        localStorage.setItem(CONSENT_STORAGE_KEY, JSON.stringify(data));
      } catch (e) {
        /* noop: fallback gracioso para modo privado */
      }

      if (typeof window.gtag === 'function') {
        window.gtag('consent', 'update', {
          'ad_storage': data.ads ? 'granted' : 'denied',
          'ad_user_data': data.ads ? 'granted' : 'denied',
          'ad_personalization': data.ads ? 'granted' : 'denied',
          'analytics_storage': data.analytics ? 'granted' : 'denied'
        });
      }

      if (window.dataLayer) {
        window.dataLayer.push({
          event: 'consent_update',
          consent_analytics: data.analytics,
          consent_ads: data.ads,
          lp_version: 'A'
        });
      }

      // Reavalia persistência da atribuição com base no novo consentimento de ads
      saveAttrib(currentAttrib);
      updateHiddenConsentFields();

      banner.classList.remove('is-visible');
    }

    // Se já houver decisão válida (menor que 12 meses), não exibe o banner na visita inicial
    try {
      const raw = localStorage.getItem(CONSENT_STORAGE_KEY);
      if (raw) {
        const parsed = JSON.parse(raw);
        if (parsed && typeof parsed.ts === 'number' && (Date.now() - parsed.ts < CONSENT_EXPIRATION_MS)) {
          banner.classList.remove('is-visible');
        } else {
          banner.classList.add('is-visible');
        }
      } else {
        banner.classList.add('is-visible');
      }
    } catch (e) {
      banner.classList.add('is-visible');
    }

    if (btnAcceptAll) {
      btnAcceptAll.addEventListener('click', function () {
        saveConsentDecision(true, true);
      });
    }

    if (btnRejectAll) {
      btnRejectAll.addEventListener('click', function () {
        saveConsentDecision(false, false);
      });
    }

    if (btnCustomize) {
      btnCustomize.addEventListener('click', function () {
        const isHidden = panel ? panel.hasAttribute('hidden') : true;
        if (isHidden) {
          openCustomPanel();
        } else if (panel) {
          panel.setAttribute('hidden', '');
          btnCustomize.setAttribute('aria-expanded', 'false');
        }
      });
    }

    if (switchAnalytics) {
      switchAnalytics.addEventListener('click', function () {
        toggleSwitch(switchAnalytics);
      });
      switchAnalytics.addEventListener('keydown', function (e) {
        if (e.key === ' ' || e.key === 'Enter') {
          e.preventDefault();
          toggleSwitch(switchAnalytics);
        }
      });
    }

    if (switchAds) {
      switchAds.addEventListener('click', function () {
        toggleSwitch(switchAds);
      });
      switchAds.addEventListener('keydown', function (e) {
        if (e.key === ' ' || e.key === 'Enter') {
          e.preventDefault();
          toggleSwitch(switchAds);
        }
      });
    }

    if (btnSave) {
      btnSave.addEventListener('click', function () {
        const analyticsVal = switchAnalytics ? switchAnalytics.getAttribute('aria-checked') === 'true' : false;
        const adsVal = switchAds ? switchAds.getAttribute('aria-checked') === 'true' : false;
        saveConsentDecision(analyticsVal, adsVal);
      });
    }

    if (btnReopen) {
      btnReopen.addEventListener('click', function () {
        openCustomPanel();
        if (switchAnalytics) {
          switchAnalytics.focus();
        }
      });
    }
  }

  // 17. SPOTLIGHT MOUSE TRACKER
  function initSpotlight() {
    const spotlights = document.querySelectorAll('.jd-spotlight');
    spotlights.forEach(function (el) {
      el.addEventListener('mousemove', function (e) {
        var rect = el.getBoundingClientRect();
        el.style.setProperty('--mouse-x', (e.clientX - rect.left) + 'px');
        el.style.setProperty('--mouse-y', (e.clientY - rect.top) + 'px');
      }, { passive: true });
    });
  }

  // INICIALIZAÇÃO
  function init() {
    applyDynamicHeadline();
    initAttribution();
    initLeadForm();
    initWhatsAppButtons();
    initHeaderAndNavCtas();
    initFAQ();
    initSpotlight();
    initCookieBanner();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
