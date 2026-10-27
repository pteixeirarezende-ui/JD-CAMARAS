# PROMPT 02 — LP A (direta) · Dobra 1: cabeçalho + hero com formulário (Antigravity)

> Como usar: no mesmo projeto, depois do DS aprovado (01c). Anexe `ds_variacao.html` final e a pasta `ds-jd-camaras`. Cole tudo abaixo da linha. Quando voltar, traga o `lp-a/index.html` para validar antes da Dobra 2.

---

## CONTEXTO

Vamos construir a **LP A da JD Câmaras Frias, dobra por dobra**. A LP A é a versão **direta**: formulário na primeira tela, página curta, foco em velocidade e em gerar lead pelo Google Ads (pesquisa por "câmara fria", "mini câmara fria", "walk-in cooler" e similares). Ela concorre em teste A/B com a LP B (mais rica), então **não** inclui efeitos pesados.

Estrutura final da LP A (para você saber onde isto se encaixa; **hoje só faça a Dobra 1**):
1. **Hero + formulário** ← esta etapa
2. 3 provas
3. Produtos (4 cards)
4. Como funciona
5. Obras
6. CTA final + rodapé

## REGRAS INEGOCIÁVEIS

1. **Use somente o DS aprovado** (`ds_variacao.html` + `ds-jd-camaras/css` e `js`). Só tokens, classes e componentes que já existem. **Não crie tokens, cores, componentes ou variantes novos.** Se faltar algo, use o mais próximo e liste no final em "O que faltou no DS", sem implementar.
2. **Antes de cada elemento, confirme:** "isso existe no DS?" e "o texto está no brief ou é invenção minha?".
3. **Zero invenção de conteúdo.** Todo número, prazo, nome, selo ou claim que não esteja no brief abaixo fica como `[CONFIRMAR]` visível. Reaproveite do DS **apenas a estrutura**, nunca os valores de exemplo (`[0.000+]`, `[00 anos]`, ficha técnica de exemplo, etc.).
4. **Tema:** o hero usa o **tema escuro** (`--jd-noite`). Não use a camada de efeitos (`effects.css`, `effects.js`) na LP A: não carregue esses arquivos.
5. Cores só da tabela do DS. CTA principal: amarelo com texto `#101010`. Botão WhatsApp: verde.
6. Mobile-first. Teste em 360, 390, 768 e 1280. **Sem rolagem horizontal.**
7. A cada dobra futura você devolverá o **HTML completo e cumulativo**, sem modificar o que já foi aprovado. Nesta etapa só existe a dobra 1.

## BRIEF DE CONTEÚDO (única fonte permitida)

- Marca: **J.D. Câmaras Frias**, Ubá-MG, com filial em Anápolis-GO.
- Oferta: **câmaras frias modulares sob medida**: mini câmaras, câmaras expositoras (walk-in cooler), câmaras de resfriados (0 a +15 °C) e de congelados (-18 °C). **Telhas térmicas NÃO entram.**
- Processo: projeto sob medida, entrega e instalação, com suporte depois (ampliação, manutenção e correção).
- O cliente fornece a energia elétrica e, se necessário, o piso.
- Público: donos e compradores de conveniências, supermercados, distribuidoras de bebidas, farmácias, logística e órgãos públicos. PF e PJ.
- Tom: direto, técnico e simples, como um fabricante falando com o dono do negócio. Português do Brasil, sem exagero.
- **Proibido aparecer, mesmo como exemplo:** "supercongelados -125 °C", "entregamos em todo o Brasil", "a mais famosa do Brasil", "garantia de 5 anos", qualquer menção a ABNT, Anvisa, patente, Inmetro, selo, certificação, prazo de entrega em dias, percentual de economia.
- Dados que ainda **não temos** e devem ficar como placeholder: número de WhatsApp, e-mail de recebimento, razão social, CNPJ, endereço, telefone, quantidade de câmaras instaladas, anos de mercado, fotos reais, nomes de clientes, depoimentos.

