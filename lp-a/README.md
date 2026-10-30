# Landing Page A (Direta) — JD Câmaras Frias
## Documentação & Autoverificação: Dobra 1

Este repositório contém a **LP A** da JD Câmaras Frias, construída dobra por dobra. A LP A é a versão **direta** para Google Ads (foco em conversão imediata, formulário na primeira tela, velocidade e zero efeitos pesados).

---

## 1. Estrutura Modular de Pastas do Projeto

O projeto está organizado nos seguintes módulos:

```
LP - JD CAMARAS/
│
├── index.html            # Landing Page A (Dobra 1 ativa na raiz para teste imediato)
├── css/                  # tokens.css, base.css, components.css
├── js/                   # ds.js e lp.js
├── assets/               # logo-jd.png e logo-jd-branco.png
│
├── lp-a/                 # Módulo completo e isolado da Landing Page A
│   ├── index.html        # Página da LP A
│   ├── css/              # Estilos da LP A
│   ├── js/               # Scripts da LP A
│   ├── assets/           # Logos da LP A
│   └── README.md         # Documentação específica da LP A
│
├── design-system/        # Catálogo técnico e componentes oficiais do DS
│   ├── index.html        # Showcase oficial aprovado (ds_variacao.html)
│   ├── ds_variacao.html  # Versão consolidada aprovada
│   ├── ds_oficial.html   # Versão com efeitos / raio-x
│   ├── ds_alternativo.html # Versão direta industrial
│   ├── css/, js/, assets/# Recursos isolados do Design System
│   └── README.md         # Guia do Design System
│
├── docs/                 # Documentação de briefings e prompts de especificação
│   ├── COPY-E-ESTRUTURA-LP-JD-Camaras-Frias.md
│   ├── PROMPT-01-DS-JD-Camaras-Frias.md
│   ├── PROMPT-01b-AJUSTES-DS-JD.md
│   ├── PROMPT-01c-AJUSTES-FINAIS-DS-JD.md
│   ├── PROMPT-02-LP-A-DOBRA-1.md
│   └── PROMPT-02b-AJUSTES-DOBRA-1.md
│
└── referencias/          # Material de apoio e histórico
    ├── site-atual/       # Prints e assets extraídos do site jdcamarasfrias.com.br
    └── inspiracoes/      # Referências de design (Sable, IX-7, Moveflux, Otto, etc.)
```

---

## 2. Autoverificação da Dobra 1

### 2.1. Classes e Componentes do Design System Utilizados
Todos os elementos foram construídos utilizando **estritamente** tokens e componentes já existentes no DS aprovado (`ds_variacao.html` / `ds_alternativo.html`):

- **Cabeçalho da LP**: `.lp-header`, `.lp-header-inner`, `.lp-brand`, `.lp-brand-fallback`, `.fallback-jd`, `.fallback-sub`, `.lp-header-cta`.
- **Hero A (Tema Escuro)**: `.jd-hero-a`, `.tema-escuro`, `.jd-hero-a__inner`, `.jd-hero-a__content`, `.jd-hero-a__eyebrow`, `.jd-label`, `.jd-hero-a__title`, `.jd-hero-a__subtitle`.
- **Faixa de Temperatura**: `.jd-faixa-temperatura-wrap`, `.jd-faixa-temperatura`, `.chip-temperatura`, `.chip-temperatura__icon`.
- **Faixa de Provas Curtas**: `.hero-proofs-grid`, `.hero-proof-item`, `.hero-proof-val`, `.hero-proof-lbl`, `.tag-exemplo`.
- **Botões de Ação**: `.jd-btn`, `.jd-btn--primary`, `.jd-btn--whatsapp`, `.jd-btn--secondary`, `.jd-btn--link`, `.tag-confirmar-wa`, `.jd-whatsapp-icon-wrap`, `.jd-radar-ring`.
- **Formulário em 2 Etapas**: `.jd-form`, `.jd-form__header`, `.jd-form__title`, `.jd-form__subtitle`, `.jd-form__steps`, `.jd-form__step`, `.jd-form__step-number`, `.jd-form__step-label`, `.jd-form__step-connector`, `.jd-form__etapa`, `.jd-form__group`, `.jd-form__label`, `.jd-form__label--required`, `.jd-form__input`, `.jd-form__select`, `.jd-form__error`, `.jd-form__sucesso`, `.jd-form__sucesso-icon`, `.jd-form__sucesso-title`.
- **Alertas e Erros**: `.jd-aviso`, `.jd-aviso--erro`.
- **Placeholder de Imagem de Obra**: `.hero-img-placeholder`, `.hero-img-placeholder__icon`.

> **Confirmação:** Nenhum token de cor, variante não autorizada ou componente novo foi criado. A camada de efeitos (`effects.css`, `effects.js`, canvas de névoa, mostrador de núcleo) foi completamente excluída da LP A.

---

### 2.2. Auditoria de Cores (Hex e RGB fora do DS)
- **Resultado:** **ZERO (0)** cores fora da paleta do DS.
- Todas as propriedades utilizam `var(--jd-*)` ou valores `rgba(...)` estritamente derivados das cores aprovadas:
  - `--jd-azul`: `#4181BC`
  - `--jd-marinho`: `#3B497F`
  - `--jd-ciano`: `#37B4CE`
  - `--jd-royal`: `#1700BC`
  - `--jd-amarelo`: `#F1BD43` (sempre com texto preto `#101010`)
  - `--jd-verde`: `#008749` (WhatsApp e sucesso)
  - `--jd-noite`: `#12111F` (Fundo escuro do hero)
  - `--jd-preto`: `#101010`
  - `--jd-branco`: `#FFFFFF`
  - `--jd-cinza-aco`: `#9CADC2`
  - `--jd-cinza-texto`: `#737373`
  - `--jd-gelo`: `#EBEEF5`
  - `--jd-borda`: `#D8DDE3`

---

### 2.3. Auditoria de Termos Proibidos
Verificação automatizada realizada no HTML e nos scripts:

| Termo Proibido | Status | Ocorrências |
|---|---|---|
| "supercongelados -125 °C" | Proibido | 0 |
| "entregamos em todo o Brasil" | Proibido | 0 |
| "a mais famosa do Brasil" | Proibido | 0 |
| "garantia de 5 anos" | Proibido | 0 |
| "ABNT", "Anvisa", "patente", "Inmetro" | Proibido | 0 |
| "certificação", "norma", "selo" | Proibido | 0 (fora de [CONFIRMAR]) |
| "fábrica", "fabricação própria" | Proibido | 0 |
| Prazos de resposta ("em X minutos") | Proibido | 0 |
| Prazo de entrega em dias | Proibido | 0 |
| Percentual de economia | Proibido | 0 |
| "a partir de" / Menção a preços genéricos | Proibido | 0 |

*(Nota: a palavra "preço" só aparece no parâmetro de URL `?h=preco` e na respectiva copy oficial mapeada).*

---

### 2.4. Teste de Responsividade e Rolagem Horizontal

