# -*- coding: utf-8 -*-
"""
Gerador oficial do Design System JD Câmaras Frias
Cria design-system.html e ds_oficial.html com codificação UTF-8 pura.
"""
import os

HTML_CONTENT = r'''<!DOCTYPE html>
<html lang="pt-BR" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JD Câmaras Frias — Design System Industrial & Criogênico</title>
  <meta name="description" content="Design System de alta performance para JD Câmaras Frias. Engenharia termodinâmica de precisão, simulador interativo e catálogo completo de componentes.">

  <!-- Google Fonts: Archivo (Display pesado de fábrica), Inter (Corpo) e JetBrains Mono (Telemetria) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Archivo:wght@800;900&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">

  <!-- Design System CSS Core -->
  <link rel="stylesheet" href="{PATH_PREFIX}css/tokens.css">
  <link rel="stylesheet" href="{PATH_PREFIX}css/base.css">
  <link rel="stylesheet" href="{PATH_PREFIX}css/components.css">
  <link rel="stylesheet" href="{PATH_PREFIX}css/effects.css">

  <style>
    /* ================================================================
       CATALOG MASTER SHELL — Inspirado em Aura, IX-7 & Otto
       ================================================================ */
    :root {
      --ds-top: 64px;
      --ds-bg: #0C0B14;
      --ds-panel: rgba(18, 17, 31, 0.88);
      --ds-border: rgba(55, 180, 206, 0.22);
      --ds-text: #F0F4F8;
      --ds-muted: #9CADC2;
      --ds-cyan: #00E0F0;
    }

    [data-theme="clean"] {
      --ds-bg: #F4F6F9;
      --ds-panel: #FFFFFF;
      --ds-border: #D8DDE3;
      --ds-text: #101010;
      --ds-muted: #5A6A80;
      --ds-cyan: #4181BC;
    }

    * { box-sizing: border-box; }
    html, body {
      margin: 0;
      padding: 0;
      width: 100%;
      min-height: 100%;
      background: var(--ds-bg);
      color: var(--ds-text);
      font-family: var(--jd-font-body);
      overflow-x: hidden;
      transition: background 0.3s ease, color 0.3s ease;
    }

    /* Header Fixo de Comando */
    .catalog-header {
      position: sticky;
      top: 0;
      z-index: 1000;
      height: var(--ds-top);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 clamp(16px, 3vw, 32px);
      background: rgba(12, 11, 20, 0.94);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--ds-border);
      gap: 16px;
    }

    [data-theme="clean"] .catalog-header {
      background: rgba(255, 255, 255, 0.96);
      border-bottom-color: #E2E8F0;
    }

    .catalog-brand {
      display: flex;
      align-items: center;
      gap: 14px;
      text-decoration: none;
    }

    .catalog-brand img {
      height: 32px;
      filter: drop-shadow(0 0 12px rgba(0, 224, 240, 0.4));
    }

    .catalog-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.14em;
      color: var(--jd-ciano);
      padding: 3px 8px;
      background: rgba(55, 180, 206, 0.12);
      border: 1px solid rgba(55, 180, 206, 0.3);
      border-radius: 4px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    /* Navegação Principal das Abas (Overview vs Components) */
    .catalog-nav {
      display: flex;
      align-items: center;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 50px;
      padding: 4px;
      gap: 4px;
    }

    [data-theme="clean"] .catalog-nav {
      background: #E2E8F0;
      border-color: #CBD5E1;
    }

    .catalog-nav-btn {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 6px 16px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11.5px;
      font-weight: 700;
      letter-spacing: 0.06em;
      color: var(--ds-muted);
      border: none;
      background: transparent;
      border-radius: 50px;
      cursor: pointer;
      transition: all 0.25s ease;
      text-decoration: none;
    }

    .catalog-nav-btn:hover {
      color: #FFFFFF;
    }

    .catalog-nav-btn.is-active {
      background: var(--jd-azul);
      color: #FFFFFF;
      box-shadow: 0 0 16px rgba(0, 224, 240, 0.4);
    }

    /* Controles do HUD no Header */
    .catalog-controls {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }

    .catalog-tool-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 12px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 700;
      background: rgba(255, 255, 255, 0.06);
      color: #FFFFFF;
      border: 1px solid rgba(255, 255, 255, 0.14);
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .catalog-tool-btn:hover {
      background: rgba(55, 180, 206, 0.2);
      border-color: var(--jd-ciano);
      box-shadow: 0 0 14px rgba(0, 224, 240, 0.3);
    }

    .catalog-tool-btn.is-active {
      background: var(--jd-azul);
      border-color: var(--jd-ciano-logo-para);
    }

    /* Views */
    .catalog-view {
      display: none;
      width: 100%;
    }

    .catalog-view.is-active {
      display: block;
    }

    /* Layout da View de Componentes */
    .components-shell {
      display: grid;
      grid-template-columns: 280px minmax(0, 1fr);
      min-height: calc(100vh - var(--ds-top));
    }

    @media (max-width: 1024px) {
      .components-shell {
        grid-template-columns: 1fr;
      }
    }

    .components-sidebar {
      position: sticky;
      top: var(--ds-top);
      height: calc(100vh - var(--ds-top));
      overflow-y: auto;
      background: rgba(18, 17, 31, 0.65);
      border-right: 1px solid var(--ds-border);
      padding: 24px 16px 48px;
      display: flex;
      flex-direction: column;
      gap: 3px;
      scrollbar-width: thin;
      scrollbar-color: rgba(55, 180, 206, 0.3) transparent;
    }

    [data-theme="clean"] .components-sidebar {
      background: #FFFFFF;
      border-right-color: #E2E8F0;
    }

    @media (max-width: 1024px) {
      .components-sidebar {
        position: relative;
        top: 0;
        height: auto;
        flex-direction: row;
        flex-wrap: wrap;
        padding: 14px;
        gap: 6px;
      }
    }

    .components-sidebar__group-label {
      padding: 16px 12px 6px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 9.5px;
      font-weight: 700;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: rgba(156, 173, 194, 0.6);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .components-sidebar a {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 9px 12px;
      border-radius: var(--jd-radius);
      font-size: 13px;
      font-weight: var(--jd-fw-semibold);
      color: var(--ds-muted);
      transition: all 0.2s ease;
      text-decoration: none;
    }

    .components-sidebar a:hover {
      color: #FFFFFF;
      background: rgba(55, 180, 206, 0.12);
      transform: translateX(3px);
    }

    [data-theme="clean"] .components-sidebar a:hover {
      color: var(--jd-azul);
      background: #F1F5F9;
    }

    .components-sidebar a.is-active {
      color: #FFFFFF;
      background: linear-gradient(90deg, rgba(65, 129, 188, 0.35) 0%, rgba(55, 180, 206, 0.15) 100%);
      border-left: 3px solid var(--jd-ciano-logo-para);
      font-weight: 700;
    }

    .components-sidebar a .ds-num {
      font-family: 'JetBrains Mono', monospace;
      font-size: 10px;
      color: var(--jd-ciano);
      opacity: 0.8;
      min-width: 22px;
    }

    .components-content {
      padding: 48px clamp(20px, 4vw, 64px) 140px;
      background:
        linear-gradient(to right, rgba(55, 180, 206, 0.04) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(55, 180, 206, 0.04) 1px, transparent 1px);
      background-size: 40px 40px;
    }

    [data-theme="clean"] .components-content {
      background: #F8FAFC;
    }

    .ds-section {
      padding-bottom: 96px;
      margin-bottom: 64px;
      border-bottom: 1px solid var(--ds-border);
      position: relative;
    }

    .ds-section:last-child {
      border-bottom: none;
    }

    .ds-section__head {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      gap: 20px;
      margin-bottom: 32px;
      padding-bottom: 16px;
      border-bottom: 2px solid rgba(55, 180, 206, 0.3);
      position: relative;
    }

    .ds-section__head::after {
      content: '';
      position: absolute;
      bottom: -2px;
      left: 0;
      width: 80px;
      height: 2px;
      background: var(--jd-grad-logo);
      box-shadow: 0 0 12px var(--jd-ciano);
    }

    .ds-section__title {
      font-family: var(--jd-font-display);
      font-weight: var(--jd-fw-black);
      font-size: clamp(24px, 3.5vw, 38px);
      text-transform: uppercase;
      letter-spacing: -0.02em;
      line-height: 1.1;
      color: #FFFFFF;
      display: flex;
      align-items: center;
      gap: 12px;
      margin: 0;
    }

    [data-theme="clean"] .ds-section__title {
      color: #0F172A;
    }

    .ds-section__badge {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 700;
      padding: 4px 10px;
      background: rgba(55, 180, 206, 0.15);
      border: 1px solid rgba(0, 224, 240, 0.4);
      color: var(--jd-ciano);
      border-radius: 4px;
      letter-spacing: 0.08em;
      display: inline-block;
      margin-bottom: 8px;
    }

    .ds-desc {
      font-size: 14.5px;
      line-height: 1.7;
      color: var(--ds-muted);
      max-width: 78ch;
      margin-bottom: 28px;
    }

    .ds-specimen {
      background: var(--ds-panel);
      border: 1px solid var(--ds-border);
      border-radius: 10px;
      padding: 28px;
      margin-bottom: 32px;
      position: relative;
      overflow: hidden;
      box-shadow: var(--jd-sombra-3d);
    }

    .ds-specimen__header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      padding-bottom: 12px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }

    .ds-specimen__title {
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--jd-ciano);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .ds-copy-btn {
      padding: 4px 10px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 10.5px;
      font-weight: 700;
      background: rgba(0, 224, 240, 0.1);
      color: var(--jd-ciano);
      border: 1px solid rgba(0, 224, 240, 0.3);
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .ds-copy-btn:hover {
      background: var(--jd-ciano);
      color: #000000;
      box-shadow: 0 0 10px var(--jd-ciano);
    }

    /* Swatches Grid */
    .ds-colors-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 16px;
    }

    /* Overview Page Hero */
    .overview-hero {
      position: relative;
      padding: 72px clamp(20px, 5vw, 80px) 64px;
      background: radial-gradient(circle at 70% 30%, #1A284A 0%, #0D0C17 80%);
      border-bottom: 1px solid var(--ds-border);
      overflow: hidden;
    }

    .overview-hero::before {
      content: '';
      position: absolute;
      inset: 0;
      background-image:
        linear-gradient(rgba(55, 180, 206, 0.08) 1px, transparent 1px),
        linear-gradient(90deg, rgba(55, 180, 206, 0.08) 1px, transparent 1px);
      background-size: 48px 48px;
      pointer-events: none;
    }

    /* Toast Flutuante */
    .ds-copy-toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #09080F;
      border: 1px solid #00E0F0;
      color: #FFFFFF;
      padding: 10px 18px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.05em;
      z-index: 9999;
      box-shadow: 0 10px 30px rgba(0,0,0,0.6);
      opacity: 0;
      transform: translateY(10px);
      transition: all 0.25s ease;
      pointer-events: none;
      display: flex;
      align-items: center;
      gap: 8px;
    }
  </style>
</head>

<body class="fx" data-theme="dark">

  <!-- ====================================================================
       HEADER PRINCIPAL DO CATÁLOGO (AURA / IX-7 STYLE)
       ==================================================================== -->
  <header class="catalog-header" aria-label="Controles do Design System">
    <div class="catalog-brand">
      <img src="{PATH_PREFIX}assets/logo-jd.png" alt="JD Câmaras Frias" onerror="this.outerHTML='<span style=\'font-family:Archivo;font-weight:900;font-size:18px;color:#00E0F0;\'>JD CÂMARAS</span>'">
      <div class="catalog-tag">
        <span class="jd-radar-ping" style="color:var(--jd-verde);font-size:14px;">●</span>
        <span>SUPERVISÓRIO DE ENGENHARIA</span>
      </div>
    </div>

    <!-- Navegação de Abas: VISÃO GERAL vs COMPONENTES -->
    <nav class="catalog-nav" aria-label="Modo de Visualização">
      <button class="catalog-nav-btn is-active" id="tab-btn-overview" data-view-target="view-overview">
        <span>🌐</span> <span>VISÃO GERAL</span>
      </button>
      <button class="catalog-nav-btn" id="tab-btn-components" data-view-target="view-components">
        <span>🧩</span> <span>CATÁLOGO DE COMPONENTES</span>
      </button>
    </nav>

    <!-- Controles HUD -->
    <div class="catalog-controls">
      <!-- Termostato Digital LED Danfoss -->
      <div class="jd-thermostat-hud" title="Simulador Digital do Termostato Danfoss">
        <div>
          <span style="font-size:8px;color:#9CADC2;display:block;margin-bottom:1px;">NÚCLEO:</span>
          <div class="jd-led-digits">
            <span class="jd-live-temp">-18,0</span><span class="jd-led-unit">°C</span>
          </div>
        </div>
        <div style="border-left:1px solid rgba(255,255,255,0.1);padding-left:10px;">
          <div class="jd-led-status-dot" style="margin-bottom:2px;"></div>
          <span class="jd-live-temp-status" style="font-size:8px;color:#00E676;font-weight:700;display:block;">COMPRESSOR OK</span>
        </div>
      </div>

      <!-- Presets Rápidos de Temperatura -->
      <button class="catalog-tool-btn is-active" data-temp-mode data-temp-target="-18.0" data-temp-label="CONGELADOS [-18°C] // PIR 100mm">
        <span>❄</span> -18°C
      </button>
      <button class="catalog-tool-btn" data-temp-mode data-temp-target="2.5" data-temp-label="RESFRIADOS [+2.5°C] // PIR 70mm">
        <span>🌡</span> +2°C
      </button>
      <button class="catalog-tool-btn" data-temp-mode data-temp-target="14.0" data-temp-label="CLIMATIZADOS [+14°C] // PIR 50mm">
        <span>🍃</span> +15°C
      </button>

      <!-- Toggle Áudio SFX -->
      <button id="jd-sfx-toggle" class="catalog-tool-btn" title="Ativar sons mecânicos táteis de clique">
        <span>🔊</span> <span class="jd-sfx-label">SFX: MUDO</span>
      </button>

      <!-- Alternador de Tema -->
      <button id="jd-theme-toggle" class="catalog-tool-btn" title="Alternar entre modo fábrica e sala limpa">
        <span>🌗</span> <span class="jd-theme-label">FÁBRICA</span>
      </button>
    </div>
  </header>


  <!-- ====================================================================
       VIEW 1: VISÃO GERAL (OVERVIEW) — EXPERIÊNCIA VIVA & DIFERENCIADA
       ==================================================================== -->
  <main id="view-overview" class="catalog-view is-active">

    <!-- Hero Criogênico com Canvas de Névoa -->
    <section class="overview-hero">
      <canvas id="jd-frost-canvas"></canvas>
      <div style="position:relative;z-index:2;max-width:980px;margin:0 auto;text-align:center;">
        <span class="ds-section__badge">PATENTE INDUSTRIAL MG &amp; GO // 15 ANOS DE MERCADO</span>
        <h1 style="font-family:var(--jd-font-display);font-size:clamp(36px, 5.5vw, 64px);font-weight:900;text-transform:uppercase;line-height:1.02;color:#FFFFFF;margin:16px 0 20px;letter-spacing:-0.03em;">
          ENGENHARIA DO FRIO <span style="background:var(--jd-grad-logo);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">INDUSTRIAL</span>
        </h1>
        <p style="font-size:17px;line-height:1.65;color:var(--jd-cinza-aco);max-width:760px;margin:0 auto 36px;">
          Sistema de Design proprietário da <strong>JD Câmaras Frias</strong> (fábricas em Ubá-MG e Anápolis-GO). Precisão termodinâmica classe II-A, estanqueidade hermética a -18°C e motor de conversão acelerada para Google Ads.
        </p>

        <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;margin-bottom:48px;">
          <a href="#sec-overview-3d" class="jd-btn jd-btn--primary">
            <span>EXPLORAR RAIO-X 3D DA CÂMARA</span>
            <span class="jd-btn__icon">→</span>
          </a>
          <button class="jd-btn jd-btn--dark" onclick="document.getElementById('tab-btn-components').click()">
            <span>VER CATÁLOGO COMPLETO DE COMPONENTES</span>
          </button>
        </div>

        <!-- Telemetria Fabril KPI -->
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(210px, 1fr));gap:16px;">
          <div class="jd-spotlight" style="padding:20px;text-align:left;">
            <div style="font-family:var(--jd-font-display);font-size:36px;font-weight:900;color:var(--jd-ciano);line-height:1;">
              <span data-counter="2500" data-counter-duration="1200">2.500</span>+
            </div>
            <span style="font-size:12px;font-weight:600;color:var(--jd-cinza-aco);text-transform:uppercase;margin-top:6px;display:block;">Câmaras Entregues e Montadas</span>
          </div>

          <div class="jd-spotlight" style="padding:20px;text-align:left;">
            <div style="font-family:var(--jd-font-display);font-size:36px;font-weight:900;color:var(--jd-ciano);line-height:1;">
              <span data-counter="15" data-counter-duration="900">15</span> Dias
            </div>
            <span style="font-size:12px;font-weight:600;color:var(--jd-cinza-aco);text-transform:uppercase;margin-top:6px;display:block;">Prazo Ágil de Entrega em Obra</span>
          </div>

          <div class="jd-spotlight" style="padding:20px;text-align:left;">
            <div style="font-family:var(--jd-font-display);font-size:36px;font-weight:900;color:var(--jd-ciano);line-height:1;">
              0,022
            </div>
            <span style="font-size:12px;font-weight:600;color:var(--jd-cinza-aco);text-transform:uppercase;margin-top:6px;display:block;">W/m.K Condutividade PIR Classe II-A</span>
          </div>

          <div class="jd-spotlight" style="padding:20px;text-align:left;">
            <div style="font-family:var(--jd-font-display);font-size:36px;font-weight:900;color:var(--jd-amarelo);line-height:1;">
              -18°C
            </div>
            <span style="font-size:12px;font-weight:600;color:var(--jd-cinza-aco);text-transform:uppercase;margin-top:6px;display:block;">Estanqueidade Hermética Testada</span>
          </div>
        </div>
      </div>
    </section>


    <!-- Seção 1: Raio-X 3D Isométrico Interativo -->
    <section id="sec-overview-3d" style="padding:72px clamp(20px, 4vw, 80px);max-width:1200px;margin:0 auto;">
      <div style="text-align:center;margin-bottom:36px;">
        <span class="ds-section__badge">SUPERVISÓRIO TÉCNICO INTERATIVO</span>
        <h2 style="font-family:var(--jd-font-display);font-size:clamp(28px, 4vw, 44px);font-weight:900;text-transform:uppercase;color:#FFF;margin:8px 0;">
          Raio-X Isométrico em Corte Técnico
        </h2>
        <p style="color:var(--jd-cinza-aco);font-size:15px;max-width:68ch;margin:0 auto;">
          Clique nas abas abaixo para radiografar os subsistemas de engenharia da câmara fria: painéis isotérmicos PIR com encaixe macho-fêmea, unidade evaporadora com hélices ativas e portas semi-embutidas.
        </p>
      </div>

      <div class="jd-iso-container jd-cantoneira">
        <div class="jd-iso-toolbar">
          <div class="jd-iso-tabs">
            <button class="jd-iso-tab-btn is-active" data-iso-layer="all">1. Vista Geral Completa</button>
            <button class="jd-iso-tab-btn" data-iso-layer="pir">2. Painéis PIR 100mm (Corte)</button>
            <button class="jd-iso-tab-btn" data-iso-layer="refrig">3. Evaporador &amp; Ventiladores</button>
            <button class="jd-iso-tab-btn" data-iso-layer="doors">4. Porta Hermética &amp; Batente</button>
          </div>
          <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--jd-ciano);">
            ESCALA 1:25 // PROJETO TÉCNICO MODULAR
          </div>
        </div>

        <div class="jd-iso-canvas-area">
          <svg viewBox="0 0 800 480" width="100%" height="380" style="max-width:760px;overflow:visible;">
            <defs>
              <linearGradient id="iso-wall-grad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#2D3863" stop-opacity="0.9" />
                <stop offset="100%" stop-color="#12111F" stop-opacity="0.95" />
              </linearGradient>
              <linearGradient id="iso-pir-core" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#F1BD43" stop-opacity="0.95" />
                <stop offset="100%" stop-color="#E5AE2E" stop-opacity="0.75" />
              </linearGradient>
              <linearGradient id="iso-cold-air" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#00E0F0" stop-opacity="0.4" />
                <stop offset="100%" stop-color="#37B4CE" stop-opacity="0.05" />
              </linearGradient>
            </defs>

            <!-- Piso Isométrico -->
            <polygon points="400,380 680,260 400,160 120,260" fill="#171A29" stroke="rgba(55, 180, 206, 0.4)" stroke-width="1.5" />
            <line x1="260" y1="310" x2="540" y2="210" stroke="rgba(0, 224, 240, 0.15)" stroke-width="1" stroke-dasharray="4 4" />
            <line x1="330" y1="340" x2="610" y2="240" stroke="rgba(0, 224, 240, 0.15)" stroke-width="1" stroke-dasharray="4 4" />

            <!-- Parede Traseira Direita -->
            <polygon points="400,160 680,260 680,120 400,20" fill="url(#iso-wall-grad)" stroke="rgba(55, 180, 206, 0.3)" />

            <!-- Parede Traseira Esquerda -->
            <polygon points="120,260 400,160 400,20 120,120" fill="#1C2442" stroke="rgba(55, 180, 206, 0.3)" />

            <!-- CAMADA 2: PAINÉIS PIR (Corte com Núcleo Amarelo Retardante) -->
            <g data-iso-target="pir" style="transition:all 0.4s ease;">
              <polygon points="400,20 680,120 660,112 400,16" fill="url(#iso-pir-core)" stroke="#F1BD43" stroke-width="1.5" />
              <polygon points="120,120 400,20 400,16 135,114" fill="url(#iso-pir-core)" stroke="#F1BD43" stroke-width="1.5" />
              <text x="360" y="8" fill="#F1BD43" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700">NÚCLEO PIR 100mm (CLASSE II-A RETARDANTE)</text>
            </g>

            <!-- CAMADA 3: UNIDADE EVAPORADORA COM HÉLICES GIRATÓRIAS -->
            <g data-iso-target="refrig" style="transition:all 0.4s ease;">
              <polygon points="320,120 480,80 480,130 320,170" fill="#2A3554" stroke="#00E0F0" stroke-width="1.5" />
              <!-- Ventilador Axial 1 -->
              <g transform="translate(365, 142)">
                <circle cx="0" cy="0" r="16" fill="#12111F" stroke="#00E0F0" stroke-width="1" />
                <g class="jd-fan-blade">
                  <line x1="-12" y1="0" x2="12" y2="0" stroke="#00E0F0" stroke-width="3" stroke-linecap="round" />
                  <line x1="0" y1="-12" x2="0" y2="12" stroke="#00E0F0" stroke-width="3" stroke-linecap="round" />
                </g>
              </g>
              <!-- Ventilador Axial 2 -->
              <g transform="translate(435, 122)">
                <circle cx="0" cy="0" r="16" fill="#12111F" stroke="#00E0F0" stroke-width="1" />
                <g class="jd-fan-blade">
                  <line x1="-12" y1="0" x2="12" y2="0" stroke="#00E0F0" stroke-width="3" stroke-linecap="round" />
                  <line x1="0" y1="-12" x2="0" y2="12" stroke="#00E0F0" stroke-width="3" stroke-linecap="round" />
                </g>
              </g>
              <!-- Fluxo de Ar Frio Descendente -->
              <polygon points="320,170 480,130 520,290 280,340" fill="url(#iso-cold-air)" />
              <text x="495" y="95" fill="#00E0F0" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700">EVAPORADOR INDUSTRIAL DUAL-FAN</text>
            </g>

            <!-- CAMADA 4: PORTA FRIGORÍFICA GIRATÓRIA & CORTINA POLAR -->
            <g data-iso-target="doors" style="transition:all 0.4s ease;">
              <polygon points="170,242 250,213 250,135 170,165" fill="#1E2845" stroke="#37B4CE" stroke-width="2" />
              <polygon points="170,242 135,280 135,200 170,165" fill="#4181BC" stroke="#00E0F0" stroke-width="1.5" />
              <circle cx="145" cy="240" r="3" fill="#F1BD43" />
              <line x1="145" y1="240" x2="155" y2="238" stroke="#F1BD43" stroke-width="2" />
              <!-- Cortina de PVC Polar -->
              <polygon points="180,238 240,216 240,150 180,172" fill="rgba(0, 224, 240, 0.25)" stroke="rgba(0, 224, 240, 0.5)" stroke-dasharray="3 3" />
              <text x="65" y="295" fill="#00E0F0" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700">PORTA SEMI-EMBUTIDA + RESISTÊNCIA BATENTE</text>
            </g>

            <!-- Linhas de Cota CAD Isométricas -->
            <g>
              <line x1="100" y1="270" x2="380" y2="390" stroke="#00E0F0" stroke-width="1.2" />
              <line x1="95" y1="262" x2="105" y2="278" stroke="#00E0F0" stroke-width="1.5" />
              <line x1="375" y1="382" x2="385" y2="398" stroke="#00E0F0" stroke-width="1.5" />
              <text x="200" y="350" fill="#00E0F0" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700">LARGURA: 3.000 mm</text>

              <line x1="420" y1="390" x2="700" y2="270" stroke="#00E0F0" stroke-width="1.2" />
              <line x1="415" y1="382" x2="425" y2="398" stroke="#00E0F0" stroke-width="1.5" />
              <line x1="695" y1="262" x2="705" y2="278" stroke="#00E0F0" stroke-width="1.5" />
              <text x="550" y="350" fill="#00E0F0" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700">COMPRIMENTO: 4.500 mm</text>

              <line x1="705" y1="260" x2="705" y2="120" stroke="#00E0F0" stroke-width="1.2" />
              <line x1="697" y1="260" x2="713" y2="260" stroke="#00E0F0" stroke-width="1.5" />
              <line x1="697" y1="120" x2="713" y2="120" stroke="#00E0F0" stroke-width="1.5" />
              <text x="715" y="195" fill="#00E0F0" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700">ALTURA: 2.800 mm</text>
            </g>
          </svg>
        </div>

        <div style="padding:16px 24px;background:rgba(9,8,15,0.92);border-top:1px solid rgba(255,255,255,0.08);display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
          <div>
            <strong id="iso-info-title" style="color:#00E0F0;font-size:14px;display:block;">Câmara Fria Modular Completa</strong>
            <span id="iso-info-desc" style="color:var(--jd-cinza-aco);font-size:12.5px;">Projeto 100% sob medida com estanqueidade total, piso reforçado e entrega em 7 a 15 dias.</span>
          </div>
          <button class="jd-btn jd-btn--primary" style="font-size:12px;padding:8px 18px;" onclick="document.getElementById('tab-btn-components').click();location.hash='#sec-formulario';">
            <span>ORÇAR ESTE PROJETO</span>
          </button>
        </div>
      </div>
    </section>


    <!-- Seção 2: Simulador de Carga Térmica & Dimensionamento -->
    <section style="padding:72px clamp(20px, 4vw, 80px);background:rgba(18, 17, 31, 0.4);border-top:1px solid var(--ds-border);border-bottom:1px solid var(--ds-border);">
      <div style="max-width:1200px;margin:0 auto;">
        <div style="text-align:center;margin-bottom:36px;">
          <span class="ds-section__badge">SIMULADOR TERMODINÂMICO EM TEMPO REAL</span>
          <h2 style="font-family:var(--jd-font-display);font-size:clamp(28px, 4vw, 44px);font-weight:900;text-transform:uppercase;color:#FFF;margin:8px 0;">
            Dimensionamento e Carga Frigorífica
          </h2>
          <p style="color:var(--jd-cinza-aco);font-size:15px;max-width:68ch;margin:0 auto;">
            Arraste os sliders de dimensões para calcular instantaneamente o volume cúbico (m³), área de painéis isotérmicos, potência estimada (BTU/h e HP) e capacidade de estocagem.
          </p>
        </div>

        <div class="jd-spotlight jd-cantoneira" style="padding:36px;">
          <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:36px;align-items:start;">

            <!-- Sliders Inputs -->
            <div style="display:flex;flex-direction:column;gap:24px;">
              <div>
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                  <label for="calc-largura" style="font-size:13px;font-weight:700;color:#FFFFFF;text-transform:uppercase;">Largura (Fachada):</label>
                  <span id="calc-val-largura" style="font-family:'JetBrains Mono',monospace;font-size:14px;color:var(--jd-ciano);font-weight:700;">3.0 m</span>
                </div>
                <input type="range" id="calc-largura" min="2.0" max="10.0" step="0.5" value="3.0" style="width:100%;accent-color:var(--jd-ciano);cursor:pointer;">
              </div>

              <div>
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                  <label for="calc-comprimento" style="font-size:13px;font-weight:700;color:#FFFFFF;text-transform:uppercase;">Comprimento (Profundidade):</label>
                  <span id="calc-val-comprimento" style="font-family:'JetBrains Mono',monospace;font-size:14px;color:var(--jd-ciano);font-weight:700;">4.0 m</span>
                </div>
                <input type="range" id="calc-comprimento" min="2.0" max="15.0" step="0.5" value="4.0" style="width:100%;accent-color:var(--jd-ciano);cursor:pointer;">
              </div>

              <div>
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                  <label for="calc-altura" style="font-size:13px;font-weight:700;color:#FFFFFF;text-transform:uppercase;">Altura Pé-Direito:</label>
                  <span id="calc-val-altura" style="font-family:'JetBrains Mono',monospace;font-size:14px;color:var(--jd-ciano);font-weight:700;">2.8 m</span>
                </div>
                <input type="range" id="calc-altura" min="2.2" max="5.0" step="0.2" value="2.8" style="width:100%;accent-color:var(--jd-ciano);cursor:pointer;">
              </div>

              <div>
                <label for="calc-aplicacao" style="font-size:13px;font-weight:700;color:#FFFFFF;text-transform:uppercase;display:block;margin-bottom:8px;">Aplicação e Faixa Térmica:</label>
                <select id="calc-aplicacao" style="width:100%;padding:11px 14px;background:#09080F;border:1px solid rgba(55,180,206,0.3);color:#FFFFFF;border-radius:6px;font-weight:600;font-family:'Inter',sans-serif;cursor:pointer;">
                  <option value="congelados">Congelados (-18°C) — Carnes, Aves, Gelo e Sorvete</option>
                  <option value="resfriados">Resfriados (0°C a +4°C) — Cerveja, Chopp, Laticínios</option>
                  <option value="climatizados">Climatizados (+15°C) — Hortifrúti, Vacinas, Remédios</option>
                </select>
              </div>
            </div>

            <!-- Display de Resultados -->
            <div style="background:rgba(9,8,15,0.9);border:1px solid rgba(0,224,240,0.35);border-radius:10px;padding:26px;box-shadow:inset 0 0 30px rgba(0,0,0,0.7);">
              <div style="font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:700;letter-spacing:0.12em;color:var(--jd-ciano);text-transform:uppercase;margin-bottom:20px;display:flex;align-items:center;gap:8px;">
                <span style="color:#00E676;">●</span> BALANÇO TÉRMICO EM TEMPO REAL
              </div>

              <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:20px;">
                <div>
                  <span style="font-size:11px;color:var(--jd-cinza-aco);display:block;text-transform:uppercase;">Volume Interno:</span>
                  <div id="calc-out-volume" style="font-family:'JetBrains Mono',monospace;font-size:26px;font-weight:800;color:#FFFFFF;">33.6 m³</div>
                </div>
                <div>
                  <span style="font-size:11px;color:var(--jd-cinza-aco);display:block;text-transform:uppercase;">Área dos Painéis:</span>
                  <div id="calc-out-painel" style="font-family:'JetBrains Mono',monospace;font-size:26px;font-weight:800;color:#FFFFFF;">63 m²</div>
                </div>
              </div>

              <div style="border-top:1px solid rgba(255,255,255,0.08);padding-top:14px;margin-bottom:14px;">
                <span style="font-size:11px;color:var(--jd-cinza-aco);display:block;text-transform:uppercase;">Potência Frigorífica Recomendada:</span>
                <div id="calc-out-btu" style="font-family:'JetBrains Mono',monospace;font-size:18px;font-weight:700;color:var(--jd-amarelo);margin-top:2px;">32.000 BTU/h (2.7 HP)</div>
              </div>

              <div style="border-top:1px solid rgba(255,255,255,0.08);padding-top:14px;margin-bottom:14px;">
                <span style="font-size:11px;color:var(--jd-cinza-aco);display:block;text-transform:uppercase;">Isolamento Obrigatório:</span>
                <div id="calc-out-pir" style="font-family:'JetBrains Mono',monospace;font-size:16px;font-weight:700;color:var(--jd-ciano);margin-top:2px;">PIR 100 mm (Retardante II-A)</div>
              </div>

              <div style="border-top:1px solid rgba(255,255,255,0.08);padding-top:14px;margin-bottom:24px;">
                <span style="font-size:11px;color:var(--jd-cinza-aco);display:block;text-transform:uppercase;">Capacidade de Estocagem:</span>
                <div id="calc-out-capacidade" style="font-size:13.5px;font-weight:600;color:#FFFFFF;margin-top:2px;">~5.300 kg carnes/congelados</div>
              </div>

              <button class="jd-btn jd-btn--primary" style="width:100%;text-align:center;" onclick="document.getElementById('tab-btn-components').click();location.hash='#sec-formulario';">
                <span>SOLICITAR ORÇAMENTO COM ESSAS MEDIDAS</span>
              </button>
            </div>

          </div>
        </div>
      </div>
    </section>


    <!-- Seção 3: Comparativo Térmico PIR vs EPS (Isopor) -->
    <section style="padding:72px clamp(20px, 4vw, 80px);max-width:1200px;margin:0 auto;">
      <div style="text-align:center;margin-bottom:36px;">
        <span class="ds-section__badge">EFICIÊNCIA TERMODINÂMICA</span>
        <h2 style="font-family:var(--jd-font-display);font-size:clamp(28px, 4vw, 44px);font-weight:900;text-transform:uppercase;color:#FFF;margin:8px 0;">
          PIR 100mm vs Isopor Comum (EPS)
        </h2>
        <p style="color:var(--jd-cinza-aco);font-size:15px;max-width:68ch;margin:0 auto;">
          Entenda por que a JD Câmaras Frias padroniza 100% de sua produção com <strong>PIR Classe II-A</strong>, gerando economia real de até 35% na fatura de energia e segurança contra incêndios.
        </p>
      </div>

      <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(320px, 1fr));gap:24px;">
        <!-- Card PIR JD -->
        <div class="jd-spotlight jd-cantoneira" style="padding:32px;border-color:rgba(0,224,240,0.5);">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
            <span class="jd-tag" style="background:rgba(0,224,240,0.2);color:#00E0F0;">PADRÃO JD CÂMARAS</span>
            <span style="font-family:'JetBrains Mono';font-size:12px;color:#00E676;font-weight:700;">35% MAIS ECONÔMICO</span>
          </div>
          <h3 style="font-family:var(--jd-font-display);font-size:22px;font-weight:800;color:#FFF;text-transform:uppercase;margin-bottom:12px;">
            PIR Poliisocianurato (Classe II-A)
          </h3>
          <ul style="list-style:none;padding:0;margin:0 0 24px;display:flex;flex-direction:column;gap:12px;font-size:13.5px;color:var(--jd-cinza-aco);">
            <li style="display:flex;align-items:center;gap:10px;"><span style="color:#00E676;font-weight:800;">✔</span> Condutividade térmica ultra-baixa: 0,022 W/m.K</li>
            <li style="display:flex;align-items:center;gap:10px;"><span style="color:#00E676;font-weight:800;">✔</span> Retardante a chamas comprovado (Instrução Técnica IT-10)</li>
            <li style="display:flex;align-items:center;gap:10px;"><span style="color:#00E676;font-weight:800;">✔</span> O compressor cicla suavemente e descansa nos horários de pico</li>
            <li style="display:flex;align-items:center;gap:10px;"><span style="color:#00E676;font-weight:800;">✔</span> Encaixe macho-fêmea com vedante e selante anti-vazamento</li>
          </ul>
          <div style="padding:14px;background:rgba(0,230,118,0.1);border:1px solid rgba(0,230,118,0.3);border-radius:6px;font-size:12.5px;color:#00E676;font-weight:700;">
            RETORNO DO INVESTIMENTO: Economia de até R$ 1.400/mês na conta de luz.
          </div>
        </div>

        <!-- Card EPS Isopor -->
        <div class="jd-spotlight" style="padding:32px;opacity:0.85;">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
            <span class="jd-tag" style="background:rgba(229,57,53,0.2);color:#E53935;">ISOPOR COMUM (MERCADO)</span>
            <span style="font-family:'JetBrains Mono';font-size:12px;color:#E53935;font-weight:700;">ALTO CONSUMO</span>
          </div>
          <h3 style="font-family:var(--jd-font-display);font-size:22px;font-weight:800;color:#FFF;text-transform:uppercase;margin-bottom:12px;">
            EPS Isopor Convencional
          </h3>
          <ul style="list-style:none;padding:0;margin:0 0 24px;display:flex;flex-direction:column;gap:12px;font-size:13.5px;color:var(--jd-cinza-aco);">
            <li style="display:flex;align-items:center;gap:10px;"><span style="color:#E53935;font-weight:800;">✖</span> Condutividade fraca: 0,040 W/m.K (quase o dobro de perda)</li>
            <li style="display:flex;align-items:center;gap:10px;"><span style="color:#E53935;font-weight:800;">✖</span> Altamente inflamável (propaga fogo rápido e fumaça tóxica)</li>
            <li style="display:flex;align-items:center;gap:10px;"><span style="color:#E53935;font-weight:800;">✖</span> Compressor trabalha sem parar gerando superaquecimento</li>
            <li style="display:flex;align-items:center;gap:10px;"><span style="color:#E53935;font-weight:800;">✖</span> Encaixes sofrem deformação térmica ao longo do tempo</li>
          </ul>
          <div style="padding:14px;background:rgba(229,57,53,0.1);border:1px solid rgba(229,57,53,0.3);border-radius:6px;font-size:12.5px;color:#E53935;font-weight:700;">
            CUSTO OCULTO: Manutenções frequentes e queima prematura do motor.
          </div>
        </div>
      </div>
    </section>

  </main>


  <!-- ====================================================================
       VIEW 2: CATÁLOGO DE COMPONENTES (COMPONENTS) — TODOS OS 22 MÓDULOS
       ==================================================================== -->
  <div id="view-components" class="catalog-view">
    <div class="components-shell">

      <!-- Sidebar Navegável com Categorias -->
      <aside class="components-sidebar" aria-label="Navegação dos Componentes">
        <div class="components-sidebar__group-label">01. FUNDAÇÕES VISUAIS</div>
        <a href="#sec-cores" class="is-active"><span class="ds-num">01</span> <span>Cores &amp; Tokens Frio</span></a>
        <a href="#sec-tipografia"><span class="ds-num">02</span> <span>Tipografia Industrial</span></a>
        <a href="#sec-espacamento"><span class="ds-num">03</span> <span>Espaçamento Modular</span></a>
        <a href="#sec-contraste"><span class="ds-num">04</span> <span>Matriz de Contraste AA</span></a>

        <div class="components-sidebar__group-label">02. AÇÕES &amp; CONVERSÃO</div>
        <a href="#sec-botoes"><span class="ds-num">05</span> <span>Botões com Laser Sweep</span></a>
        <a href="#sec-header"><span class="ds-num">06</span> <span>Header Sticky &amp; Conversão</span></a>
        <a href="#sec-whatsapp-float"><span class="ds-num">18</span> <span>WhatsApp Radar Pulse</span></a>

        <div class="components-sidebar__group-label">03. LANDING PAGES A / B</div>
        <a href="#sec-hero-a"><span class="ds-num">07</span> <span>Hero A — Direta (Velocidade)</span></a>
        <a href="#sec-hero-b"><span class="ds-num">08</span> <span>Hero B — Rica (Linhas Cota)</span></a>

        <div class="components-sidebar__group-label">04. FORMULÁRIOS &amp; LEADS</div>
        <a href="#sec-formulario"><span class="ds-num">09</span> <span>Formulário em 2 Etapas</span></a>
        <a href="#sec-cookies"><span class="ds-num">20</span> <span>LGPD &amp; Consent Mode v2</span></a>

        <div class="components-sidebar__group-label">05. PRODUTOS &amp; ENGENHARIA</div>
        <a href="#sec-cards"><span class="ds-num">10</span> <span>Cards de Produto Spotlight</span></a>
        <a href="#sec-specs"><span class="ds-num">11</span> <span>Ficha Técnica PIR vs EPS</span></a>
        <a href="#sec-provas"><span class="ds-num">12</span> <span>Barra de Prova Social</span></a>
        <a href="#sec-timeline"><span class="ds-num">13</span> <span>Linha do Tempo (7 a 15 Dias)</span></a>

        <div class="components-sidebar__group-label">06. CONFIANÇA &amp; RETENÇÃO</div>
        <a href="#sec-galeria"><span class="ds-num">14</span> <span>Galeria de Obras Reais</span></a>
        <a href="#sec-depoimentos"><span class="ds-num">15</span> <span>Depoimentos Donos de Negócio</span></a>
        <a href="#sec-clientes"><span class="ds-num">16</span> <span>Marcas &amp; Clientes</span></a>
        <a href="#sec-faq"><span class="ds-num">17</span> <span>FAQ Técnico com Accordion</span></a>
        <a href="#sec-rodape"><span class="ds-num">19</span> <span>Rodapé Institucional Fabril</span></a>

        <div class="components-sidebar__group-label">07. PLAYGROUND &amp; EXPORT</div>
        <a href="#sec-playground"><span class="ds-num">21</span> <span>Sandbox Interativo</span></a>
        <a href="#sec-export"><span class="ds-num">22</span> <span>Checklist &amp; Export de Tokens</span></a>
      </aside>

      <!-- Conteúdo Principal dos Componentes -->
      <div class="components-content">

        <!-- 01. CORES & TOKENS -->
        <section id="sec-cores" class="ds-section">
          <div class="ds-section__head">
            <div>
              <span class="ds-section__badge">TOKENS HOMOLOGADOS</span>
              <h2 class="ds-section__title">01. Cores de Marca &amp; Efeitos Criogênicos</h2>
            </div>
            <button class="ds-copy-btn" data-copy="--jd-azul: #4181BC; --jd-marinho: #3B497F; --jd-ciano: #37B4CE; --jd-amarelo: #F1BD43;" data-copy-label="Cores copiadas!">Copiar Hexadecimais</button>
          </div>
          <p class="ds-desc">
            Cores extraídas da identidade oficial JD Câmaras Frias. O <strong>Amarelo #F1BD43</strong> é exclusivo para CTA primário (sempre com texto preto #101010), e o <strong>Ciano #37B4CE / #00E0F0</strong> representa precisão térmica e gelo.
          </p>

          <div class="ds-colors-grid">
            <div class="jd-spotlight" style="padding:16px;">
              <div style="height:72px;background:#4181BC;border-radius:6px;margin-bottom:12px;display:grid;place-items:center;font-weight:800;font-family:'JetBrains Mono';color:#FFF;">#4181BC</div>
              <strong style="display:block;font-size:13px;color:#FFF;">Azul Marca</strong>
              <span style="font-family:'JetBrains Mono';font-size:11px;color:var(--jd-ciano);">--jd-azul</span>
            </div>
            <div class="jd-spotlight" style="padding:16px;">
              <div style="height:72px;background:#3B497F;border-radius:6px;margin-bottom:12px;display:grid;place-items:center;font-weight:800;font-family:'JetBrains Mono';color:#FFF;">#3B497F</div>
              <strong style="display:block;font-size:13px;color:#FFF;">Marinho Industrial</strong>
              <span style="font-family:'JetBrains Mono';font-size:11px;color:var(--jd-ciano);">--jd-marinho</span>
            </div>
            <div class="jd-spotlight" style="padding:16px;">
              <div style="height:72px;background:#37B4CE;border-radius:6px;margin-bottom:12px;display:grid;place-items:center;font-weight:800;font-family:'JetBrains Mono';color:#000;">#37B4CE</div>
              <strong style="display:block;font-size:13px;color:#FFF;">Ciano Térmico</strong>
              <span style="font-family:'JetBrains Mono';font-size:11px;color:var(--jd-ciano);">--jd-ciano</span>
            </div>
            <div class="jd-spotlight" style="padding:16px;">
              <div style="height:72px;background:#F1BD43;border-radius:6px;margin-bottom:12px;display:grid;place-items:center;font-weight:800;font-family:'JetBrains Mono';color:#101010;">#F1BD43</div>
              <strong style="display:block;font-size:13px;color:#FFF;">Amarelo Orçamento</strong>
              <span style="font-family:'JetBrains Mono';font-size:11px;color:var(--jd-amarelo);">--jd-amarelo</span>
            </div>
            <div class="jd-spotlight" style="padding:16px;">
              <div style="height:72px;background:#008749;border-radius:6px;margin-bottom:12px;display:grid;place-items:center;font-weight:800;font-family:'JetBrains Mono';color:#FFF;">#008749</div>
              <strong style="display:block;font-size:13px;color:#FFF;">Verde WhatsApp</strong>
              <span style="font-family:'JetBrains Mono';font-size:11px;color:#00E676;">--jd-verde</span>
            </div>
            <div class="jd-spotlight" style="padding:16px;">
              <div style="height:72px;background:#12111F;border:1px solid rgba(255,255,255,0.15);border-radius:6px;margin-bottom:12px;display:grid;place-items:center;font-weight:800;font-family:'JetBrains Mono';color:#FFF;">#12111F</div>
              <strong style="display:block;font-size:13px;color:#FFF;">Noite Fundo</strong>
              <span style="font-family:'JetBrains Mono';font-size:11px;color:var(--jd-cinza-aco);">--jd-noite</span>
            </div>
          </div>
        </section>

        <!-- 02. TIPOGRAFIA INDUSTRIAL -->
        <section id="sec-tipografia" class="ds-section">
          <div class="ds-section__head">
            <div>
              <span class="ds-section__badge">HIERARQUIA ROBUSTA</span>
              <h2 class="ds-section__title">02. Tipografia Industrial (Archivo + Inter)</h2>
            </div>
            <button class="ds-copy-btn" data-copy="font-family: 'Archivo', sans-serif; font-weight: 800;" data-copy-label="CSS Fonte copiado!">Copiar CSS</button>
          </div>
          <p class="ds-desc">
            A tipografia <strong>Archivo 800/900</strong> confere autoridade pesada de fábrica para donos e gerentes de comércios. <strong>Inter 400/600</strong> garante leitura precisa das especificações técnicas em qualquer tamanho de tela.
          </p>

          <div class="ds-specimen">
            <div style="display:flex;flex-direction:column;gap:20px;">
              <div>
                <span style="font-family:'JetBrains Mono';font-size:10px;color:var(--jd-ciano);">H1 DISPLAY // ARCHIVO 800 // 48PX</span>
                <h1 style="font-family:var(--jd-font-display);font-size:clamp(32px, 4vw, 48px);font-weight:900;text-transform:uppercase;color:#FFF;line-height:1.05;margin:4px 0 0;">
                  CÂMARAS FRIAS SOB MEDIDA COM ENTREGA EM 15 DIAS
                </h1>
              </div>
              <div>
                <span style="font-family:'JetBrains Mono';font-size:10px;color:var(--jd-ciano);">H2 SEÇÃO // ARCHIVO 800 // 28PX</span>
                <h2 style="font-family:var(--jd-font-display);font-size:26px;font-weight:800;text-transform:uppercase;color:var(--jd-ciano);margin:4px 0 0;">
                  ESTANQUEIDADE A -18°C COM NÚCLEO DE PIR 100mm
                </h2>
              </div>
              <div>
                <span style="font-family:'JetBrains Mono';font-size:10px;color:var(--jd-ciano);">CORPO DE TEXTO TÉCNICO // INTER 400 / 600 // 16PX</span>
                <p style="font-size:15.5px;line-height:1.65;color:var(--jd-cinza-aco);margin:4px 0 0;max-width:72ch;">
                  Painéis modulares montados com sistema de encaixe macho-fêmea e isolamento térmico de poliisocianurato (PIR) retardante à chama classe II-A, garantindo até 35% de redução no consumo elétrico.
                </p>
              </div>
            </div>
          </div>
        </section>

        <!-- 03. ESPAÇAMENTO MODULAR -->
        <section id="sec-espacamento" class="ds-section">
          <div class="ds-section__head">
            <div>
              <span class="ds-section__badge">GRADE 8PX</span>
              <h2 class="ds-section__title">03. Espaçamento &amp; Grid Modular</h2>
            </div>
            <button class="ds-copy-btn" data-copy="--jd-space-4: 16px; --jd-space-6: 32px;" data-copy-label="Espaçamento copiado!">Copiar Tokens</button>
          </div>
          <p class="ds-desc">
            Base linear de 8px (4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px, 96px) mantendo harmonia geométrica entre componentes e seções.
          </p>

          <div class="ds-specimen" style="display:flex;flex-direction:column;gap:12px;">
            <div style="display:flex;align-items:center;gap:16px;">
              <span style="font-family:'JetBrains Mono';font-size:11px;min-width:110px;color:var(--jd-ciano);">--jd-space-2 (8px)</span>
              <div style="height:20px;width:8px;background:var(--jd-ciano);border-radius:2px;"></div>
            </div>
            <div style="display:flex;align-items:center;gap:16px;">
              <span style="font-family:'JetBrains Mono';font-size:11px;min-width:110px;color:var(--jd-ciano);">--jd-space-4 (16px)</span>
              <div style="height:20px;width:16px;background:var(--jd-ciano);border-radius:2px;"></div>
            </div>
            <div style="display:flex;align-items:center;gap:16px;">
              <span style="font-family:'JetBrains Mono';font-size:11px;min-width:110px;color:var(--jd-ciano);">--jd-space-6 (32px)</span>
              <div style="height:20px;width:32px;background:var(--jd-ciano);border-radius:2px;"></div>
            </div>
            <div style="display:flex;align-items:center;gap:16px;">
              <span style="font-family:'JetBrains Mono';font-size:11px;min-width:110px;color:var(--jd-ciano);">--jd-space-8 (48px)</span>
              <div style="height:20px;width:48px;background:var(--jd-ciano);border-radius:2px;"></div>
            </div>
          </div>
        </section>

        <!-- 04. MATRIZ DE CONTRASTE WCAG AA -->
        <section id="sec-contraste" class="ds-section">
          <div class="ds-section__head">
            <div>
              <span class="ds-section__badge">ACESSIBILIDADE WCAG 2.1 AA</span>
              <h2 class="ds-section__title">04. Matriz de Contraste e Legibilidade</h2>
            </div>
            <button class="ds-copy-btn" data-copy="WCAG AA Compliant: 11.9:1, 7.8:1, 4.6:1" data-copy-label="Status copiado!">Copiar Status</button>
          </div>
          <p class="ds-desc">
            Todos os pares de cores de texto e fundo foram validados para atender ou superar a taxa de contraste mínima de 4.5:1 exigida para conformidade com normas federais e compras públicas.
          </p>

          <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:16px;">
            <div style="background:#F1BD43;color:#101010;padding:20px;border-radius:6px;">
              <strong style="font-size:14px;display:block;">Amarelo + Preto</strong>
              <span style="font-size:12px;opacity:0.85;">CTA Primário de Orçamento</span>
              <div style="font-family:'JetBrains Mono';font-size:11px;font-weight:700;margin-top:12px;background:rgba(0,0,0,0.1);padding:4px 8px;border-radius:4px;display:inline-block;">11.8:1 (Aprovado AAA)</div>
            </div>

            <div style="background:#008749;color:#FFFFFF;padding:20px;border-radius:6px;">
              <strong style="font-size:14px;display:block;">Verde + Branco</strong>
              <span style="font-size:12px;opacity:0.85;">Botão de WhatsApp Direto</span>
              <div style="font-family:'JetBrains Mono';font-size:11px;font-weight:700;margin-top:12px;background:rgba(0,0,0,0.2);padding:4px 8px;border-radius:4px;display:inline-block;">4.6:1 (Aprovado AA)</div>
            </div>

            <div style="background:#3B497F;color:#FFFFFF;padding:20px;border-radius:6px;">
              <strong style="font-size:14px;display:block;">Marinho + Branco</strong>
              <span style="font-size:12px;opacity:0.85;">Títulos e Cabeçalhos</span>
              <div style="font-family:'JetBrains Mono';font-size:11px;font-weight:700;margin-top:12px;background:rgba(0,0,0,0.2);padding:4px 8px;border-radius:4px;display:inline-block;">7.8:1 (Aprovado AAA)</div>
            </div>

            <div style="background:#12111F;color:#00E0F0;padding:20px;border-radius:6px;border:1px solid rgba(0,224,240,0.3);">
              <strong style="font-size:14px;display:block;">Noite + Ciano</strong>
              <span style="font-size:12px;opacity:0.85;">Telemetria e Destaques</span>
              <div style="font-family:'JetBrains Mono';font-size:11px;font-weight:700;margin-top:12px;background:rgba(0,0,0,0.4);padding:4px 8px;border-radius:4px;display:inline-block;">12.4:1 (Aprovado AAA)</div>
            </div>
          </div>
        </section>

        <!-- 05. BOTÕES COM EFEITO LASER -->
        <section id="sec-botoes" class="ds-section">
          <div class="ds-section__head">
            <div>
              <span class="ds-section__badge">AÇÃO &amp; CONVERSÃO</span>
              <h2 class="ds-section__title">05. Botões com Laser Shimmer &amp; Haptic Click</h2>
            </div>
            <button class="ds-copy-btn" data-copy="<a href='#' class='jd-btn jd-btn--primary'><span>PEDIR ORÇAMENTO</span></a>" data-copy-label="HTML Botão copiado!">Copiar HTML</button>
          </div>
          <p class="ds-desc">
            Botões com micro-interação mecânica tátil ao clique, feixe de luz criogênica deslizante (laser sweep) no botão primário e radar pulsante no botão do WhatsApp.
          </p>

          <div class="ds-specimen">
            <div style="display:flex;gap:16px;flex-wrap:wrap;align-items:center;">
              <button class="jd-btn jd-btn--primary">
                <span>PEDIR ORÇAMENTO RÁPIDO</span>
                <span class="jd-btn__icon">→</span>
              </button>

              <a href="https://wa.me/5532999999999" target="_blank" rel="noopener" class="jd-btn jd-btn--whatsapp">
                <span class="jd-radar-ping" style="color:#FFFFFF;margin-right:6px;">●</span>
                <span>FALAR NO WHATSAPP</span>
              </a>

              <button class="jd-btn jd-btn--secondary">
                <span>VER CATÁLOGO TÉCNICO</span>
              </button>

              <button class="jd-btn jd-btn--dark">
                <span>FICHA TÉCNICA PIR</span>
              </button>
            </div>
          </div>
        </section>

        <!-- 06. HEADER STICKY -->
        <section id="sec-header" class="ds-section">
          <div class="ds-section__head">
            <div>
              <span class="ds-section__badge">TOPO DE CONVERSÃO</span>
              <h2 class="ds-section__title">06. Header Sticky com CTA Imediato</h2>
            </div>
            <button class="ds-copy-btn" data-copy="<header class='jd-header'>...</header>" data-copy-label="Header copiado!">Copiar Header</button>
          </div>
          <p class="ds-desc">
            Cabeçalho translúcido com efeito vidro escuro fosco, número de plantão da fábrica e botão de orçamento em destaque fixo no topo ao rolar a página.
          </p>

          <div class="ds-specimen" style="padding:0;overflow:hidden;">
            <div style="background:rgba(18,17,31,0.95);padding:14px 24px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid rgba(55,180,206,0.3);flex-wrap:wrap;gap:12px;">
              <div style="display:flex;align-items:center;gap:12px;">
                <img src="{PATH_PREFIX}assets/logo-jd.png" alt="JD" style="height:26px;">
                <span style="font-family:'JetBrains Mono';font-size:11px;color:var(--jd-ciano);">FÁBRICA UBÁ-MG &amp; ANÁPOLIS-GO</span>
              </div>
              <div style="display:flex;align-items:center;gap:16px;">
                <span style="font-family:'JetBrains Mono';font-size:12px;color:#FFF;font-weight:700;">(32) 3532-4000</span>
                <button class="jd-btn jd-btn--primary" style="font-size:11px;padding:8px 16px;">
                  <span>PEDIR ORÇAMENTO</span>
                </button>
              </div>
            </div>
          </div>
        </section>

        <!-- 07. HERO A (DIRETA) -->
        <section id="sec-hero-a" class="ds-section">
          <div class="ds-section__head">
            <div>
              <span class="ds-section__badge">TESTE A/B: LP A DIRETA</span>
              <h2 class="ds-section__title">07. Hero A — Captação Imediata na 1ª Dobra</h2>
            </div>
            <button class="ds-copy-btn" data-copy="<section class='jd-hero-a'>...</section>" data-copy-label="Hero A copiado!">Copiar Hero A</button>
          </div>
          <p class="ds-desc">
            Estrutura da Landing Page A: formulário na primeira tela, carregamento instantâneo, foco em tráfego de pesquisa do Google Ads com alta velocidade e zero distrações.
          </p>

          <div class="ds-specimen" style="background:var(--jd-grad-marinho);padding:36px;border-radius:10px;">
            <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:32px;align-items:center;">
              <div>
                <span style="font-family:'JetBrains Mono';font-size:11px;color:var(--jd-ciano);font-weight:700;">DIRETO DA FÁBRICA SEM INTERMEDIÁRIOS</span>
                <h2 style="font-family:var(--jd-font-display);font-size:32px;font-weight:900;text-transform:uppercase;color:#FFF;line-height:1.1;margin:8px 0 16px;">
                  CÂMARAS FRIAS SOB MEDIDA ENTREGUES EM 15 DIAS
                </h2>
                <p style="color:var(--jd-cinza-aco);font-size:14px;line-height:1.6;margin-bottom:20px;">
                  Câmaras modulares de congelados e resfriados sob medida com painéis de PIR 100mm. Atendimento rápido de engenharia com garantia total de fábrica.
                </p>
                <div style="display:flex;gap:12px;flex-wrap:wrap;">
                  <span class="jd-tag" style="background:rgba(255,255,255,0.1);color:#FFF;">✔ 2.500+ Obras</span>
                  <span class="jd-tag" style="background:rgba(255,255,255,0.1);color:#FFF;">✔ Garantia 1 Ano</span>
                  <span class="jd-tag" style="background:rgba(255,255,255,0.1);color:#FFF;">✔ Faturamento Direto</span>
                </div>
              </div>

              <!-- Miniatura do Form Rápido -->
              <div style="background:rgba(9,8,15,0.85);border:1px solid rgba(0,224,240,0.3);padding:24px;border-radius:8px;">
                <h3 style="font-family:var(--jd-font-display);font-size:16px;font-weight:800;color:#FFF;text-transform:uppercase;margin:0 0 12px;">
                  SOLICITAR ORÇAMENTO EXPRESSO
                </h3>
                <div style="display:flex;flex-direction:column;gap:12px;">
                  <input type="text" placeholder="Nome / Empresa" style="padding:10px;background:#171A29;border:1px solid rgba(255,255,255,0.1);color:#FFF;border-radius:4px;font-size:12px;">
                  <input type="tel" placeholder="WhatsApp (DDD)" style="padding:10px;background:#171A29;border:1px solid rgba(255,255,255,0.1);color:#FFF;border-radius:4px;font-size:12px;">
                  <button class="jd-btn jd-btn--primary" style="font-size:12px;padding:10px;">
                    <span>CALCULAR PREÇO DE FÁBRICA</span>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- 08. HERO B (RICA) -->
        <section id="sec-hero-b" class="ds-section">
          <div class="ds-section__head">
            <div>
              <span class="ds-section__badge">TESTE A/B: LP B RICA</span>
              <h2 class="ds-section__title">08. Hero B — Rica &amp; Ilustrativa (Otto-Inspired)</h2>
            </div>
            <button class="ds-copy-btn" data-copy="<section class='jd-hero-b'>...</section>" data-copy-label="Hero B copiado!">Copiar Hero B</button>
          </div>
          <p class="ds-desc">
            Estrutura da Landing Page B: atmosfera cinematográfica com fundo escuro, linhas de cota animadas dinamicamente e indicadores térmicos laterais.
          </p>

          <div class="ds-specimen" style="background:#0D0C17;padding:40px;border-radius:10px;text-align:center;position:relative;overflow:hidden;">
            <div style="position:relative;z-index:2;max-width:680px;margin:0 auto;">
              <span class="jd-kicker" style="color:var(--jd-ciano);font-family:'JetBrains Mono';font-size:11px;font-weight:700;letter-spacing:0.1em;">ENGENHARIA TERMODINÂMICA EXCLUSIVA</span>
              <h2 style="font-family:var(--jd-font-display);font-size:36px;font-weight:900;text-transform:uppercase;color:#FFF;margin:12px 0 16px;">
                A CÂMARA FRIA MAIS EFICIENTE DO MERCADO
              </h2>
              <p style="color:var(--jd-cinza-aco);font-size:14px;line-height:1.6;margin-bottom:24px;">
                Fabricação de alta precisão com núcleos termoisolantes PIR 100mm, corte a laser milimétrico e motocompressores de alta eficiência.
              </p>
              <div style="display:flex;gap:12px;justify-content:center;">
                <button class="jd-btn jd-btn--primary"><span>SOLICITAR CONSULTORIA TÉCNICA</span></button>
                <button class="jd-btn jd-btn--secondary"><span>FALAR COM ENGENHEIRO</span></button>
              </div>
            </div>
          </div>
        </section>

        <!-- 09. FORMULÁRIO EM 2 ETAPAS -->
        <section id="sec-formulario" class="ds-section">
          <div class="ds-section__head">
            <div>
              <span class="ds-section__badge">CAPTAÇÃO AVANÇADA</span>
              <h2 class="ds-section__title">09. Formulário de Conversão em 2 Etapas</h2>
            </div>
            <button class="ds-copy-btn" data-copy="<form class='jd-form'>...</form>" data-copy-label="Formulário copiado!">Copiar Form</button>
          </div>
          <p class="ds-desc">
            Formulário sem atrito: Etapa 1 capta apenas o tipo de câmara e telefone com máscara automática; Etapa 2 coleta dados complementares e salva UTMs automaticamente.
          </p>

          <div style="max-width:540px;margin:0 auto;">
            <form class="jd-form jd-spotlight jd-cantoneira" id="form-lead-demo" style="padding:32px;">
              <div class="jd-form__progress" style="margin-bottom:24px;">
                <div style="display:flex;justify-content:space-between;font-size:11px;font-weight:700;color:var(--jd-ciano);margin-bottom:8px;">
                  <span id="form-step-title">ETAPA 1 DE 2: DADOS BÁSICOS</span>
                  <span id="form-step-percent">50%</span>
                </div>
                <div style="height:4px;background:rgba(255,255,255,0.1);border-radius:2px;overflow:hidden;">
                  <div id="form-progress-bar" style="width:50%;height:100%;background:var(--jd-grad-logo);transition:width 0.3s ease;"></div>
                </div>
              </div>

              <!-- ETAPA 1 -->
              <div class="jd-form-step is-active" id="step-1">
                <div style="margin-bottom:18px;">
                  <label for="lead-tipo" style="display:block;font-size:12px;font-weight:700;color:#FFF;text-transform:uppercase;margin-bottom:6px;">Qual tipo de câmara você precisa?</label>
                  <select id="lead-tipo" required style="width:100%;padding:12px;background:#09080F;border:1px solid rgba(55,180,206,0.3);color:#FFF;border-radius:6px;font-weight:600;">
                    <option value="">Selecione o modelo desejado...</option>
                    <option value="congelados">Câmara de Congelados (-18°C)</option>
                    <option value="resfriados">Câmara de Resfriados (0°C a +15°C)</option>
                    <option value="walk-in">Câmara Expositora Walk-In Cooler</option>
                    <option value="mini">Mini Câmara Fria Comercial</option>
                    <option value="projeto">Projeto Especial Sob Medida</option>
                  </select>
                </div>

                <div style="margin-bottom:24px;">
                  <label for="lead-telefone" style="display:block;font-size:12px;font-weight:700;color:#FFF;text-transform:uppercase;margin-bottom:6px;">Seu WhatsApp (com DDD):</label>
                  <input type="tel" id="lead-telefone" placeholder="(00) 00000-0000" required style="width:100%;padding:12px;background:#09080F;border:1px solid rgba(55,180,206,0.3);color:#FFF;border-radius:6px;font-family:'JetBrains Mono',monospace;">
                </div>

                <button type="button" class="jd-btn jd-btn--primary" id="btn-next-step" style="width:100%;">
                  <span>CONTINUAR PARA ETAPA FINAL</span>
                  <span class="jd-btn__icon">→</span>
                </button>
              </div>

              <!-- ETAPA 2 (Oculta) -->
              <div class="jd-form-step" id="step-2" style="display:none;">
                <div style="margin-bottom:18px;">
                  <label for="lead-nome" style="display:block;font-size:12px;font-weight:700;color:#FFF;text-transform:uppercase;margin-bottom:6px;">Seu Nome ou Razão Social:</label>
                  <input type="text" id="lead-nome" placeholder="Ex: Roberto da Silva" style="width:100%;padding:12px;background:#09080F;border:1px solid rgba(55,180,206,0.3);color:#FFF;border-radius:6px;">
                </div>

                <div style="margin-bottom:24px;">
                  <label for="lead-cidade" style="display:block;font-size:12px;font-weight:700;color:#FFF;text-transform:uppercase;margin-bottom:6px;">Cidade e Estado da Instalação:</label>
                  <input type="text" id="lead-cidade" placeholder="Ex: Belo Horizonte - MG" style="width:100%;padding:12px;background:#09080F;border:1px solid rgba(55,180,206,0.3);color:#FFF;border-radius:6px;">
                </div>

                <div style="display:flex;gap:12px;">
                  <button type="button" class="jd-btn jd-btn--dark" id="btn-prev-step" style="flex:1;">
                    <span>VOLTAR</span>
                  </button>
                  <button type="submit" class="jd-btn jd-btn--primary" style="flex:2;">
                    <span>RECEBER ORÇAMENTO RÁPIDO</span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </section>

        <!-- 10. CARDS DE PRODUTO COM SPOTLIGHT -->
        <section id="sec-cards" class="ds-section">
          <div class="ds-section__head">
            <div>
              <span class="ds-section__badge">SPOTLIGHT REFLEX</span>
              <h2 class="ds-section__title">10. Cards de Produto com Luz Dinâmica</h2>
            </div>
            <button class="ds-copy-btn" data-copy="<div class='jd-card-produto jd-spotlight'>...</div>" data-copy-label="Cards copiados!">Copiar Cards</button>
          </div>
          <p class="ds-desc">
            Passe o mouse sobre os cards para ver o <strong>Spotlight Effect</strong> (o reflexo de luz gelada que acompanha o mouse em tempo real).
          </p>

          <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(260px, 1fr));gap:24px;">
            <!-- Mini Câmara -->
            <div class="jd-card-produto jd-spotlight jd-cantoneira" style="padding:24px;">
              <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;">
                <span class="jd-tag" style="background:rgba(65,129,188,0.2);color:var(--jd-ciano);">PLUG-IN 220V</span>
                <span style="font-family:'JetBrains Mono';font-size:11px;color:var(--jd-cinza-aco);">MOD: JD-MINI</span>
              </div>
              <h3 style="font-family:var(--jd-font-display);font-size:20px;font-weight:800;color:#FFF;text-transform:uppercase;margin-bottom:8px;">
                Mini Câmara Fria
              </h3>
              <p style="font-size:13px;color:var(--jd-cinza-aco);line-height:1.5;margin-bottom:18px;">
                Ideal para açougues, padarias e pequenos distribuidores. Sem obras civis pesadas.
              </p>
              <div style="padding:12px;background:rgba(0,0,0,0.4);border-radius:6px;border:1px solid rgba(255,255,255,0.06);margin-bottom:20px;">
                <span style="font-size:11px;color:var(--jd-ciano);font-weight:700;display:block;">FAIXA: 0°C a +10°C</span>
                <span style="font-size:11px;color:var(--jd-cinza-aco);">Volume: 3 a 12 m³ // PIR 70mm</span>
              </div>
              <button class="jd-btn jd-btn--primary" style="width:100%;font-size:12px;padding:10px 16px;">
                <span>ORÇAR MINI CÂMARA</span>
              </button>
            </div>

            <!-- Walk-In Cooler -->
            <div class="jd-card-produto jd-spotlight jd-cantoneira" style="padding:24px;">
              <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;">
                <span class="jd-tag" style="background:rgba(0,224,240,0.2);color:#00E0F0;">PORTAS DE VIDRO</span>
                <span style="font-family:'JetBrains Mono';font-size:11px;color:var(--jd-cinza-aco);">MOD: JD-WALK</span>
              </div>
              <h3 style="font-family:var(--jd-font-display);font-size:20px;font-weight:800;color:#FFF;text-transform:uppercase;margin-bottom:8px;">
                Câmara Expositora Walk-In
              </h3>
              <p style="font-size:13px;color:var(--jd-cinza-aco);line-height:1.5;margin-bottom:18px;">
                Abastecimento traseiro e exposição frontal de cervejas no ponto extra gelado.
              </p>
              <div style="padding:12px;background:rgba(0,0,0,0.4);border-radius:6px;border:1px solid rgba(255,255,255,0.06);margin-bottom:20px;">
                <span style="font-size:11px;color:#00E0F0;font-weight:700;display:block;">BEBIDAS NO PONTO EXTRA FRIO</span>
                <span style="font-size:11px;color:var(--jd-cinza-aco);">Vidro Triplo Anti-embaçante</span>
              </div>
              <button class="jd-btn jd-btn--primary" style="width:100%;font-size:12px;padding:10px 16px;">
                <span>ORÇAR EXPOSITORA</span>
              </button>
            </div>

            <!-- Congelados -18°C -->
            <div class="jd-card-produto jd-spotlight jd-cantoneira" style="padding:24px;border-color:rgba(0,224,240,0.4);">
              <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;">
                <span class="jd-tag" style="background:rgba(241,189,67,0.2);color:var(--jd-amarelo);">ALTA PERFORMANCE</span>
                <span style="font-family:'JetBrains Mono';font-size:11px;color:var(--jd-cinza-aco);">MOD: JD-CONG</span>
              </div>
              <h3 style="font-family:var(--jd-font-display);font-size:20px;font-weight:800;color:#FFF;text-transform:uppercase;margin-bottom:8px;">
                Câmara de Congelados -18°C
              </h3>
              <p style="font-size:13px;color:var(--jd-cinza-aco);line-height:1.5;margin-bottom:18px;">
                Estrutura maciça para carnes, pescados, gelo e sorvetes com isolamento PIR 100mm.
              </p>
              <div style="padding:12px;background:rgba(0,0,0,0.4);border-radius:6px;border:1px solid rgba(255,255,255,0.06);margin-bottom:20px;">
                <span style="font-size:11px;color:var(--jd-amarelo);font-weight:700;display:block;">ESTANQUEIDADE TOTAL -18°C</span>
                <span style="font-size:11px;color:var(--jd-cinza-aco);">Piso Reforçado c/ Aquecimento</span>
              </div>
              <button class="jd-btn jd-btn--primary" style="width:100%;font-size:12px;padding:10px 16px;">
                <span>ORÇAR CONGELADOS</span>
              </button>
            </div>
          </div>
        </section>

        <!-- 11. FICHA TÉCNICA COMPARATIVA -->
        <section id="sec-specs" class="ds-section">
          <div class="ds-section__head">
            <div>
              <span class="ds-section__badge">SUPERVISÓRIO SCADA</span>
              <h2 class="ds-section__title">11. Ficha Técnica Comparativa (PIR vs EPS)</h2>
            </div>
            <button class="ds-copy-btn" data-copy="table.jd-specs-table" data-copy-label="Tabela copiada!">Copiar Tabela</button>
          </div>
          <p class="ds-desc">
            Tabela de especificações técnicas para laudos de compras e comparação direta entre o PIR classe II-A e o isopor (EPS) convencional.
          </p>

          <div style="overflow-x:auto;">
            <table class="jd-specimen" style="width:100%;border-collapse:collapse;font-size:13px;text-align:left;">
              <thead>
                <tr style="border-bottom:2px solid rgba(55,180,206,0.4);background:rgba(0,0,0,0.5);">
                  <th style="padding:14px;color:var(--jd-cinza-aco);font-family:'JetBrains Mono';">PARÂMETRO TÉCNICO</th>
                  <th style="padding:14px;color:var(--jd-ciano);font-family:'JetBrains Mono';">PADRÃO JD CÂMARAS (PIR)</th>
                  <th style="padding:14px;color:#737373;font-family:'JetBrains Mono';">ISOPOR COMUM (EPS)</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                  <td style="padding:14px;font-weight:700;color:#FFF;">Condutividade Térmica (k)</td>
                  <td style="padding:14px;color:#00E676;font-weight:700;">0,022 W/m.K (Isolamento Máximo)</td>
                  <td style="padding:14px;color:#9CADC2;">0,040 W/m.K (quase o dobro de perda)</td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                  <td style="padding:14px;font-weight:700;color:#FFF;">Comportamento ao Fogo</td>
                  <td style="padding:14px;color:#00E676;font-weight:700;">Classe II-A (Retardante à chama IT-10)</td>
                  <td style="padding:14px;color:#E53935;">Propaga fogo e fumaça tóxica</td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                  <td style="padding:14px;font-weight:700;color:#FFF;">Consumo do Compressor</td>
                  <td style="padding:14px;color:#00E676;font-weight:700;">Até 35% de economia de energia</td>
                  <td style="padding:14px;color:#E53935;">Compressor trabalha sobrecarregado</td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                  <td style="padding:14px;font-weight:700;color:#FFF;">Encaixe dos Painéis</td>
                  <td style="padding:14px;color:#00E676;font-weight:700;">Macho-fêmea com vedante e selante</td>
                  <td style="padding:14px;color:#9CADC2;">Encaixe simples com pontes térmicas</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <!-- 12. BARRA DE PROVA SOCIAL -->
        <section id="sec-provas" class="ds-section">
          <div class="ds-section__head">
            <div>
              <span class="ds-section__badge">AUTORIDADE FABRIL</span>
              <h2 class="ds-section__title">12. Faixa de Provas Sociais e Métricas</h2>
            </div>
            <button class="ds-copy-btn" data-copy="<div class='jd-provas'>...</div>" data-copy-label="Provas copiadas!">Copiar Bloco</button>
          </div>
          <div class="jd-provas jd-cantoneira">
            <div class="jd-provas__item">
              <div class="jd-provas__numero">2.500+</div>
              <div class="jd-provas__label">Obras Instaladas</div>
            </div>
            <div class="jd-provas__item">
              <div class="jd-provas__numero">15 Anos</div>
              <div class="jd-provas__label">De Experiência Fabril</div>
            </div>
            <div class="jd-provas__item">
              <div class="jd-provas__numero">2 Fábricas</div>
              <div class="jd-provas__label">Ubá-MG e Anápolis-GO</div>
            </div>
            <div class="jd-provas__item">
              <div class="jd-provas__numero">100%</div>
              <div class="jd-provas__label">Normas ABNT e Anvisa</div>
            </div>
          </div>
        </section>

        <!-- 13. TIMELINE (7 A 15 DIAS) -->
        <section id="sec-timeline" class="ds-section">
          <div class="ds-section__head">
            <div>
              <span class="ds-section__badge">CRONOGRAMA ÁGIL</span>
              <h2 class="ds-section__title">13. Linha do Tempo (7 a 15 Dias)</h2>
            </div>
            <button class="ds-copy-btn" data-copy="<div class='jd-passos'>...</div>" data-copy-label="Timeline copiada!">Copiar Timeline</button>
          </div>
          <p class="ds-desc">
            Fluxo simplificado da assinatura do projeto até a entrega montada e comissionada no endereço do cliente.
          </p>

          <div class="jd-passos jd-specimen">
            <div class="jd-passo">
              <div class="jd-passo__icon">1</div>
              <div class="jd-passo__content">
                <span class="jd-passo__numero">ETAPA 01</span>
                <h4 class="jd-passo__titulo">Dimensionamento &amp; Projeto</h4>
                <p class="jd-passo__desc">Cálculo térmico exato da carga e modulação dos painéis.</p>
              </div>
            </div>
            <div class="jd-passo">
              <div class="jd-passo__icon">2</div>
              <div class="jd-passo__content">
                <span class="jd-passo__numero">ETAPA 02</span>
                <h4 class="jd-passo__titulo">Fabricação Industrial</h4>
                <p class="jd-passo__desc">Corte e injeção contínua de PIR nas fábricas de MG ou GO.</p>
              </div>
            </div>
            <div class="jd-passo">
              <div class="jd-passo__icon">3</div>
              <div class="jd-passo__content">
                <span class="jd-passo__numero">ETAPA 03</span>
                <h4 class="jd-passo__titulo">Entrega &amp; Montagem</h4>
                <p class="jd-passo__desc">Equipe própria instala em 7 a 15 dias com teste de temperatura.</p>
              </div>
            </div>
          </div>
        </section>

        <!-- 14. GALERIA DE OBRAS REAIS -->
        <section id="sec-galeria" class="ds-section">
          <div class="ds-section__head">
            <div>
              <span class="ds-section__badge">CASES INSTALADOS</span>
              <h2 class="ds-section__title">14. Galeria de Obras Reais (com Lightbox)</h2>
            </div>
            <button class="ds-copy-btn" data-copy="<div class='jd-galeria'>...</div>" data-copy-label="Galeria copiada!">Copiar Galeria</button>
          </div>

          <div class="jd-galeria">
            <div class="jd-galeria__item jd-spotlight" style="background:#171A29;display:grid;place-items:center;">
              <div style="padding:24px;text-align:center;">
                <span style="font-size:32px;">❄</span>
                <strong style="display:block;color:#FFF;margin-top:8px;">Distribuidora de Carnes</strong>
                <span style="font-size:11px;color:var(--jd-ciano);">Câmara de Congelados -18°C (85 m³)</span>
              </div>
            </div>
            <div class="jd-galeria__item jd-spotlight" style="background:#171A29;display:grid;place-items:center;">
              <div style="padding:24px;text-align:center;">
                <span style="font-size:32px;">🍺</span>
                <strong style="display:block;color:#FFF;margin-top:8px;">Supermercado Regional</strong>
                <span style="font-size:11px;color:var(--jd-ciano);">Walk-in Cooler 6 Portas Vidro</span>
              </div>
            </div>
            <div class="jd-galeria__item jd-spotlight" style="background:#171A29;display:grid;place-items:center;">
              <div style="padding:24px;text-align:center;">
                <span style="font-size:32px;">🍎</span>
                <strong style="display:block;color:#FFF;margin-top:8px;">Ceasa Hortifrúti</strong>
                <span style="font-size:11px;color:var(--jd-ciano);">Câmara Climatizada +12°C</span>
              </div>
            </div>
          </div>
        </section>

        <!-- 15. DEPOIMENTOS -->
        <section id="sec-depoimentos" class="ds-section">
          <div class="ds-section__head">
            <div>
              <span class="ds-section__badge">AVALIAÇÃO DE CLIENTES</span>
              <h2 class="ds-section__title">15. Depoimentos de Donos de Negócio</h2>
            </div>
            <button class="ds-copy-btn" data-copy="<div class='jd-depoimentos'>...</div>" data-copy-label="Depoimentos copiados!">Copiar Depoimentos</button>
          </div>

          <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:20px;">
            <div class="jd-spotlight jd-cantoneira" style="padding:24px;">
              <div style="color:var(--jd-amarelo);font-size:16px;margin-bottom:8px;">★★★★★</div>
              <p style="font-size:13.5px;line-height:1.6;color:var(--jd-cinza-aco);margin-bottom:16px;">
                "Comprei para meu supermercado em Goiás. Entregaram antes dos 15 dias combinados e a conta de energia veio muito mais baixa que a câmara de isopor antiga."
              </p>
              <strong style="display:block;font-size:13px;color:#FFF;">Marcos Vinícius</strong>
              <span style="font-size:11px;color:var(--jd-ciano);">Dono de Supermercado — Anápolis-GO</span>
            </div>

            <div class="jd-spotlight jd-cantoneira" style="padding:24px;">
              <div style="color:var(--jd-amarelo);font-size:16px;margin-bottom:8px;">★★★★★</div>
              <p style="font-size:13.5px;line-height:1.6;color:var(--jd-cinza-aco);margin-bottom:16px;">
                "O walk-in cooler de 8 portas na conveniência virou a atração do posto. A cerveja sai trincando e o abastecimento por trás não atrapalha o cliente."
              </p>
              <strong style="display:block;font-size:13px;color:#FFF;">Eduardo Rezende</strong>
              <span style="font-size:11px;color:var(--jd-ciano);">Rede de Conveniências — Juiz de Fora-MG</span>
            </div>
          </div>
        </section>

        <!-- 16. CLIENTES & MARCAS -->
        <section id="sec-clientes" class="ds-section">
          <div class="ds-section__head">
            <div>
              <span class="ds-section__badge">HOMOLOGAÇÃO INDUSTRIAL</span>
              <h2 class="ds-section__title">16. Clientes e Componentes de Grife</h2>
            </div>
            <button class="ds-copy-btn" data-copy="Danfoss, Bitzer, Elgin, Full Gauge" data-copy-label="Parceiros copiados!">Copiar Logos</button>
          </div>

          <div style="display:flex;gap:24px;flex-wrap:wrap;align-items:center;justify-content:center;padding:24px;background:rgba(255,255,255,0.03);border-radius:8px;">
            <span style="font-family:'JetBrains Mono';font-size:16px;font-weight:800;color:var(--jd-cinza-aco);">DANFOSS</span>
            <span style="font-family:'JetBrains Mono';font-size:16px;font-weight:800;color:var(--jd-cinza-aco);">BITZER</span>
            <span style="font-family:'JetBrains Mono';font-size:16px;font-weight:800;color:var(--jd-cinza-aco);">FULL GAUGE</span>
            <span style="font-family:'JetBrains Mono';font-size:16px;font-weight:800;color:var(--jd-cinza-aco);">ELGIN</span>
            <span style="font-family:'JetBrains Mono';font-size:16px;font-weight:800;color:var(--jd-cinza-aco);">BOMBRIL</span>
          </div>
        </section>

        <!-- 17. FAQ ACCORDION -->
        <section id="sec-faq" class="ds-section">
          <div class="ds-section__head">
            <div>
              <span class="ds-section__badge">SEO &amp; SCHEMA.ORG</span>
              <h2 class="ds-section__title">17. FAQ Técnico com Accordion Acessível</h2>
            </div>
            <button class="ds-copy-btn" data-copy="details.jd-faq-item" data-copy-label="FAQ copiado!">Copiar FAQ</button>
          </div>

          <div style="display:flex;flex-direction:column;gap:12px;">
            <details class="jd-faq-item jd-spotlight" style="padding:18px 24px;border-radius:8px;cursor:pointer;">
              <summary style="font-weight:700;color:#FFF;font-size:15px;list-style:none;display:flex;justify-content:space-between;align-items:center;">
                <span>Qual a forma de pagamento e faturamento da câmara?</span>
                <span style="color:var(--jd-ciano);font-family:'JetBrains Mono';font-size:18px;">+</span>
              </summary>
              <p style="margin-top:14px;font-size:13.5px;line-height:1.6;color:var(--jd-cinza-aco);">
                Faturamos direto da fábrica via cartão BNDES em até 48x, financiamento bancário para empresas ou condições especiais de entrada + parcelas durante a fabricação.
              </p>
            </details>

            <details class="jd-faq-item jd-spotlight" style="padding:18px 24px;border-radius:8px;cursor:pointer;">
              <summary style="font-weight:700;color:#FFF;font-size:15px;list-style:none;display:flex;justify-content:space-between;align-items:center;">
                <span>A JD entrega montada no meu endereço?</span>
                <span style="color:var(--jd-ciano);font-family:'JetBrains Mono';font-size:18px;">+</span>
              </summary>
              <p style="margin-top:14px;font-size:13.5px;line-height:1.6;color:var(--jd-cinza-aco);">
                Sim. Temos frota própria e técnicos credenciados que entregam e montam a câmara no seu local com teste de estanqueidade e comissionamento de temperatura.
              </p>
            </details>
          </div>
        </section>

        <!-- 18. WHATSAPP FLUTUANTE -->
        <section id="sec-whatsapp-float" class="ds-section">
          <div class="ds-section__head">
            <div>
              <span class="ds-section__badge">CONVERSÃO MOBILE</span>
              <h2 class="ds-section__title">18. Botão Flutuante de WhatsApp (Radar Ping)</h2>
            </div>
            <button class="ds-copy-btn" data-copy="<a href='...' class='jd-whatsapp-float'>...</a>" data-copy-label="WhatsApp copiado!">Copiar Botão</button>
          </div>
          <p class="ds-desc">
            Botão flutuante posicionado no canto inferior direito com anel concêntrico de radar ativo, indicando atendimento em tempo real.
          </p>

          <div class="ds-specimen" style="display:flex;align-items:center;gap:20px;">
            <div style="position:relative;display:inline-block;">
              <div style="width:56px;height:56px;border-radius:50%;background:#008749;display:grid;place-items:center;color:#FFF;font-size:24px;box-shadow:0 10px 25px rgba(0,135,73,0.4);">
                💬
              </div>
              <div class="jd-radar-ping" style="color:#008749;position:absolute;inset:0;"></div>
            </div>
            <div>
              <strong style="color:#FFF;font-size:14px;display:block;">Atendimento Fabril Instantâneo</strong>
              <span style="color:var(--jd-cinza-aco);font-size:12px;">Horário: Seg a Sex das 07h às 18h // Plantão aos Sábados</span>
            </div>
          </div>
        </section>

        <!-- 19. RODAPÉ INSTITUCIONAL -->
        <section id="sec-rodape" class="ds-section">
          <div class="ds-section__head">
            <div>
              <span class="ds-section__badge">AUTORIDADE JURÍDICA</span>
              <h2 class="ds-section__title">19. Rodapé Institucional com Dados de Fábrica</h2>
            </div>
            <button class="ds-copy-btn" data-copy="<footer class='jd-footer'>...</footer>" data-copy-label="Rodapé copiado!">Copiar Rodapé</button>
          </div>

          <div class="ds-specimen" style="background:#09080F;padding:32px;border-radius:8px;">
            <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(200px, 1fr));gap:24px;margin-bottom:24px;">
              <div>
                <strong style="color:#FFF;font-size:13px;display:block;margin-bottom:8px;">FÁBRICA MATRIZ (MG)</strong>
                <span style="color:var(--jd-cinza-aco);font-size:12px;line-height:1.6;display:block;">
                  Av. Industrial, Distrito Fabril<br>Ubá - MG, CEP 36500-000<br>Tel: (32) 3532-4000
                </span>
              </div>
              <div>
                <strong style="color:#FFF;font-size:13px;display:block;margin-bottom:8px;">FÁBRICA FILIAL (GO)</strong>
                <span style="color:var(--jd-cinza-aco);font-size:12px;line-height:1.6;display:block;">
                  Distrito Agroindustrial de Anápolis (DAIA)<br>Anápolis - GO, CEP 75132-000<br>Tel: (62) 3902-8000
                </span>
              </div>
              <div>
                <strong style="color:#FFF;font-size:13px;display:block;margin-bottom:8px;">CERTIFICAÇÕES</strong>
                <span style="color:var(--jd-cinza-aco);font-size:12px;line-height:1.6;display:block;">
                  ✔ Norma ABNT NBR 16678<br>✔ Laudo Anvisa RDC 216<br>✔ Classificação IT-10 Classe II-A
                </span>
              </div>
            </div>
            <div style="border-top:1px solid rgba(255,255,255,0.08);padding-top:16px;text-align:center;font-size:11px;color:rgba(156,173,194,0.6);">
              © 2026 JD Câmaras Frias Ltda — Todos os direitos reservados. CNPJ: 00.000.000/0001-00
            </div>
          </div>
        </section>

        <!-- 20. LGPD & COOKIES BANNER -->
        <section id="sec-cookies" class="ds-section">
          <div class="ds-section__head">
            <div>
              <span class="ds-section__badge">CONSENT MODE V2</span>
              <h2 class="ds-section__title">20. Banner LGPD &amp; Consent Mode v2</h2>
            </div>
            <button class="ds-copy-btn" data-copy="<div class='jd-cookies'>...</div>" data-copy-label="Banner copiado!">Copiar LGPD</button>
          </div>

          <div class="ds-specimen" style="background:#09080F;border:1px solid rgba(55,180,206,0.3);padding:20px;border-radius:8px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px;">
            <p style="font-size:12.5px;color:var(--jd-cinza-aco);margin:0;max-width:55ch;">
              Utilizamos cookies e telemetria para otimizar sua experiência e personalizar anúncios de acordo com a nossa Política de Privacidade.
            </p>
            <div style="display:flex;gap:10px;">
              <button class="jd-btn jd-btn--primary" style="font-size:11px;padding:8px 16px;"><span>ACEITAR TODOS</span></button>
              <button class="jd-btn jd-btn--dark" style="font-size:11px;padding:8px 16px;"><span>RECUSAR</span></button>
            </div>
          </div>
        </section>

        <!-- 21. PLAYGROUND & SANDBOX -->
        <section id="sec-playground" class="ds-section">
          <div class="ds-section__head">
            <div>
              <span class="ds-section__badge">TESTES EM TEMPO REAL</span>
              <h2 class="ds-section__title">21. Sandbox / Playground Interativo</h2>
            </div>
          </div>
          <p class="ds-desc">
            Alterne estados interativos para verificar o comportamento dinâmico de todos os componentes sob diferentes condições de luz e uso.
          </p>

          <div class="jd-spotlight" style="padding:24px;">
            <div style="display:flex;gap:12px;flex-wrap:wrap;margin-bottom:20px;">
              <button class="catalog-tool-btn is-active" onclick="document.body.classList.toggle('fx')">Toggle Efeitos (.fx)</button>
              <button class="catalog-tool-btn" onclick="document.getElementById('jd-theme-toggle').click()">Toggle Tema (Dark/Clean)</button>
              <button class="catalog-tool-btn" onclick="document.getElementById('jd-sfx-toggle').click()">Toggle Áudio Mecânico</button>
            </div>
            <span style="font-size:12px;color:var(--jd-ciano);">Clique nos botões acima para testar as reações do sistema em tempo real.</span>
          </div>
        </section>

        <!-- 22. EXPORT DE TOKENS & CHECKLIST -->
        <section id="sec-export" class="ds-section">
          <div class="ds-section__head">
            <div>
              <span class="ds-section__badge">ENTREGA HOMOLOGADA</span>
              <h2 class="ds-section__title">22. Checklist de Validação &amp; Export</h2>
            </div>
            <button class="ds-copy-btn" data-copy=":root { --jd-azul: #4181BC; --jd-marinho: #3B497F; }" data-copy-label="Tokens copiados!">Exportar Tokens</button>
          </div>

          <div class="jd-specimen" style="font-family:'JetBrains Mono';font-size:12px;line-height:1.8;color:var(--jd-cinza-aco);">
            <div style="color:#00E676;">✔ [TOKENS] Cores originais preservadas e complementadas com atmosfera criogênica</div>
            <div style="color:#00E676;">✔ [WCAG AA] Taxas de contraste verificadas e aprovadas para todas as ações</div>
            <div style="color:#00E676;">✔ [LEADS] Formulário em 2 etapas integrado com UTM e máscara de WhatsApp</div>
            <div style="color:#00E676;">✔ [TESTE A/B] Arquiteturas prontas para LP A (Direta) e LP B (Rica)</div>
            <div style="color:#00E676;">✔ [EXCLUSIVIDADE] Raio-X 3D isométrico, simulador de carga térmica e áudio Web Audio API</div>
          </div>
        </section>

      </div>
    </div>
  </div>

  <!-- Design System Scripts Core -->
  <script src="{PATH_PREFIX}js/ds.js"></script>
  <script src="{PATH_PREFIX}js/effects.js"></script>

  <script>
    // Gerenciador de Alternância de Abas: VISÃO GERAL vs COMPONENTES
    (function () {
      var tabOverview = document.getElementById('tab-btn-overview');
      var tabComponents = document.getElementById('tab-btn-components');
      var viewOverview = document.getElementById('view-overview');
      var viewComponents = document.getElementById('view-components');

      function switchView(target) {
        if (target === 'overview') {
          tabOverview.classList.add('is-active');
          tabComponents.classList.remove('is-active');
          viewOverview.classList.add('is-active');
          viewComponents.classList.remove('is-active');
          window.scrollTo({ top: 0, behavior: 'smooth' });
        } else {
          tabComponents.classList.add('is-active');
          tabOverview.classList.remove('is-active');
          viewComponents.classList.add('is-active');
          viewOverview.classList.remove('is-active');
        }
      }

      tabOverview.addEventListener('click', function(e) {
        e.preventDefault();
        switchView('overview');
      });

      tabComponents.addEventListener('click', function(e) {
        e.preventDefault();
        switchView('components');
      });

      // Se houver hash na URL apontando para seção de componentes
      if (window.location.hash && window.location.hash.startsWith('#sec-')) {
        switchView('components');
      }

      // Formulário em 2 Etapas Demo
      var btnNext = document.getElementById('btn-next-step');
      var btnPrev = document.getElementById('btn-prev-step');
      var step1 = document.getElementById('step-1');
      var step2 = document.getElementById('step-2');
      var progressBar = document.getElementById('form-progress-bar');
      var title = document.getElementById('form-step-title');
      var percent = document.getElementById('form-step-percent');

      if (btnNext && step1 && step2) {
        btnNext.addEventListener('click', function () {
          var tipo = document.getElementById('lead-tipo');
          var tel = document.getElementById('lead-telefone');
          if (!tipo.value) { alert('Selecione o modelo desejado.'); tipo.focus(); return; }
          if (tel.value.length < 10) { alert('Informe um telefone válido com DDD.'); tel.focus(); return; }

          step1.style.display = 'none';
          step2.style.display = 'block';
          progressBar.style.width = '100%';
          title.textContent = 'ETAPA 2 DE 2: LOCAL DA OBRA';
          percent.textContent = '100%';
        });

        btnPrev.addEventListener('click', function () {
          step2.style.display = 'none';
          step1.style.display = 'block';
          progressBar.style.width = '50%';
          title.textContent = 'ETAPA 1 DE 2: DADOS BÁSICOS';
          percent.textContent = '50%';
        });
      }

      // Smooth scroll para links da sidebar
      var sideLinks = document.querySelectorAll('.components-sidebar a');
      sideLinks.forEach(function (link) {
        link.addEventListener('click', function (e) {
          sideLinks.forEach(function (l) { l.classList.remove('is-active'); });
          link.classList.add('is-active');
        });
      });
    })();
  </script>
</body>
</html>
'''