## ENTREGA: DOBRA 1

### Estrutura de arquivos

```
/lp-a
  index.html
  /css     (copie tokens.css, base.css, components.css do DS; NÃO copie effects.css)
  /js      (copie ds.js do DS; crie lp.js para o que é específico da LP; NÃO copie effects.js)
  /assets  (logo-jd.png, favicon placeholder, imagens da câmara como placeholder)
```

### 1. `<head>`
- `lang="pt-BR"`, viewport, `<title>` com **no máximo 60 caracteres**: "Câmara Fria sob Medida | JD Câmaras Frias" (ajuste se passar).
- `meta description` com até 155 caracteres, sem claim proibido.
- `<meta name="robots" content="noindex, nofollow">` **por enquanto** (a LP é só para anúncio e ainda não foi publicada). Deixe comentário `<!-- remover noindex só se decidirmos indexar -->`.
- Google Fonts do DS (Archivo + Inter) com `preconnect` e `display=swap`.
- **Marcadores de tracking como comentários** (não ative nada):
  `<!-- GTM: inserir snippet do container [GTM-XXXXXXX] aqui -->` no head e `<!-- GTM noscript -->` logo após o `<body>`.
- Declare `window.dataLayer = window.dataLayer || [];` e deixe o **Consent Mode v2** com estado padrão `denied` para `ad_storage`, `ad_user_data`, `ad_personalization` e `analytics_storage`, comentado como "configurar junto com o banner de cookies na Dobra final".
- Pré-carregue a imagem do hero se houver (`fetchpriority="high"`), sem `loading="lazy"` nela.

### 2. Cabeçalho da LP
Use o componente **"Cabeçalho da LP"** do DS: logo + botão "Pedir orçamento" (que rola suavemente até o formulário no desktop e, no mobile, também). Sem menu.

### 3. Hero A (tema escuro) com formulário na primeira tela
Use o componente **Hero A** do DS.

Textos (use exatamente; marque `[CONFIRMAR]` onde indicado):
- Eyebrow: **PROJETO SOB MEDIDA, ENTREGA E INSTALAÇÃO**
- H1: **Câmara fria sob medida, projetada e instalada para o seu negócio**
- Subtítulo: **Mini câmaras, câmaras expositoras, resfriados e congelados. Informe o que você vai armazenar e as medidas do espaço e receba o orçamento da JD.**
- 3 provas curtas (use o componente de prova do DS; **mantenha a etiqueta `EXEMPLO`**):
  1. `[CONFIRMAR]` câmaras instaladas
  2. `[CONFIRMAR]` anos de experiência
  3. Projeto sob medida para o seu espaço *(este é fato do brief, **sem** etiqueta de exemplo)*
- Chips de faixa de temperatura do DS ("Congelados (-18 °C)" e "Resfriados (0 a +15 °C)") em uma linha, rolável no mobile. **Não use o mostrador "Núcleo: -18 °C"**, ele é só efeito e não faz parte da LP A.
- Imagem do hero: placeholder rotulado do DS: "Foto de obra: câmara fria instalada". No mobile, a imagem vem **depois** do formulário (o formulário deve aparecer na primeira tela do celular sem rolar muito).