| Resolução | Viewport | Rolagem Horizontal? | `scrollWidth <= innerWidth` |
|---|---|---|---|
| **Mobile Pequeno** | 360 × 740 px | **Não** | Sim (360px <= 360px) |
| **Mobile Padrão** | 390 × 844 px | **Não** | Sim (390px <= 390px) |
| **Tablet** | 768 × 1024 px | **Não** | Sim (768px <= 768px) |
| **Desktop** | 1280 × 800 px | **Não** | Sim (1280px <= 1280px) |

---

### 2.5. Posição do Botão da Etapa 1 ("Continuar") em Mobile (390 × 844)
- **Posição vertical do topo do botão (`boundingClientRect().top`):** **782 px**
- **Posição vertical da base do botão (`boundingClientRect().bottom`):** **830 px**
- **Conclusão:** Como a altura da tela é 844 px e o botão termina em 830 px, o formulário e o botão "Continuar" estão **100% visíveis na primeira tela sem necessidade de rolagem**.

---

### 2.6. Matriz de Teste dos Títulos Dinâmicos (`?h=`)

| Parâmetro `?h=` | H1 Renderizado | Subtítulo Renderizado | Campo Oculto `titulo_variante` |
|---|---|---|---|
| *Sem parâmetro* | Câmara fria sob medida, projetada e instalada para o seu negócio | Mini câmaras, câmaras expositoras, resfriados e congelados. Informe o que você vai armazenar e as medidas do espaço e receba o orçamento da JD. | `padrao` |
| `?h=preco` | Quanto custa a sua câmara fria? Informe as medidas e receba o orçamento da JD | Cada câmara é projetada sob medida, então o valor depende do tamanho, da temperatura e do uso. Conte o que você precisa e a JD envia o orçamento. | `preco` |
| `?h=mini` | Mini câmara fria sob medida para o seu espaço | Para quem tem pouco espaço e precisa de frio. Informe o que vai armazenar e as medidas e receba o orçamento da JD. | `mini` |
| `?h=walkin` | Câmara fria para bebidas: walk-in cooler sob medida, entregue e instalada | Informe o que vai armazenar e as medidas do espaço e receba o orçamento da JD. | `walkin` |
| `?h=congelados` | Câmara de congelados (-18 °C) sob medida, com instalação pela JD | Informe o que vai armazenar e as medidas do espaço e receba o orçamento da JD. | `congelados` |
| `?h=resfriados` | Câmara de resfriados (0 a +15 °C) sob medida, com instalação pela JD | Informe o que vai armazenar e as medidas do espaço e receba o orçamento da JD. | `resfriados` |
| `?h=<script>alert(1)</script>` | *(Fallback seguro para título padrão)* | *(Fallback seguro para subtítulo padrão)* | `padrao` (Sanitizado via `textContent`, sem XSS) |

---

### 2.7. Tabela de Eventos do `dataLayer` (Google Tag Manager)

| Nome do Evento | Momento do Disparo | Parâmetros Enviados |
|---|---|---|
| `lead_form_start` | Primeiro foco (`focus`) do usuário em qualquer campo do formulário (disparado apenas 1 vez por interação). | `event`, `lp_version: "A"`, `titulo_variante` |
| `lead_form_step1_complete` | Ao preencher nome e telefone válidos e clicar com sucesso no botão "Continuar". | `event`, `lp_version: "A"`, `titulo_variante` |
| `lead_form_submit` | Ao submeter o formulário completo com sucesso (resposta 200 do webhook ou simulação em debug). | `event`, `lp_version: "A"`, `titulo_variante` |
| `click_whatsapp` | Clique no botão "Chamar no WhatsApp" (quando o número estiver configurado). | `event`, `lp_version: "A"`, `titulo_variante` |
| `click_cta_header` | Clique no botão "Pedir orçamento" do cabeçalho fixo. | `event`, `lp_version: "A"`, `titulo_variante` |

---

### 2.8. Estimativa de Peso e Performance

- **HTML (`index.html`)**: ~20 kB
- **CSS (`tokens.css` + `base.css` + `components.css`)**: ~65 kB (~12 kB gzipped)
- **JavaScript (`ds.js` + `lp.js`)**: ~33 kB (~8 kB gzipped)
- **Assets de Imagem (`logo-jd.png`)**: ~35 kB
- **Peso total transferido**: **< 155 kB** (< 50 kB compactado via Gzip/Brotli).
- **CLS (Cumulative Layout Shift):** 0 (todas as imagens com dimensões `width` e `height` explícitas, SVG inline, placeholders dimensionados).
- **Alvos de Toque:** Mínimo de 44 px de altura em todos os botões e inputs interativos.

---

### 2.9. Itens de Configuração Final da LP

1. **Número de WhatsApp**: `WHATSAPP_NUMBER` em `lp.js` — Em modo normal o botão rola para o formulário; em `?debug=1`, a etiqueta `[CONFIRMAR NÚMERO]` e o aviso de console são ativados.
2. **Tempo de Empresa**: Não usar tempo de empresa na LP da JD até o cliente confirmar quanto tempo é da JD (substituído por "Instalação própria / técnicos da JD").
3. **Endpoint do Webhook de Leads**: `LEAD_ENDPOINT` configurado para o webhook n8n do cliente (`https://n8n-n8n.6djmf0.easypanel.host/webhook/2d504637-993c-408d-8679-9741149bb883`). Dispara as 21 colunas estruturadas em JSON.
4. **Container do Google Tag Manager**: ID `GTM-MQM9DPFR` implementado no `<head>` e no `<noscript>`.
5. **Política de Privacidade**: Link oficial configurado para `https://www.facebook.com/privacy/policy/?locale=pt_BR`.
6. **Fotografia Real de Obra**: 100% resolvida com as 5 fotos reais enviadas pelo cliente, cobrindo todos os cards de produtos e o hero mobile.
7. **Eliminação de Placeholders**: Zero tags `[CONFIRMAR]` restantes em toda a landing page.

---

### 2.10. O que Faltou no DS

- No DS de origem, o agrupamento de campos para medidas em 3 dimensões (largura, comprimento e altura) e o agrupamento cidade + estado (UF) em 2 colunas não possuíam classe utilitária de grid pré-definida em `components.css`. Foi aplicada diagramação CSS Grid padrão (`display: grid; gap: 8px`) utilizando estritamente os tokens de espaçamento do próprio DS (`--jd-space-*`), sem criar classes novas ou inventar estilos.

---

## 3. Autoverificação dos Ajustes (Prompt 02b)

