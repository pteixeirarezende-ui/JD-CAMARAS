/* ============================================================================
   JD CÂMARAS FRIAS — DS.JS
   Funcionalidades core: formulário, máscara, UTM, header, FAQ, lightbox.
   Sem dependências externas. < 10 kB minificado.
   ============================================================================ */

(function () {
  'use strict';

  /* ====================================================================
     UTM & GCLID — Preenche campos ocultos a partir da URL
     ==================================================================== */
  function captureUTM() {
    var params = new URLSearchParams(window.location.search);
    var fields = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'gclid'];
    fields.forEach(function (key) {
      var value = params.get(key);
      if (value) {
        var els = document.querySelectorAll('input[name="' + key + '"]');
        els.forEach(function (el) { el.value = value; });
        // Salva no sessionStorage para persistir entre páginas
        try { sessionStorage.setItem('jd_' + key, value); } catch (e) { /* noop */ }
      } else {
        // Recupera do sessionStorage se disponível
        try {
          var stored = sessionStorage.getItem('jd_' + key);
          if (stored) {
            var els = document.querySelectorAll('input[name="' + key + '"]');
            els.forEach(function (el) { el.value = stored; });
          }
        } catch (e) { /* noop */ }
      }
    });
  }


  /* ====================================================================
     MÁSCARA DE TELEFONE BR — (XX) XXXXX-XXXX
     ==================================================================== */
  function maskPhone(input) {
    input.addEventListener('input', function () {
      var v = this.value.replace(/\D/g, '');
      if (v.length > 11) v = v.slice(0, 11);

      if (v.length > 6) {
        this.value = '(' + v.slice(0, 2) + ') ' + v.slice(2, 7) + '-' + v.slice(7);
      } else if (v.length > 2) {
        this.value = '(' + v.slice(0, 2) + ') ' + v.slice(2);
      } else if (v.length > 0) {
        this.value = '(' + v;
      }
    });

    // Permite apenas números e caracteres de controle
    input.addEventListener('keypress', function (e) {
      if (!/\d/.test(e.key) && e.key !== 'Backspace' && e.key !== 'Delete' && e.key !== 'Tab') {
        e.preventDefault();
      }
    });
  }


  /* ====================================================================
     VALIDAÇÃO INLINE
     ==================================================================== */
  function validateField(input) {
    var group = input.closest('.jd-form__group');
    if (!group) return true;

    var isValid = true;
    var errorEl = group.querySelector('.jd-form__error');

    // Required
    if (input.hasAttribute('required') && !input.value.trim()) {
      isValid = false;
      if (errorEl) errorEl.textContent = 'Campo obrigatório';
    }

    // Telefone — mínimo 14 caracteres com máscara
    if (input.type === 'tel' && input.value.trim()) {
      var digits = input.value.replace(/\D/g, '');
      if (digits.length < 10) {
        isValid = false;
        if (errorEl) errorEl.textContent = 'Informe um telefone válido com DDD';
      }
    }

    // Nome — mínimo 3 caracteres
    if (input.name === 'nome' && input.value.trim()) {
      if (input.value.trim().length < 3) {
        isValid = false;
        if (errorEl) errorEl.textContent = 'Informe seu nome completo';
      }
    }

    if (isValid) {
      group.classList.remove('is-error');
      input.classList.remove('is-error');
    } else {
      group.classList.add('is-error');
      input.classList.add('is-error');
    }

    return isValid;
  }


  /* ====================================================================
     FORMULÁRIO EM 2 ETAPAS
     ==================================================================== */
  function initForms() {
    var forms = document.querySelectorAll('.jd-form');

    forms.forEach(function (form) {
      var etapas = form.querySelectorAll('.jd-form__etapa');
      var steps = form.querySelectorAll('.jd-form__step');
      var btnNext = form.querySelector('[data-action="next"]');
      var btnPrev = form.querySelector('[data-action="prev"]');
      var btnSubmit = form.querySelector('[data-action="submit"]');
      var successEl = form.querySelector('.jd-form__sucesso');
      var currentStep = 0;

      function showStep(index) {
        etapas.forEach(function (e, i) {
          e.classList.toggle('is-active', i === index);
        });

        steps.forEach(function (s, i) {
          s.classList.remove('is-active', 'is-done', 'is-pending');
          if (i < index) s.classList.add('is-done');
          else if (i === index) s.classList.add('is-active');
          else s.classList.add('is-pending');
        });

        if (btnPrev) btnPrev.style.display = index === 0 ? 'none' : '';
        if (btnNext) btnNext.style.display = index === etapas.length - 1 ? 'none' : '';
        if (btnSubmit) btnSubmit.style.display = index === etapas.length - 1 ? '' : 'none';

        currentStep = index;
      }

      // Próxima etapa
      if (btnNext) {
        btnNext.addEventListener('click', function (e) {
          e.preventDefault();
          var currentEtapa = etapas[currentStep];
          var inputs = currentEtapa.querySelectorAll('.jd-form__input, .jd-form__select');
          var allValid = true;

          inputs.forEach(function (input) {
            if (!validateField(input)) allValid = false;
          });

          if (allValid && currentStep < etapas.length - 1) {
            showStep(currentStep + 1);
            // Foco no primeiro campo da próxima etapa
            var firstInput = etapas[currentStep].querySelector('.jd-form__input, .jd-form__select');
            if (firstInput) firstInput.focus();
          }
        });
      }

      // Etapa anterior
      if (btnPrev) {
        btnPrev.addEventListener('click', function (e) {
          e.preventDefault();
          if (currentStep > 0) showStep(currentStep - 1);
        });
      }

      // Enviar (simulado no DS)
      if (btnSubmit) {
        btnSubmit.addEventListener('click', function (e) {
          e.preventDefault();
          var currentEtapa = etapas[currentStep];
          var inputs = currentEtapa.querySelectorAll('.jd-form__input, .jd-form__select');
          var allValid = true;

          inputs.forEach(function (input) {
            if (!validateField(input)) allValid = false;
          });

          if (allValid) {
            // Esconde formulário, mostra sucesso
            etapas.forEach(function (e) { e.classList.remove('is-active'); });
            form.querySelector('.jd-form__steps').style.display = 'none';
            form.querySelector('.jd-form__header').style.display = 'none';
            var actions = form.querySelector('.jd-form__actions');
            if (actions) actions.style.display = 'none';
            if (successEl) successEl.classList.add('is-visible');
          }
        });
      }

      // Validação on blur
      var allInputs = form.querySelectorAll('.jd-form__input, .jd-form__select');
      allInputs.forEach(function (input) {
        input.addEventListener('blur', function () {
          validateField(this);
        });
        // Remove erro ao digitar
        input.addEventListener('input', function () {
          var group = this.closest('.jd-form__group');
          if (group && group.classList.contains('is-error')) {
            group.classList.remove('is-error');
            this.classList.remove('is-error');
          }
        });
      });

      // Init
      showStep(0);
    });

    // Init phone masks
    var phoneInputs = document.querySelectorAll('input[type="tel"]');
    phoneInputs.forEach(maskPhone);
  }


  /* ====================================================================
     HEADER — Scroll behavior (esconde ao descer, mostra ao subir)
     ==================================================================== */
  function initHeader() {
    var header = document.querySelector('.jd-header');
    if (!header) return;

    var lastScroll = 0;
    var threshold = 80;

    window.addEventListener('scroll', function () {
      var currentScroll = window.pageYOffset;

      // Adiciona sombra quando scrollado
      header.classList.toggle('is-scrolled', currentScroll > 10);

      // Esconde/mostra no mobile
      if (currentScroll > threshold) {
        if (currentScroll > lastScroll) {
          header.classList.add('is-hidden');
        } else {
          header.classList.remove('is-hidden');
        }
      } else {
        header.classList.remove('is-hidden');
      }

      lastScroll = currentScroll;
    }, { passive: true });
  }


  /* ====================================================================
     FAQ — Acordeão acessível
     ==================================================================== */
  function initFAQ() {
    var items = document.querySelectorAll('.jd-faq__item');

    items.forEach(function (item) {
      var btn = item.querySelector('.jd-faq__pergunta');
      var answer = item.querySelector('.jd-faq__resposta');

      if (!btn || !answer) return;

      // Setup ARIA
      var id = 'faq-' + Math.random().toString(36).slice(2, 8);
      btn.setAttribute('aria-expanded', 'false');
      btn.setAttribute('aria-controls', id);
      answer.setAttribute('id', id);
      answer.setAttribute('role', 'region');
      answer.setAttribute('aria-labelledby', btn.id || id + '-btn');
      if (!btn.id) btn.id = id + '-btn';

      btn.addEventListener('click', function () {
        var isOpen = item.classList.contains('is-open');

        // Fecha outros (comportamento accordion)
        items.forEach(function (other) {
          if (other !== item && other.classList.contains('is-open')) {
            other.classList.remove('is-open');
            other.querySelector('.jd-faq__pergunta').setAttribute('aria-expanded', 'false');
          }
        });

        item.classList.toggle('is-open', !isOpen);
        btn.setAttribute('aria-expanded', !isOpen ? 'true' : 'false');
      });
    });
  }


  /* ====================================================================
     LIGHTBOX — Galeria simples
     ==================================================================== */
  function initLightbox() {
    var lightbox = document.querySelector('.jd-lightbox');
    if (!lightbox) return;

    var img = lightbox.querySelector('.jd-lightbox__img');
    var closeBtn = lightbox.querySelector('.jd-lightbox__close');
    var items = document.querySelectorAll('.jd-galeria__item');

    items.forEach(function (item) {
      item.addEventListener('click', function () {
        var src = item.querySelector('img');
        if (src && img) {
          img.src = src.src;
          img.alt = src.alt || '';
          lightbox.classList.add('is-open');
          document.body.style.overflow = 'hidden';
          closeBtn.focus();
        }
      });
    });

    function closeLightbox() {
      lightbox.classList.remove('is-open');
      document.body.style.overflow = '';
    }

    if (closeBtn) closeBtn.addEventListener('click', closeLightbox);

    lightbox.addEventListener('click', function (e) {
      if (e.target === lightbox) closeLightbox();
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && lightbox.classList.contains('is-open')) {
        closeLightbox();
      }
    });
  }


  /* ====================================================================
     COOKIES BANNER — Consent Mode v2 ready
     ==================================================================== */
  function initCookies() {
    var banner = document.querySelector('.jd-cookies');
    if (!banner) return;

    // Check if consent was already given
    try {
      var consent = localStorage.getItem('jd_consent');
      if (consent) return; // Already decided
    } catch (e) { /* noop */ }

    // Show banner after 1 second
    setTimeout(function () {
      banner.classList.add('is-visible');
    }, 1000);

    var btnAceitar = banner.querySelector('.jd-cookies__btn--aceitar');
    var btnRecusar = banner.querySelector('.jd-cookies__btn--recusar');
    var btnAjustar = banner.querySelector('.jd-cookies__btn--ajustar');

    function setConsent(value) {
      try { localStorage.setItem('jd_consent', value); } catch (e) { /* noop */ }
      banner.classList.remove('is-visible');

      // Consent Mode v2 — Push to dataLayer if available
      if (window.dataLayer) {
        window.dataLayer.push({
          event: 'consent_update',
          consent_action: value
        });
      }

      // gtag consent update
      if (typeof gtag === 'function') {
        if (value === 'accepted') {
          gtag('consent', 'update', {
            'ad_storage': 'granted',
            'analytics_storage': 'granted',
            'ad_user_data': 'granted',
            'ad_personalization': 'granted'
          });
        } else {
          gtag('consent', 'update', {
            'ad_storage': 'denied',
            'analytics_storage': 'denied',
            'ad_user_data': 'denied',
            'ad_personalization': 'denied'
          });
        }
      }
    }

    if (btnAceitar) btnAceitar.addEventListener('click', function () { setConsent('accepted'); });
    if (btnRecusar) btnRecusar.addEventListener('click', function () { setConsent('denied'); });
    if (btnAjustar) btnAjustar.addEventListener('click', function () {
      // Placeholder — em produção, abre modal de preferências
      setConsent('custom');
    });
  }


  /* ====================================================================
     INIT
     ==================================================================== */
    /* ====================================================================
     AJUSTE 5: WHATSAPP NUMBER & BLINDAGEM DE PUBLICAÇÃO
     ==================================================================== */
  var WHATSAPP_NUMBER = ''; // TODO: preencher com DDI+DDD+número (ex.: 5562900000000)

  function initWhatsApp() {
    var buttons = document.querySelectorAll('.jd-btn--whatsapp, [data-whatsapp-btn]');
    buttons.forEach(function (btn) {
      if (!WHATSAPP_NUMBER) {
        btn.setAttribute('aria-disabled', 'true');
        btn.setAttribute('title', 'Número de WhatsApp a confirmar pelo cliente');
        btn.href = 'javascript:void(0);';
        btn.style.opacity = '0.9';
        btn.style.cursor = 'not-allowed';

        if (!btn.querySelector('.tag-confirmar-wa')) {
          var tag = document.createElement('span');
          tag.className = 'tag-exemplo tag-confirmar-wa';
          tag.style.marginLeft = '8px';
          tag.style.fontSize = '10px';
          tag.textContent = 'CONFIRMAR NÚMERO';
          btn.appendChild(tag);
        }

        btn.addEventListener('click', function (e) {
          e.preventDefault();
          alert('Número de WhatsApp ainda não configurado pela JD [CONFIRMAR NÚMERO].');
        });
      } else {
        btn.href = 'https://wa.me/' + WHATSAPP_NUMBER;
      }
    });
  }

  function init() {
    initWhatsApp();
    captureUTM();
    initForms();
    initHeader();
    initFAQ();
    initLightbox();
    initCookies();
  }

  // DOMContentLoaded ou já pronto
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