### 4. Formulário em 2 etapas (componente do DS)
- **Etapa 1:** Nome + WhatsApp (máscara BR `(00) 00000-0000`). Botão "Continuar".
- **Etapa 2:** Tipo de câmara (select: Mini câmara · Câmara expositora/walk-in · Câmara de resfriados · Câmara de congelados · Não sei ainda), medida aproximada (largura × comprimento × altura em metros, **opcional**), cidade + UF, "O que você vai armazenar?" (select: Bebidas · Alimentos · Carnes · Hortifrúti · Medicamentos/vacinas · Outro). Botão "Pedir orçamento".
- **Sem** campo de energia, **sem** dois telefones, **sem** campo de texto livre obrigatório.
- Validação inline com **ícone + texto** (nunca só cor). Estado de sucesso: "Recebemos seu pedido. A JD vai chamar você no WhatsApp." (sem prometer prazo).
- Microcópia abaixo do botão: "Seus dados são usados só para enviar o orçamento." com link `[CONFIRMAR: política de privacidade]`.
- **Campos ocultos** preenchidos por JS a partir da URL e de `document.referrer`: `utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content`, `gclid`, `gbraid`, `wbraid`, `landing_page`, `lp_version` (fixo `"A"`), `timestamp_envio` (ISO, no envio).
- Guarde UTM e `gclid` em `sessionStorage` com `try/catch` para sobreviver a recarga.
- **Envio:** crie `const LEAD_ENDPOINT = '';` em `lp.js` com `// TODO: URL do webhook/Apps Script que grava na planilha e dispara WhatsApp + e-mail`. Com endpoint vazio, o envio **não falha silenciosamente**: mostre, no modo de desenvolvimento (`?debug=1`), o JSON que seria enviado no console, e na tela mostre o estado de sucesso normalmente. Com endpoint preenchido, `POST` em JSON com `fetch`, com tratamento de erro (mensagem + botão "Tentar de novo") e proteção contra duplo clique.
- **Anti-spam simples:** campo honeypot escondido (`name="website"`) que descarta o envio se preenchido.

### 5. Eventos de tracking (dataLayer, sem ativar nada)
Envie com `dataLayer.push` nos momentos abaixo, com `lp_version: "A"` em todos:
- `lead_form_start` (primeiro foco em qualquer campo)
- `lead_form_step1_complete`
- `lead_form_submit` (somente em sucesso de envio)
- `click_whatsapp` (clique no botão de WhatsApp, quando existir)
- `click_cta_header` (clique no botão do cabeçalho)
Documente a lista no README em uma tabela (evento, quando dispara, parâmetros).

### 6. Botão de WhatsApp
Mostre o botão "Chamar no WhatsApp" do DS no hero. Mantenha a regra do DS: com `WHATSAPP_NUMBER` vazio, ele aparece **desabilitado** com a etiqueta `[CONFIRMAR NÚMERO]`. Corrija a etiqueta para **não ser cortada** em 360/390 px (quebre em duas linhas ou reduza o padding). A mensagem pré-preenchida, quando houver número: "Olá! Vim pelo site e quero um orçamento de câmara fria."

### 7. Performance e acessibilidade
- Sem biblioteca externa de JS. Tudo em `lp.js` + `ds.js`. Peso do HTML + CSS + JS da dobra 1 estimado no README.
- Imagens com `width` e `height` (sem CLS). Ícones em SVG inline.
- Labels em todos os campos, `autocomplete` correto (`name`, `tel`, `address-level2`), `inputmode="tel"` no telefone, alvos de 44 px, foco visível, `prefers-reduced-motion` respeitado.
- Contraste AA em todos os pares usados.

## AUTOVERIFICAÇÃO (README da LP, seção "Dobra 1")

1. Lista de classes e componentes do DS usados e confirmação de que **nenhum token ou componente novo** foi criado.
2. Busca por hex ou `rgb()` fora do DS: resultado (deve ser zero).
3. Busca pelos termos proibidos: resultado (deve ser zero fora de `[CONFIRMAR]`).
4. Rolagem horizontal em 360 / 390 / 768 / 1280: sim ou não.
5. O formulário aparece na primeira tela do mobile (390 × 844)? Informe a posição (em px) do botão da etapa 1.
6. Tabela de eventos do dataLayer.
7. Placeholders pendentes da dobra 1 (lista).
8. **O que faltou no DS** (se algo).

No final da resposta, em até 5 linhas: o que foi entregue, o que ficou pendente do cliente e qualquer decisão sua que eu deva revisar.