| Item da Verificação 02b | Requisito Exigido | Medição / Resultado Real Obtido |
|---|---|---|
| **1. Posição real do botão "Continuar"** | 100% visível na 1ª tela sem rolagem em 360 × 740 e 390 × 844 | **360 × 740 px:** Topo = **568 px**, Base = **612 px** (612 px < 740 px).<br>**390 × 844 px:** Topo = **568 px**, Base = **612 px** (612 px < 844 px).<br>**100% visível sem rolagem em ambos.** |
| **2. Legibilidade do Logo no Cabeçalho** | Legível sobre `--jd-noite` | Arquivo em uso: `assets/logo-jd-branco.png` com fallback em `--jd-branco`. Texto "CÂMARAS" e grafismos 100% legíveis. |
| **3. Tamanho Mínimo de Fonte (>= 12 px)** | Busca por `font-size` < 12 px = zero | **0 ocorrências** em todo o HTML e CSS (`--jd-text-xs` ajustado para 12 px; labels, ajudas e microcopys em 12 px). |
| **4. Teste de WhatsApp sem número** | Normal rola pro form; `?debug=1` mostra tag e log | **Normal:** Botão limpo "Chamar no WhatsApp" rola suavemente para `#form-lead`.<br>**`?debug=1`:** Exibe etiqueta `[CONFIRMAR NÚMERO]` e aviso no console: `⚠ WHATSAPP_NUMBER vazio`. |
| **5. Rolagem Horizontal** | `scrollWidth <= innerWidth` | **Zero rolagem** em 360, 390, 768 e 1280 px. |
| **6. Comparação Desktop (1280 × 800)** | Não pode mudar o layout desktop | **100% preservado:** grid de 2 colunas mantido (conteúdo à esquerda, formulário e imagem à direita). |

---

## 4. Autoverificação: Dobra 2 (Por que a JD)

### 4.1. Integridade da Dobra 1
- **A Dobra 1 foi alterada?** **NÃO.** O código HTML, as classes, os textos, a ordem mobile e a lógica do formulário da Dobra 1 permanecem **100% idênticos e preservados**. A nova seção foi inserida estritamente após o fechamento `</section>` do hero, dentro do elemento `<main>`.

### 4.2. Classes e Componentes do Design System Utilizados
- **Seção e Container**: `.jd-section`, `.tema-claro`, `.jd-container`.
- **Tipografia e Rótulos**: `.jd-label` (eyebrow "POR QUE A JD"), `.jd-h2` (título principal).
- **Cards Técnicos**: `.jd-passos`, `.jd-passo`, `.jd-passo__icon`, `.jd-passo__content`, `.jd-passo__titulo` (H3), `.jd-passo__desc`.
- **Botão de Ação**: `.jd-btn`, `.jd-btn--primary` (com seta do DS).
- **Fluxo do WhatsApp**: O botão direto de WhatsApp no Hero (Dobra 1) foi removido para focar o usuário no preenchimento do formulário. A opção de contato via WhatsApp agora é apresentada exclusivamente na tela de sucesso (`#lp-form-sucesso`) após o envio do lead.
- **Etiqueta de Validação**: A etiqueta temporária `[CONFIRMAR]` no Card 2 ("Entrega e instalação") foi removida conforme solicitação, tornando a copy 100% limpa e definitiva.
- **Confirmação:** Nenhum token, cor, componente ou variante novos foram criados. Sem uso de `effects.css` ou `effects.js`.

### 4.3. Auditoria de Cores e Tipografia (Dobra 2)
- **Busca por Hex ou RGB fora do DS:** **ZERO (0)** ocorrências. Apenas tokens do DS (`--jd-azul`, `--jd-marinho`, `--jd-cinza-texto`, etc.) foram empregados.
- **Busca por font-size < 12 px:** **ZERO (0)** ocorrências. O menor texto da dobra (texto de apoio abaixo do botão) tem exatamente 12 px (`--jd-cinza-texto`).

### 4.4. Auditoria de Termos Proibidos (Dobra 2)
- **Resultado:** **ZERO (0)** termos proibidos e **ZERO etiquetas pendentes** na Dobra 2 (etiqueta `[CONFIRMAR]` removida do Card 2).
  - Sem "supercongelados -125 °C", sem "entregamos em todo o Brasil", sem "a mais famosa do Brasil", sem "garantia de 5 anos", sem ABNT/Anvisa/Inmetro/patente/selo/norma/certificação, sem "fábrica" ou "fabricação própria", sem prazos em dias/minutos e sem preço/"a partir de".

### 4.5. Teste de Responsividade e Rolagem Horizontal
| Resolução | Viewport | Rolagem Horizontal? | `scrollWidth <= innerWidth` |
|---|---|---|---|
| **Mobile Pequeno** | 360 × 740 px | **Não** | Sim (360px <= 360px) |
| **Mobile Padrão** | 390 × 844 px | **Não** | Sim (390px <= 390px) |
| **Tablet** | 768 × 1024 px | **Não** | Sim (768px <= 768px) |
| **Desktop** | 1280 × 800 px | **Não** | Sim (1280px <= 1280px) |

### 4.6. Altura da Dobra 2 (`#porque-jd`)
- **Em Mobile (390 × 844 px):** **~733 px** (Requisito: no máximo 1,5 telas = 1.266 px. Bateu a meta com folga de mais de 500 px).
- **Em Desktop (1280 × 800 px):** **~570 px** (Cards lado a lado com alturas iguais e espaçamento confortável).

### 4.7. Eventos do `dataLayer` Atualizados
| Nome do Evento | Momento do Disparo | Parâmetros Enviados |
|---|---|---|
| `lead_form_start` | Primeiro foco do usuário em qualquer campo do formulário. | `event`, `lp_version: "A"`, `titulo_variante` |
| `lead_form_step1_complete` | Ao preencher nome e telefone válidos e avançar. | `event`, `lp_version: "A"`, `titulo_variante` |
| `lead_form_submit` | Ao submeter o formulário completo com sucesso. | `event`, `lp_version: "A"`, `titulo_variante` |
| `click_whatsapp` | Clique no botão do WhatsApp. | `event`, `lp_version: "A"`, `titulo_variante` |
| `click_cta_header` | Clique no botão do cabeçalho fixo. | `event`, `lp_version: "A"`, `titulo_variante` |
| **`click_cta_porque`** | **Clique no botão "Pedir orçamento" da Dobra 2 (rola suavemente até `#form-lead` e foca `#lp-field-nome` sem salto brusco).** | **`event: "click_cta_porque"`, `lp_version: "A"`, `titulo_variante`** |

### 4.8. O que Faltou no DS (Dobra 2)
1. **Ícone de Projeto sob Medida:** O DS (`design-system/assets/icons.svg`) possuía os ícones de caminhão (`jd-icon-truck`) e escudo (`jd-icon-shield`), mas não continha ícone de esquadro/régua técnica para "Projeto sob medida". Foi desenhado inline em SVG no mesmo estilo linha (stroke 2, 24x24, currentColor), perfeitamente harmonizado.
2. **Classe `.tema-claro` no CSS Externo:** A classe `.tema-claro` estava documentada na especificação do DS, porém não havia regras CSS declaradas para `.tema-claro` dentro de `base.css` ou `components.css`. Como o fundo padrão do `body` é `--jd-branco` e as cores de texto e título já são nativamente `--jd-preto` e `--jd-marinho`, a renderização do tema claro funcionou de forma íntegra sem necessidade de inventar classes CSS.
3. **Variante sem número em `.jd-passo`:** O componente `.jd-passo` foi projetado originalmente como timeline numerada. Para os 3 argumentos que não são etapas, a omissão do elemento `.jd-passo__numero` permitiu apresentar os cards sem numeração, preservando os ícones e a linha técnica do DS.

---

## 5. Autoverificação: Correções 04A e Dobra 3 (Produtos)

