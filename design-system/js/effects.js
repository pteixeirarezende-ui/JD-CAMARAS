/* ============================================================================
   JD CÂMARAS FRIAS — EFFECTS.JS (Cryogenic Engine & Interactive FX)
   Supercharged interactivity:
   - Dynamic Mouse Spotlight
   - Thermodynamic Digital HUD Controller (-18°C / +2°C / +15°C)
   - Real-time Cold Room Sizing & Load Calculator
   - Isometric Cold Room Layer Explorer
   - Web Audio Industrial Haptic Feedback (Synthesized, 0KB audio files)
   - Ambient Frost Canvas Particle Drift
   - 1-Click Code Copy with Toast
   - Factory Dark / Clean Chamber Theme Switcher
   ============================================================================ */

(function () {
  'use strict';

  /* ====================================================================
     1. SYNTHESIZED WEB AUDIO ENGINE (Sons Táteis Industriais)
     ==================================================================== */
  var audioCtx = null;
  var soundEnabled = false;

  function initAudio() {
    if (!audioCtx) {
      var AudioContext = window.AudioContext || window.webkitAudioContext;
      if (AudioContext) {
        audioCtx = new AudioContext();
      }
    }
    if (audioCtx && audioCtx.state === 'suspended') {
      audioCtx.resume();
    }
  }

  function playRelayClick(freq, duration) {
    if (!soundEnabled || !audioCtx) return;
    try {
      var osc = audioCtx.createOscillator();
      var gain = audioCtx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(freq || 1200, audioCtx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(180, audioCtx.currentTime + (duration || 0.04));

      gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + (duration || 0.04));

      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.start();
      osc.stop(audioCtx.currentTime + (duration || 0.04));
    } catch (e) {
      // Audio fail silent
    }
  }

  // Ativa áudio no primeiro clique do usuário se habilitado
  window.addEventListener('click', function () {
    if (soundEnabled && !audioCtx) initAudio();
  }, { once: true });


  /* ====================================================================
     2. DYNAMIC MOUSE SPOTLIGHT TRACKER
     ==================================================================== */
  function initSpotlights() {
    var cards = document.querySelectorAll('.jd-spotlight');
    cards.forEach(function (card) {
      card.addEventListener('mousemove', function (e) {
        var rect = card.getBoundingClientRect();
        var x = e.clientX - rect.left;
        var y = e.clientY - rect.top;
        card.style.setProperty('--mouse-x', x + 'px');
        card.style.setProperty('--mouse-y', y + 'px');
      });
    });
  }


  /* ====================================================================
     3. THERMODYNAMIC CONTROLLER (-18°C, 2°C, 15°C)
     ==================================================================== */
  var currentTemp = -18.0;

  function initThermostat() {
    var tempDisplays = document.querySelectorAll('.jd-live-temp');
    var modeButtons = document.querySelectorAll('[data-temp-mode]');
    var statusLabels = document.querySelectorAll('.jd-live-temp-status');

    function setTemperature(targetTemp, labelText) {
      initAudio();
      playRelayClick(980, 0.06);

      var start = currentTemp;
      var startTime = performance.now();
      var duration = 400;

      function update(now) {
        var elapsed = now - startTime;
        var progress = Math.min(elapsed / duration, 1);
        var eased = 1 - Math.pow(1 - progress, 3);
        var val = start + (targetTemp - start) * eased;

        tempDisplays.forEach(function (el) {
          var sign = val > 0 ? '+' : '';
          el.textContent = sign + val.toFixed(1).replace('.', ',');
        });

        if (progress < 1) {
          requestAnimationFrame(update);
        } else {
          currentTemp = targetTemp;
          tempDisplays.forEach(function (el) {
            var sign = targetTemp > 0 ? '+' : '';
            el.textContent = sign + targetTemp.toFixed(1).replace('.', ',');
          });
        }
      }
      requestAnimationFrame(update);

      if (labelText) {
        statusLabels.forEach(function (el) {
          el.textContent = labelText;
        });
      }

      // Atualiza visual dos botões
      modeButtons.forEach(function (btn) {
        if (parseFloat(btn.getAttribute('data-temp-target')) === targetTemp) {
          btn.classList.add('is-active');
        } else {
          btn.classList.remove('is-active');
        }
      });
    }

    modeButtons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var t = parseFloat(btn.getAttribute('data-temp-target'));
        var label = btn.getAttribute('data-temp-label') || '';
        setTemperature(t, label);
      });
    });
  }


  /* ====================================================================
     4. REAL-TIME SIZING & COOLING LOAD CALCULATOR
     ==================================================================== */
  function initCalculator() {
    var inputLargura = document.getElementById('calc-largura');
    var inputComprimento = document.getElementById('calc-comprimento');
    var inputAltura = document.getElementById('calc-altura');
    var inputAplicacao = document.getElementById('calc-aplicacao');

    var outVolume = document.getElementById('calc-out-volume');
    var outPainel = document.getElementById('calc-out-painel');
    var outBTU = document.getElementById('calc-out-btu');
    var outCapacidade = document.getElementById('calc-out-capacidade');
    var outPIR = document.getElementById('calc-out-pir');

    if (!inputLargura || !inputComprimento || !inputAltura) return;

    function recalculate() {
      var w = parseFloat(inputLargura.value) || 3.0;
      var l = parseFloat(inputComprimento.value) || 4.0;
      var h = parseFloat(inputAltura.value) || 2.8;
      var app = inputAplicacao ? inputAplicacao.value : 'congelados';

      // Atualiza mostradores dos sliders
      var labelW = document.getElementById('calc-val-largura');
      var labelL = document.getElementById('calc-val-comprimento');
      var labelH = document.getElementById('calc-val-altura');
      if (labelW) labelW.textContent = w.toFixed(1) + ' m';
      if (labelL) labelL.textContent = l.toFixed(1) + ' m';
      if (labelH) labelH.textContent = h.toFixed(1) + ' m';

      // Volume = W * L * H
      var volume = w * l * h;
      // Área de painéis (Paredes + Teto + Piso)
      var areaPaineis = 2 * (w * h) + 2 * (l * h) + 2 * (w * l);

      // Carga térmica aproximada
      var btuM3 = (app === 'congelados') ? 950 : 650;
      var totalBTU = Math.round(volume * btuM3 / 1000) * 1000;
      var hpEstimado = (totalBTU / 12000).toFixed(1);

      // Espessura PIR recomendada
      var pirRecomendado = (app === 'congelados') ? 'PIR 100 mm' : (volume > 50 ? 'PIR 70 mm' : 'PIR 50 mm');

      // Capacidade estimada de estocagem
      var caixas = Math.round(volume * 18);
      var paletes = Math.max(1, Math.floor((w * l) / 1.8));

      if (outVolume) outVolume.textContent = volume.toFixed(1) + ' m³';
      if (outPainel) outPainel.textContent = Math.round(areaPaineis) + ' m²';
      if (outBTU) outBTU.textContent = totalBTU.toLocaleString('pt-BR') + ' BTU/h (' + hpEstimado + ' HP)';
      if (outPIR) outPIR.textContent = pirRecomendado;
      if (outCapacidade) {
        if (app === 'congelados') {
          outCapacidade.textContent = '~' + Math.round(volume * 160) + ' kg carnes/congelados';
        } else {
          outCapacidade.textContent = '~' + caixas.toLocaleString('pt-BR') + ' caixas / ' + paletes + ' paletes PBR';
        }
      }
    }

    [inputLargura, inputComprimento, inputAltura, inputAplicacao].forEach(function (el) {
      if (el) {
        el.addEventListener('input', function () {
          recalculate();
          playRelayClick(800, 0.02);
        });
      }
    });

    recalculate();
  }


  /* ====================================================================
     5. ISOMETRIC COLD ROOM EXPLORER (Camadas Interativas)
     ==================================================================== */
  function initIsoExplorer() {
    var isoTabs = document.querySelectorAll('[data-iso-layer]');
    var isoLayers = document.querySelectorAll('[data-iso-target]');
    var infoTitle = document.getElementById('iso-info-title');
    var infoDesc = document.getElementById('iso-info-desc');

    var specs = {
      all: {
        title: 'Câmara Fria Modular Completa',
        desc: 'Projeto 100% sob medida com estanqueidade total, piso antiderrapante, iluminação estanque e sistema de refrigeração plug-in ou remoto.'
      },
      pir: {
        title: 'Painéis Termoisolantes PIR 100mm / 70mm',
        desc: 'Núcleo em poliisocianurato retardante de chama classe II-A (IT-10), chapa de aço galvanizado pré-pintado 0,5mm RAL 9003 com encaixe macho-fêmea hermético.'
      },
      refrig: {
        title: 'Unidade Evaporadora & Compressor',
        desc: 'Evaporador de alto rendimento com ventiladores axiais eletrônicos, degelo elétrico inteligente e motocompressor de alta eficiência energética.'
      },
      doors: {
        title: 'Porta Frigorífica Semi-embutida & Cortina PVC',
        desc: 'Vedação por gaxeta magnética dupla, resistência elétrica de aquecimento no batente (evita congelamento), maçaneta com destravamento interno de segurança.'
      }
    };

    isoTabs.forEach(function (tab) {
      tab.addEventListener('click', function () {
        var layerKey = tab.getAttribute('data-iso-layer');
        initAudio();
        playRelayClick(1100, 0.04);

        isoTabs.forEach(function (t) { t.classList.remove('is-active'); });
        tab.classList.add('is-active');

        isoLayers.forEach(function (layer) {
          var target = layer.getAttribute('data-iso-target');
          if (layerKey === 'all' || target === layerKey) {
            layer.style.opacity = '1';
            layer.style.filter = 'none';
          } else {
            layer.style.opacity = '0.15';
            layer.style.filter = 'grayscale(100%)';
          }
        });

        if (specs[layerKey] && infoTitle && infoDesc) {
          infoTitle.textContent = specs[layerKey].title;
          infoDesc.textContent = specs[layerKey].desc;
        }
      });
    });
  }


  /* ====================================================================
     6. AMBIENT FROST CANVAS PARTICLES (Micro Cristais Flutuantes)
     ==================================================================== */
  function initFrostCanvas() {
    var canvas = document.getElementById('jd-frost-canvas');
    if (!canvas) return;

    var ctx = canvas.getContext('2d');
    var particles = [];
    var particleCount = 28;
    var width, height;

    function resize() {
      width = canvas.width = canvas.parentElement.offsetWidth || window.innerWidth;
      height = canvas.height = canvas.parentElement.offsetHeight || 500;
    }
    resize();
    window.addEventListener('resize', resize);

    for (var i = 0; i < particleCount; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        size: Math.random() * 2.2 + 0.8,
        speedY: -(Math.random() * 0.4 + 0.15),
        speedX: (Math.random() - 0.5) * 0.3,
        opacity: Math.random() * 0.5 + 0.2,
        pulse: Math.random() * Math.PI
      });
    }

    function animate() {
      ctx.clearRect(0, 0, width, height);

      particles.forEach(function (p) {
        p.y += p.speedY;
        p.x += p.speedX;
        p.pulse += 0.02;

        if (p.y < 0) {
          p.y = height;
          p.x = Math.random() * width;
        }
        if (p.x < 0) p.x = width;
        if (p.x > width) p.x = 0;

        var currentAlpha = p.opacity + Math.sin(p.pulse) * 0.15;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(0, 224, 240, ' + Math.max(0, currentAlpha) + ')';
        ctx.shadowBlur = 8;
        ctx.shadowColor = 'rgba(0, 224, 240, 0.6)';
        ctx.fill();
      });

      requestAnimationFrame(animate);
    }
    animate();
  }


  /* ====================================================================
     7. 1-CLICK CODE COPY WITH TOAST
     ==================================================================== */
  function initCopyButtons() {
    var copyTriggers = document.querySelectorAll('[data-copy]');
    var toast = document.createElement('div');
    toast.className = 'jd-copy-toast';
    toast.style.cssText = 'position:fixed;bottom:24px;right:24px;background:#09080F;border:1px solid #00E0F0;color:#FFFFFF;padding:10px 18px;border-radius:6px;font-size:12px;font-weight:700;letter-spacing:0.05em;z-index:9999;box-shadow:0 10px 30px rgba(0,0,0,0.6);opacity:0;transform:translateY(10px);transition:all 0.25s ease;pointer-events:none;display:flex;align-items:center;gap:8px;';
    toast.innerHTML = '<span style="color:#00E676;font-size:14px;">✔</span> <span id="jd-toast-msg">Copiado para a área de transferência!</span>';
    document.body.appendChild(toast);

    var toastTimeout = null;

    copyTriggers.forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        var text = btn.getAttribute('data-copy');
        if (!text) return;

        navigator.clipboard.writeText(text).then(function () {
          initAudio();
          playRelayClick(1400, 0.05);

          var msg = btn.getAttribute('data-copy-label') || 'Copiado com sucesso!';
          document.getElementById('jd-toast-msg').textContent = msg;

          toast.style.opacity = '1';
          toast.style.transform = 'translateY(0)';

          clearTimeout(toastTimeout);
          toastTimeout = setTimeout(function () {
            toast.style.opacity = '0';
            toast.style.transform = 'translateY(10px)';
          }, 2200);
        });
      });
    });
  }


  /* ====================================================================
     8. FACTORY DARK / CLEAN CHAMBER THEME SWITCHER
     ==================================================================== */
  function initThemeSwitcher() {
    var themeToggle = document.getElementById('jd-theme-toggle');
    if (!themeToggle) return;

    themeToggle.addEventListener('click', function () {
      initAudio();
      playRelayClick(1000, 0.04);
      var currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
      var newTheme = currentTheme === 'dark' ? 'clean' : 'dark';
      document.documentElement.setAttribute('data-theme', newTheme);
      themeToggle.setAttribute('data-current', newTheme);

      var label = themeToggle.querySelector('.jd-theme-label');
      if (label) {
        label.textContent = newTheme === 'dark' ? 'MODO FÁBRICA' : 'MODO SALA LIMPA';
      }
    });
  }


  /* ====================================================================
     9. AUDIO SFX TOGGLE (Mudo / Ativado)
     ==================================================================== */
  function initSoundToggle() {
    var sfxToggle = document.getElementById('jd-sfx-toggle');
    if (!sfxToggle) return;

    sfxToggle.addEventListener('click', function () {
      soundEnabled = !soundEnabled;
      if (soundEnabled) {
        initAudio();
        playRelayClick(1200, 0.08);
      }
      sfxToggle.classList.toggle('is-active', soundEnabled);
      var label = sfxToggle.querySelector('.jd-sfx-label');
      if (label) {
        label.textContent = soundEnabled ? 'SFX: ATIVADO' : 'SFX: MUDO';
      }
    });
  }


  /* ====================================================================
     INICIALIZAÇÃO QUANDO DOM PRONTO
     ==================================================================== */
  function init() {
    initSpotlights();
    initThermostat();
    initCalculator();
    initIsoExplorer();
    initFrostCanvas();
    initCopyButtons();
    initThemeSwitcher();
    initSoundToggle();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