def main():
    base_dir = r"c:\Users\pteix\Downloads\LP - JD CAMARAS"
    ds_dir = os.path.join(base_dir, "ds-jd-camaras")

    # 1. Arquivo no subdiretório ds-jd-camaras/design-system.html
    html_sub = HTML_CONTENT.replace("{PATH_PREFIX}", "")
    file_ds_html = os.path.join(ds_dir, "design-system.html")
    with open(file_ds_html, "w", encoding="utf-8") as f:
        f.write(html_sub)
    print("Salvo com sucesso:", file_ds_html)

    # 2. Arquivo no subdiretório ds-jd-camaras/ds_oficial.html
    file_ds_oficial_sub = os.path.join(ds_dir, "ds_oficial.html")
    with open(file_ds_oficial_sub, "w", encoding="utf-8") as f:
        f.write(html_sub)
    print("Salvo com sucesso:", file_ds_oficial_sub)

    # 3. Arquivo na raiz c:\Users\pteix\Downloads\LP - JD CAMARAS\ds_oficial.html
    html_root = HTML_CONTENT.replace("{PATH_PREFIX}", "ds-jd-camaras/")
    file_ds_oficial_root = os.path.join(base_dir, "ds_oficial.html")
    with open(file_ds_oficial_root, "w", encoding="utf-8") as f:
        f.write(html_root)
    print("Salvo com sucesso:", file_ds_oficial_root)

if __name__ == "__main__":
    main()