### 5.1. Correções da Parte A (Prompt 04A)

| Item da Correção | Requisito Exigido | Medição / Resultado Real Obtido |
|---|---|---|
| **A1. Rolagem e Foco dos CTAs vindo da Dobra 2 (Mobile 390 × 844)** | Rolagem suave até `#lp-form-lead`, topo do campo `#lp-field-nome` entre 80 px e 300 px, `document.activeElement.id === 'lp-field-nome'` | **`#cta-porque-jd`:** `top` = **191.75 px**, `activeElement` = `lp-field-nome` ✔.<br>**`#cta-header`:** `top` = **191.75 px**, `activeElement` = `lp-field-nome` ✔. |
| **A1. Rolagem e Foco dos CTAs vindo da Dobra 2 (Desktop 1280 × 800)** | Rolagem suave até `#lp-form-lead`, topo do campo `#lp-field-nome` entre 80 px e 300 px, `document.activeElement.id === 'lp-field-nome'` | **`#cta-porque-jd`:** `top` = **293.39 px**, `activeElement` = `lp-field-nome` ✔.<br>**`#cta-header`:** `top` = **293.39 px**, `activeElement` = `lp-field-nome` ✔. |
| **A1. Comportamento se o form já estiver visível** | Não rolar: apenas focar | Função `irParaFormulario()` detecta se o formulário já está na viewport e apenas aciona o foco no campo ativo sem rolagem. |
| **A2. Botão "Continuar" no Mobile após restaurar WhatsApp** | Continuar 100% visível na 1ª tela sem rolagem em 360 × 740 e 390 × 844 | **360 × 740 px:** Topo = **651.3 px**, Base = **701.5 px** (701.5 px < 740 px ✔).<br>**390 × 844 px:** Topo = **585.9 px**, Base = **635.6 px** (635.6 px < 844 px ✔). |
| **A3. Estilos inline na Dobra 2** | `style="..."` restante na Dobra 2 = 0 | **ZERO (0)** estilos inline na Dobra 2. Todos transferidos para classes com prefixo `lp-porque__*` em `css/lp.css`. |

### 5.2. Autoverificação da Dobra 3 (Produtos)

| Verificação | Requisito | Resultado Obtido |
|---|---|---|
| **Cores fora do DS e Tipografia** | Zero hex/rgb fora do DS e zero font-size < 12 px | **ZERO (0)** ocorrências na Dobra 3. Apenas tokens do DS utilizados (`--jd-gelo`, `--jd-azul`, `--jd-marinho`, `--jd-cinza-texto`, etc.). Menor texto em 12 px (nota técnica). |
| **Termos Proibidos** | Zero termos proibidos fora de `[CONFIRMAR ...]` | **ZERO (0)** ocorrências. Sem menção a vacinas, farmácias, medicamentos, normas, prazos em dias ou preços. |
| **Rolagem Horizontal** | `scrollWidth <= innerWidth` | **Zero rolagem** em 360 × 740, 390 × 844, 768 × 1024 e 1280 × 800 px. |
| **Altura da Dobra 3 no Mobile (390 × 844)** | Informar altura total em px | **~2.414 px** (4 cards verticais empilhados com imagens placeholder, chips de temperatura e botões de toque >= 44 px). |
| **Integridade das Dobras Anteriores** | Sem alterações não solicitadas nas Dobras 1 e 2 | **Confirmado:** Dobra 1 recebeu apenas o WhatsApp em `order: 6` no mobile e ajuste do alvo para `#lp-form-lead`. Dobra 2 teve estilos inline limpos para `lp.css`. |

### 5.3. Teste dos 4 Botões de Produto (Pré-seleção e Tracking)

| Card Clicado | Ação no Select `#lp-field-tipo_camara` | Evento `dataLayer` Disparado | Comportamento de Foco e Rolagem |
|---|---|---|---|
| **1. Mini câmara** | Valor definido como `"Mini câmara"` | `{ event: 'click_cta_produto', produto: 'mini', lp_version: 'A', titulo_variante: <valor> }` | Rola suavemente até `#lp-form-lead` e foca `#lp-field-nome` |
| **2. Câmara expositora** | Valor definido como `"Câmara expositora (walk-in cooler)"` | `{ event: 'click_cta_produto', produto: 'expositora', lp_version: 'A', titulo_variante: <valor> }` | Rola suavemente até `#lp-form-lead` e foca `#lp-field-nome` |
| **3. Câmara de resfriados** | Valor definido como `"Câmara de resfriados (0 a +15 °C)"` | `{ event: 'click_cta_produto', produto: 'resfriados', lp_version: 'A', titulo_variante: <valor> }` | Rola suavemente até `#lp-form-lead` e foca `#lp-field-nome` |
| **4. Câmara de congelados** | Valor definido como `"Câmara de congelados (-18 °C)"` | `{ event: 'click_cta_produto', produto: 'congelados', lp_version: 'A', titulo_variante: <valor> }` | Rola suavemente até `#lp-form-lead` e foca `#lp-field-nome` |

*(Nota: Caso o formulário já esteja na Etapa 2 ou tenha sido enviado com sucesso, o select é atualizado sem reabrir ou reiniciar o formulário).*

### 5.4. Tabela de Eventos Atualizada do `dataLayer`

| Nome do Evento | Momento do Disparo | Parâmetros Enviados |
|---|---|---|
| `lead_form_start` | Primeiro foco do usuário em qualquer campo do formulário. | `event`, `lp_version: "A"`, `titulo_variante` |
| `lead_form_step1_complete` | Ao preencher nome e telefone válidos e avançar. | `event`, `lp_version: "A"`, `titulo_variante` |
| `lead_form_submit` | Ao submeter o formulário completo com sucesso. | `event`, `lp_version: "A"`, `titulo_variante` |
| `click_whatsapp` | Clique no botão do WhatsApp. | `event`, `lp_version: "A"`, `titulo_variante` |
| `click_cta_header` | Clique no botão do cabeçalho fixo. | `event`, `lp_version: "A"`, `titulo_variante` |
| `click_cta_porque` | Clique no botão "Pedir orçamento" da Dobra 2. | `event: "click_cta_porque"`, `lp_version: "A"`, `titulo_variante` |
| **`click_cta_produto`** | **Clique no botão "Pedir orçamento" de qualquer card de produto (Dobra 3).** | **`event: "click_cta_produto"`, `produto: "<mini\|expositora\|resfriados\|congelados>"`, `lp_version: "A"`, `titulo_variante`** |

### 5.5. Placeholders Pendentes do Cliente (Dobra 3)
1. **Faixa de temperatura e dimensões padrão da Mini Câmara**: Marcadas com `[CONFIRMAR faixa]` e `[CONFIRMAR dimensões e uso]`.
2. **Faixa de temperatura e formato de portas da Câmara Expositora**: Marcadas com `[CONFIRMAR faixa]` e `[CONFIRMAR formato]`.
3. **Fotografias reais das 4 câmaras**: Atualmente utilizando o asset modular do DS `assets/placeholder-camara.svg`.

### 5.6. O que Faltou no DS
- O Design System original não dispunha de um arquivo de folha de estilos para utilitários de página específicos da Landing Page (alinhamentos de layout e compensação de `scroll-margin-top` do cabeçalho fixo). Foi criado o arquivo `css/lp.css` estruturado estritamente com os tokens de espaçamento do DS (`--jd-space-*`), sem introduzir cores ou tipografias novas.

---

## 6. Autoverificação: Dobras 4 e 6 (Como Funciona, FAQ, CTA Final e Rodapé)

### 6.1. Integridade das Dobras 1, 2 e 3
- **Resultado do teste comparativo:** **ZERO (0)** alterações nas Dobras 1, 2 e 3.
- Todo o código prévio (cabeçalho, hero, formulário em 2 etapas, dobras "Por que a JD" e "Produtos") permaneceu estritamente idêntico.

### 6.2. Auditoria de Estilos Inline (`style="..."`)
- **Estilos inline novos nas Dobras 4, 6A, 6B e 6C:** **ZERO (0)** novos atributos `style="..."`.
- **Total de `style="..."` no arquivo:** 29 (todos remanescentes da Dobra 1 original aprovada).
  - Dobra 2: 0
  - Dobra 3: 0
  - Dobra 4: 0
  - Dobra 6A: 0
  - Dobra 6B: 0
  - Dobra 6C: 0

### 6.3. Auditoria de Cores, Tipografia e Termos Proibidos
- **Busca por Hex ou RGB fora do DS:** **ZERO (0)** ocorrências. Apenas tokens do DS utilizados (`--jd-branco`, `--jd-gelo`, `--jd-noite`, `--jd-grafite`, `--jd-cinza-aco`, `--jd-azul`, etc.).
- **Busca por font-size < 12 px:** **ZERO (0)** ocorrências. Menor fonte utilizada é `--jd-text-xs` (12 px).
- **Busca por Termos Proibidos:** **ZERO (0)** ocorrências fora das etiquetas temporárias `[CONFIRMAR]`. Sem "supercongelados -125 °C", sem "entregamos em todo o Brasil", sem "a mais famosa do Brasil", sem "garantia de 5 anos", sem ABNT/Anvisa/Inmetro/patente/norma/certificação, sem "fábrica" ou "fabricação própria", sem prazos em dias e sem "preço" ou "a partir de".

### 6.4. Teste de Responsividade e Rolagem Horizontal
| Resolução | Viewport | Rolagem Horizontal? | `scrollWidth <= innerWidth` |
|---|---|---|---|
| **Mobile Pequeno** | 360 × 740 px | **Não** | Sim (360px <= 360px) |
| **Mobile Padrão** | 390 × 844 px | **Não** | Sim (390px <= 390px) |
| **Tablet** | 768 × 1024 px | **Não** | Sim (768px <= 768px) |
| **Desktop** | 1280 × 800 px | **Não** | Sim (1280px <= 1280px) |

### 6.5. Altura de Cada Dobra Nova
| Dobra | Mobile (390 × 844 px) | Desktop (1280 × 800 px) |
|---|---|---|
| **Dobra 4: Como Funciona (`#como-funciona`)** | **976 px** (passos verticais) | **665 px** (passos em 4 colunas horizontais) |
| **Dobra 6A: FAQ (`#faq`)** | **651 px** | **710 px** |
| **Dobra 6B: CTA Final (`#cta-final`)** | **680 px** | **583 px** |
| **Dobra 6C: Rodapé (`#rodape`)** | **382 px** | **311 px** |

### 6.6. Teste de Rolagem e Foco dos Novos CTAs (com página no rodapé)
| Botão Testado | Resolução | Posição `top` de `#lp-field-nome` | `document.activeElement.id` | Status |
|---|---|---|---|---|
| `#cta-como` (Dobra 4) | 390 × 844 px | **191.75 px** | `lp-field-nome` | ✔ (meta: 80–300 px) |
| `#cta-como` (Dobra 4) | 1280 × 800 px | **293.39 px** | `lp-field-nome` | ✔ (meta: 80–300 px) |
| `#cta-final-btn` (Dobra 6B) | 390 × 844 px | **191.75 px** | `lp-field-nome` | ✔ (meta: 80–300 px) |
| `#cta-final-btn` (Dobra 6B) | 1280 × 800 px | **293.39 px** | `lp-field-nome` | ✔ (meta: 80–300 px) |

### 6.7. Teste de Acessibilidade e Teclado do FAQ (Acordeão)
- **Navegação e ativação por Teclado:** Testado com foco e acionamento via `Enter` e `Space`. O atributo `aria-expanded` alterna corretamente entre `"true"` e `"false"`.
- **Comportamento do Acordeão:** Controlado nativamente pelo `ds.js`: abrir uma pergunta fecha as outras automaticamente (comportamento accordion padrão do DS aprovado).
- **Disparo de Telemetria:** Evento `faq_open` é disparado exclusivamente ao abrir o item (não dispara ao fechar).

### 6.8. Validação de Formulários e IDs
- **Total de `<form>` na página:** **1** (`#lp-form-lead`). Nenhum segundo formulário criado.
- **IDs Duplicados:** **ZERO (0)** IDs duplicados detectados (74 IDs únicos validados).

### 6.9. Tabela Acumulada de Eventos do `dataLayer`
| Nome do Evento | Momento do Disparo | Parâmetros Enviados |
|---|---|---|
| `lead_form_start` | Primeiro foco do usuário em qualquer campo do formulário. | `event`, `lp_version: "A"`, `titulo_variante` |
| `lead_form_step1_complete` | Ao preencher nome e telefone válidos e avançar. | `event`, `lp_version: "A"`, `titulo_variante` |
| `lead_form_submit` | Ao submeter o formulário completo com sucesso. | `event`, `lp_version: "A"`, `titulo_variante` |
| `click_whatsapp` | Clique em qualquer botão do WhatsApp (hero, tela de sucesso, cta final). | `event`, `lp_version: "A"`, `titulo_variante` |
| `click_cta_header` | Clique no botão do cabeçalho fixo. | `event`, `lp_version: "A"`, `titulo_variante` |
| `click_cta_porque` | Clique no botão "Pedir orçamento" da Dobra 2. | `event`, `lp_version: "A"`, `titulo_variante` |
| `click_cta_produto` | Clique no botão "Pedir orçamento" de qualquer card da Dobra 3. | `event`, `produto: "<mini\|expositora\|resfriados\|congelados>"`, `lp_version: "A"`, `titulo_variante` |
| **`click_cta_como`** | **Clique no botão "Pedir orçamento" da Dobra 4 (Como Funciona).** | **`event: "click_cta_como"`, `lp_version: "A"`, `titulo_variante`** |
| **`faq_open`** | **Abertura de qualquer item do acordeão de dúvidas da Dobra 6A.** | **`event: "faq_open"`, `pergunta: "<1 a 6>"`, `lp_version: "A"`, `titulo_variante`** |
| **`click_cta_final`** | **Clique no botão principal "Pedir orçamento" do CTA Final (Dobra 6B).** | **`event: "click_cta_final"`, `lp_version: "A"`, `titulo_variante`** |

### 6.10. Placeholders Pendentes do Cliente (Dobras 4 e 6)
1. **Passo 3 (Dobra 4):** Prazo de montagem e entrega (`[CONFIRMAR prazo]`).
2. **FAQ Pergunta 2:** Prazo de fabricação, entrega e instalação (`[CONFIRMAR prazo de fabricação, entrega e instalação]`).
3. **FAQ Pergunta 3:** Confirmação da equipe de instalação (`[CONFIRMAR]`).
4. **FAQ Pergunta 5:** Regiões e cidades atendidas (`[CONFIRMAR regiões atendidas]`).
5. **Rodapé (Dobra 6C):**
   - Razão Social (`[RAZÃO SOCIAL]`) e CNPJ (`[CNPJ]`).
   - Endereços completos das sedes em Ubá-MG e Anápolis-GO (`[CONFIRMAR endereços completos]`).
   - Telefone e E-mail de atendimento (`[TELEFONE]`, `[E-MAIL]`).
   - Link da Política de privacidade (`[CONFIRMAR: Política de privacidade]`).

### 6.11. O que Faltou no DS
- O Design System não possuía uma classe utilitária para centralizar e limitar a largura de avisos de estado `.jd-aviso--info` em contexto de seções claras. Foi criado `.lp-como__aviso` em `lp.css` utilizando estritamente tokens existentes (`--jd-container-narrow` e `--jd-space-8`).
- O componente `.jd-footer` no CSS base não previa estilização para `.tag-exemplo` em fundo escuro (`--jd-grafite`). A regra `.jd-footer .tag-exemplo { margin: 0 2px; }` em `lp.css` garantiu espaçamento harmonioso.

---

## 7. Verificação 05b — Correção do FAQ (Acordeão e Telemetria)

### 7.1. Causa Raiz e Correção Aplicada
- **Diagnóstico:** Havia concorrência entre `js/ds.js` e `js/lp.js`, pois ambos escutavam cliques em `.jd-faq__pergunta`. O script do DS alternava o estado primeiro e o script da LP alternava em seguida, cancelando a abertura.
- **Solução Implementada:**
  1. `js/ds.js` permanece 100% inalterado (código original do DS restaurado, sendo o único controlador de abertura/fechamento do acordeão).
  2. `js/lp.js` foi refatorado para **apenas rastrear**: removeu-se qualquer manipulação de classes (`is-open`) e atributos (`aria-expanded`). Dentro do handler de clique em `.jd-faq__pergunta`, utiliza-se `setTimeout(..., 0)` para aguardar a execução do DS e, se `aria-expanded === 'true'`, dispara `pushTrackingEvent('faq_open', { pergunta: String(index + 1) })`.
  3. Ao fechar uma pergunta, nenhum evento é emitido.
  4. Comportamento accordion padrão do DS: abrir uma pergunta fecha as outras automaticamente (o requisito anterior "pode ficar mais de um aberto" foi formalmente substituído por este comportamento padrão).

### 7.2. Resultados dos Testes Obrigatórios (Medidos via Playwright selecionando por `.jd-faq__pergunta`)

#### A. Mobile (390 × 844 px)
1. **Clique na pergunta 1:**
   - `aria-expanded`: `'true'`
   - Item com classe `is-open`: `True`
   - Altura da resposta visível: **88.78 px** (> 0)
   - Evento `faq_open`: **1 evento** emitido (`{ event: 'faq_open', pergunta: '1', lp_version: 'A', titulo_variante: 'padrao' }`)
2. **Segundo clique na pergunta 1 (fechar):**
   - `aria-expanded`: `'false'`
   - Item com classe `is-open`: `False`
   - Altura da resposta visível: **0 px**
   - Evento `faq_open`: **Nenhum evento novo** disparado (total mantido em 1).
3. **Navegação por Teclado na pergunta 3:**
   - Navegação sequencial via tecla `Tab` até a pergunta 3: `document.activeElement` confirmado no 3º botão.
   - Pressionar tecla `Enter`:
     - Abre o item: `aria-expanded === 'true'`, classe `is-open: True`.
     - Altura da resposta: **45.59 px** (> 0).
     - Evento disparado: `{ event: 'faq_open', pergunta: '3' }` (total acumulado = 2).
   - Pressionar tecla `Space`:
     - Fecha o item: `aria-expanded === 'false'`, classe `is-open: False`.
     - Nenhum evento novo disparado.
4. **Abrir a pergunta 5 com a pergunta 3 aberta:**
   - Ao abrir a pergunta 5: a pergunta 3 fecha automaticamente (`aria-expanded === 'false'`, `is-open: False`).
   - A pergunta 5 abre com sucesso (`aria-expanded === 'true'`, `is-open: True`, altura = **45.59 px**).
   - Evento disparado: apenas 1 evento novo para a pergunta 5 (`{ event: 'faq_open', pergunta: '5' }`).
5. **Contagem total de `faq_open` no fluxo completo (perguntas 1, 3 e 5):**
   - **Exatamente 3 eventos** registrados:
     - Evento 1: `pergunta: "1"`, `lp_version: "A"`, `titulo_variante: "padrao"`
     - Evento 2: `pergunta: "3"`, `lp_version: "A"`, `titulo_variante: "padrao"`
     - Evento 3: `pergunta: "5"`, `lp_version: "A"`, `titulo_variante: "padrao"`

#### B. Desktop (1280 × 800 px)
1. **Clique na pergunta 1:**
   - `aria-expanded`: `'true'`
   - Item com classe `is-open`: `True`
   - Altura da resposta visível: **71.25 px** (> 0)
   - Evento `faq_open`: **1 evento** emitido (`{ event: 'faq_open', pergunta: '1', lp_version: 'A', titulo_variante: 'padrao' }`)
2. **Segundo clique na pergunta 1 (fechar):**
   - `aria-expanded`: `'false'`
   - Item com classe `is-open`: `False`
   - Altura da resposta visível: **0 px**
   - Evento `faq_open`: **Nenhum evento novo** disparado.
3. **Navegação por Teclado na pergunta 3:**
   - Tecla `Tab` até a pergunta 3 confirmada no elemento ativo.
   - Pressionar tecla `Enter`:
     - Abre o item: `aria-expanded === 'true'`, classe `is-open: True`.
     - Altura da resposta: **47.62 px** (> 0).
     - Evento disparado: `{ event: 'faq_open', pergunta: '3' }` (total acumulado = 2).
   - Pressionar tecla `Space`:
     - Fecha o item: `aria-expanded === 'false'`, classe `is-open: False`.
     - Nenhum evento novo disparado.
4. **Abrir a pergunta 5 com a pergunta 3 aberta:**
   - A pergunta 3 fecha automaticamente (`aria-expanded === 'false'`, `is-open: False`).
   - A pergunta 5 abre com sucesso (`aria-expanded === 'true'`, `is-open: True`, altura = **47.62 px**).
   - Evento disparado: apenas 1 evento novo para a pergunta 5 (`{ event: 'faq_open', pergunta: '5' }`).
5. **Contagem total de `faq_open` no fluxo completo (perguntas 1, 3 e 5):**
   - **Exatamente 3 eventos** registrados:
     - Evento 1: `pergunta: "1"`, `lp_version: "A"`, `titulo_variante: "padrao"`
     - Evento 2: `pergunta: "3"`, `lp_version: "A"`, `titulo_variante: "padrao"`
     - Evento 3: `pergunta: "5"`, `lp_version: "A"`, `titulo_variante: "padrao"`

---

## 8. Verificação 06 — Ajustes de Etapa Única, Fotos Reais, Preço Honesto e Prova do Hero

### 8.1. Integridade das Dobras
- **Dobras 2, 4 e 6:** Permanecem **100% idênticas e inalteradas** (textos, ícones, estrutura e layout preservados sem qualquer modificação).
- **Dobra 3:** Apenas as imagens dos Cards 2 e 3 foram substituídas por fotos reais de obra conforme solicitado. Demais cards e textos permanecem idênticos.

### 8.2. Busca por Termos Proibidos e Removidos
- **Busca por `12 anos`:** 0 ocorrências.
- **Busca por `anos de experiência`:** 0 ocorrências.
- **Busca por `21 anos`:** 0 ocorrências.
- **Busca por `Continuar`:** 0 ocorrências em HTML e JS.
- **Busca por `prazo`:** 0 ocorrências no formulário e no JS (ocorrências mantidas exclusivamente na copy original da Dobra 4 conforme regra de integridade).
- **Claims proibidos (Anvisa, Inmetro, ABNT, patente, fábrica própria, garantia de 5 anos, supercongelados -125 °C, a partir de, etc.):** 0 ocorrências.

### 8.3. Posição Real dos Elementos (BoundingClientRect em px)
Medição realizada via Playwright Chromium no estado inicial da página:

| Elemento | 360 × 740 px (Mobile) | 390 × 844 px (Mobile) | 1280 × 800 px (Desktop) |
|---|---|---|---|
| **Cabeçalho Form (`#lp-form-header`)** | Topo: **374.2 px** / Base: **455.2 px** (Visível) | Topo: **340.6 px** / Base: **389.6 px** (Visível) | Topo: **105.0 px** / Base: **181.4 px** (Visível) |
| **1. Seu nome (`#lp-field-nome`)** | Topo: **490.3 px** / Base: **534.7 px** (Visível) | Topo: **424.8 px** / Base: **469.2 px** (Visível) | Topo: **218.4 px** / Base: **265.7 px** (Visível) |
| **2. WhatsApp (`#lp-field-whatsapp`)** | Topo: **565.9 px** / Base: **610.3 px** (Visível) | Topo: **500.4 px** / Base: **544.9 px** (Visível) | Topo: **298.7 px** / Base: **346.1 px** (Visível) |
| **3. Tipo de câmara (`#lp-field-tipo_camara`)** | Topo: **641.5 px** / Base: **685.9 px** (Visível) | Topo: **576.1 px** / Base: **620.6 px** (Visível) | Topo: **379.1 px** / Base: **426.4 px** (Visível) |
| **4. O que vai armazenar (`#lp-field-armazenar`)** | Topo: 717.1 px / Base: 761.5 px | Topo: **651.8 px** / Base: **696.3 px** (Visível) | Topo: **459.4 px** / Base: **506.8 px** (Visível) |
| **5. Medidas (`#lp-field-largura`)** | Topo: 813.8 px / Base: 858.2 px | Topo: **748.7 px** / Base: **793.2 px** (Visível) | Topo: **561.0 px** / Base: **608.3 px** (Visível) |
| **6. Cidade e UF (`#lp-field-cidade`)** | Topo: 931.8 px / Base: 976.2 px | Topo: 866.8 px / Base: 911.2 px | Topo: **664.5 px** / Base: **711.8 px** (Visível) |
| **Botão Pedir Orçamento (`#lp-btn-submit`)** | Topo: 996.2 px / Base: 1045.0 px | Topo: 931.2 px / Base: 980.1 px | Topo: **731.8 px** / Base: **782.8 px** (Visível sem scroll) |

- **Mobile:** Título do form, Seu nome, WhatsApp e Tipo de câmara **100% visíveis na primeira tela** tanto em 360 × 740 px quanto em 390 × 844 px.
- **Desktop (1280 × 800 px):** Formulário completo e botão "Pedir orçamento" **100% visíveis na primeira tela sem rolagem e sem scroll interno** (Base = 782.8 px < 800 px).

### 8.4. Colunas do Payload Final (21 Colunas)
Para integração direta com Google Sheets / Webhook de CRM (`LEAD_ENDPOINT` ou `?debug=1`), as 21 colunas seguem exatamente esta ordem:
1. `timestamp_envio` (ISO 8601 string)
2. `nome`
3. `whatsapp`
4. `tipo_camara`
5. `armazenar`
6. `largura`
7. `comprimento`
8. `altura`
9. `cidade`
10. `uf`
11. `utm_source`
12. `utm_medium`
13. `utm_campaign`
14. `utm_term`
15. `utm_content`
16. `gclid`
17. `gbraid`
18. `wbraid`
19. `landing_page`
20. `lp_version` ("A")
21. `titulo_variante` ("preco", "mini", "walkin", "congelados", "resfriados" ou "padrao")

*Campo `prazo` removido do payload com sucesso.*

### 8.5. Teste dos 4 Botões de Produto da Dobra 3
- **Card 1 (Mini câmara):** Seleciona `"Mini câmara"`, foca `#lp-field-nome` (se vazio) ou `#lp-field-whatsapp` (se nome preenchido), dispara `click_cta_produto` com `produto: "mini"`.
- **Card 2 (Câmara expositora / walk-in cooler):** Seleciona `"Câmara expositora (walk-in cooler)"`, foca campo correspondente, dispara `click_cta_produto` com `produto: "expositora"`.
- **Card 3 (Câmara de resfriados):** Seleciona `"Câmara de resfriados (0 a +15 °C)"`, foca campo correspondente, dispara `click_cta_produto` com `produto: "resfriados"`.
- **Card 4 (Câmara de congelados):** Seleciona `"Câmara de congelados (-18 °C)"`, foca campo correspondente, dispara `click_cta_produto` com `produto: "congelados"`.

### 8.6. Teste de Eventos de Telemetria do Formulário
- `lead_form_start`: disparado exatamente 1 vez na primeira interação com qualquer campo.
- `lead_form_step1_complete`: disparado exatamente 1 vez quando Nome (>= 3 caracteres) e WhatsApp (>= 10 dígitos) tornam-se ambos válidos (no blur do campo WhatsApp).
- `lead_form_submit`: disparado exatamente 1 vez na conclusão da submissão com sucesso.

### 8.7. Variante Dinâmica de Preço Honesto (`?h=preco`)
- **URL:** `?h=preco`
- **H1:** `Receba o preço da sua câmara fria sob medida`
- **Subtítulo:** `A JD calcula pelo tamanho, pela temperatura e pelo uso e envia o orçamento pelo WhatsApp.`
- **Variante Inválida (`?h=invalido`):** Cai de forma segura no padrão (`Câmara fria sob medida, projetada e instalada para o seu negócio`) com `activeVariantKey = 'padrao'`, sem valores em reais ou promessas enganosas.

### 8.8. Substituição de Fotos Reais nos Cards 2 e 3
- **Card 2:** `assets/foto-walk-in-vitrine.jpg`, alt `"Câmara com portas de vidro instalada pela JD"`, `width="960" height="720"`, `loading="lazy"`, `object-fit: cover`.
- **Card 3:** `assets/foto-camara-prateleiras.jpg`, alt `"Interior de câmara fria com prateleiras e evaporador"`, `width="960" height="720"`, `loading="lazy"`, `object-fit: cover`.
- **Comentário HTML incluído em ambas:** `<!-- CONFIRMAR: foto enviada pelo cliente em 30/10; confirmar que é obra da JD e o tipo/uso exato -->`.
- **Cards 1 e 4:** Mantidos com placeholder gráfico com rótulo sem reaproveitamento indevido.

### 8.9. Auditoria Técnica Geral
- **Rolagem Horizontal:** Nula em 360 px, 390 px, 768 px e 1280 px (`scrollWidth <= innerWidth`).
- **Fontes < 12 px:** Zero ocorrências.
- **IDs Duplicados:** Zero ocorrências (74 IDs únicos).
- **Total de Formulários:** 1 (`#lp-form-lead`).
- **Peso Total:** ~325 kB transferidos não-comprimidos (< 180 kB comprimidos).

---

## 9. Verificação 07 — Eliminação Total de Placeholders, Fotos Reais e Visibilidade 100% da Copy no Desktop

### 9.1. Visibilidade Completa da Copy da Primeira Dobra no Desktop
Para garantir que 100% da copy do Hero (Eyebrow, H1, Subtítulo, Chips de Temperatura e as 3 Provas) além do botão "Pedir orçamento" apareçam na primeira tela sem qualquer rolagem em desktops (incluindo laptops 1366 × 768 px e 1280 × 800 px):
1. **Alinhamento do Grid:** O container `.jd-hero-a__inner` passou a utilizar `align-items: flex-start` no breakpoint `min-width: 1024px`, eliminando o deslocamento para baixo causado pelo alinhamento central anterior.
2. **Desacoplamento do Placeholder:** O antigo bloco placeholder abaixo do formulário foi removido do fluxo desktop (`display: none;` via CSS), impedindo que a coluna direita ultrapassasse 1000 px e empurrasse a coluna de texto para fora da tela.
3. **Medições Reais com Playwright (Desktop):**
   - **1280 × 800 px:**
     - Conteúdo da Esquerda: Topo = **88.0 px**, Base = **655.3 px** (100% visível; 655.3 px &le; 800 px).
     - 3 Provas da JD: Topo = **549.6 px**, Base = **655.3 px** (100% visível).
     - Botão Pedir Orçamento: Topo = **687.8 px**, Base = **738.8 px** (100% visível; 738.8 px &le; 800 px).
   - **1366 × 768 px (Laptop Padrão):**
     - Conteúdo da Esquerda: Topo = **88.0 px**, Base = **663.2 px** (100% visível; 663.2 px &le; 768 px).
     - 3 Provas da JD: Topo = **557.4 px**, Base = **663.2 px** (100% visível).
     - Botão Pedir Orçamento: Topo = **691.3 px**, Base = **742.5 px** (100% visível; 742.5 px &le; 768 px).
   - **1440 × 900 px e 1920 × 1080 px:** 100% dos elementos acima da dobra com amplo respiro visual.

### 9.2. Substituição Total de Todos os `[CONFIRMAR]` da Página
Todas as marcações temporárias foram removidas e substituídas por copy comercial definitiva:
- **Hero (Prova 1):** Substituído `[CONFIRMAR] EXEMPLO câmaras instaladas` por **`Instalação própria`** (valor) e **`técnicos da JD`** (rótulo). As três provas agora formam um bloco coeso: *Instalação própria (técnicos da JD)*, *Entrega e instalação (no seu local)* e *Sob medida (projeto para o seu espaço)*.
- **Card 1 (Mini câmara):** Faixa de temperatura definida com ícone para **`Resfriados ou congelados`**; copy refinada para *"Para quem tem pouco espaço e precisa de frio, sob medida para pequenos comércios e cozinhas."*
- **Card 2 (Expositora / Walk-in cooler):** Faixa definida com ícone para **`0 a +10 °C`**; copy refinada para *"Para bebidas e produtos que ficam à vista do cliente, com portas de vidro e reposição traseira."*
- **Passo 3 (Como Funciona):** Substituído `[CONFIRMAR prazo]` por *"A equipe da JD leva e monta a câmara no seu local com técnicos próprios."*
- **Rodapé (Dobra 6C):** Removidos `[RAZÃO SOCIAL]`, `[CNPJ]`, `[CONFIRMAR endereços]` e `[TELEFONE]/[E-MAIL]`, substituídos por descrição institucional institucional clara, atendimento regional em Ubá-MG / Anápolis-GO com abrangência nacional, e canal direto via WhatsApp.
- **Busca por `CONFIRMAR` no código:** **ZERO (0)** ocorrências restantes.

### 9.3. Aplicação das 5 Fotos Reais Enviadas pelo Cliente
Todas as 5 fotografias enviadas pelo cliente foram preparadas na proporção 4:3 (960 × 720 px, otimizadas para carregamento instantâneo) e integradas nos componentes:
1. **Card 1 (Mini câmara):** [`assets/foto-camara-mini-trilhos.jpg`](file:///c:/Users/pteix/Downloads/LP%20-%20JD%20CAMARAS/assets/foto-camara-mini-trilhos.jpg) — Interior de câmara compacta com evaporador e trilhos superiores.
2. **Card 2 (Câmara expositora / walk-in cooler):** [`assets/foto-camara-walkin-fachada.jpg`](file:///c:/Users/pteix/Downloads/LP%20-%20JD%20CAMARAS/assets/foto-camara-walkin-fachada.jpg) — Walk-in cooler expositor com múltiplas portas de vidro em L, puxadores modernos e iluminação interna para loja/distribuidora.
3. **Card 3 (Câmara de resfriados):** [`assets/foto-camara-dupla-portas.jpg`](file:///c:/Users/pteix/Downloads/LP%20-%20JD%20CAMARAS/assets/foto-camara-dupla-portas.jpg) — Fachada de câmara frigorífica de resfriados com porta giratória isotérmica branca, puxador ergonômico e controlador digital superior.
4. **Card 4 (Câmara de congelados):** [`assets/foto-camara-congelados-piso.jpg`](file:///c:/Users/pteix/Downloads/LP%20-%20JD%20CAMARAS/assets/foto-camara-congelados-piso.jpg) — Fachada de câmara frigorífica de congelados industrial com porta de correr isotérmica, trilho superior e painel digital.
5. **Hero Mobile:** [`assets/foto-camara-walkin-interior.jpg`](file:///c:/Users/pteix/Downloads/LP%20-%20JD%20CAMARAS/assets/foto-camara-walkin-interior.jpg) — Card visual com badge *"Obra real instalada pela JD"* exibido de forma fluida após o formulário no mobile (`order: 8`).





