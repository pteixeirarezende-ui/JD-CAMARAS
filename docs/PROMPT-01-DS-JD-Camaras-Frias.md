# PROMPT 01 — Design System da JD Câmaras Frias (Antigravity)

> Como usar: abra um projeto novo no Antigravity. Anexe (1) `jd-logo-site-atual.png`, (2) `jd-site-atual-home.png` e (3) os zips/prints da pasta Inspirações (ou ao menos Sable, IX-7, Moveflux, Aurora Garden e Otto). Cole tudo abaixo da linha. Quando ele entregar, traga o resultado aqui para revisão antes do Prompt 02 (LP).

---

## CONTEXTO

Você vai criar o **Design System** da **JD Câmaras Frias** (Ubá-MG, filial em Anápolis-GO). A empresa projeta, fabrica, entrega e instala **câmaras frias modulares sob medida** (mini câmaras, câmaras expositoras/walk-in cooler, câmaras de resfriados 0 a 15 °C e de congelados -18 °C). Esse DS será a base de **duas landing pages de captação de leads** para Google Ads, que rodarão em teste A/B:

- **LP A, direta:** formulário na primeira tela, página curta, foco em velocidade.
- **LP B, rica:** mais ilustrativa, com fotos de obras, mais seções e efeitos pontuais.

**Público:** homens de 25 a 60 anos (foco 40 a 50), donos e compradores de conveniências, supermercados, distribuidoras de bebidas, farmácias, logística e órgãos públicos. Compram equipamento caro, comparam fornecedores e muitos chegam pelo celular. Eles querem **confiança técnica, porte de fábrica e resposta rápida**, não estética de startup.

**Ação principal da página:** pedir orçamento (formulário em 2 etapas ou WhatsApp).

## REGRA 1 (INEGOCIÁVEL): AS CORES SÃO AS DO SITE ATUAL

Extraí as cores direto do CSS do site atual (jdcamarasfrias.com.br) e do logo. **Use somente estas cores de marca.** Você pode criar tons derivados (mais claro/escuro do mesmo matiz) apenas para estados de hover, bordas e fundos suaves, e deve declarar cada derivado no token com um comentário dizendo de qual cor veio. **Proibido** introduzir roxo, rosa, laranja, vermelho ou qualquer matiz novo como cor de marca.

| Token | Hex | Origem no site | Papel no DS |
|---|---|---|---|
| `--jd-azul` | `#4181BC` | cor primária global do site | Cor de marca, ícones, linhas, elementos grandes. **Não usar como texto pequeno sobre branco (contraste 4,1:1).** |
| `--jd-marinho` | `#3B497F` | cor secundária global | Títulos, texto de destaque, fundos escuros de seção. Contraste 8,6:1 sobre branco. |
| `--jd-ciano` | `#37B4CE` | cor de destaque global; botão "Saiba mais" | Destaque, hover, detalhes sobre fundo escuro. Sobre branco só em elementos grandes (2,5:1). |
| `--jd-ciano-logo` | `#00B0F8` → `#00E0F0` | gradiente do "JD" no logo | Usar **só** para o selo/gradiente do logo e no máximo 1 detalhe gráfico por tela. |
| `--jd-royal` | `#1700BC` | botão "ORÇAMENTO" atual do cabeçalho | Estado de ação principal no cabeçalho. Contraste 11,9:1 com texto branco. |
| `--jd-amarelo` | `#F1BD43` | cor de acento do site | Destaque e CTA secundário. **Sempre com texto `#101010`** (11:1); nunca texto branco sobre amarelo. |
| `--jd-verde` | `#008749` | ícone do widget de contato (WhatsApp) | Confirmação e botão WhatsApp. Texto branco (4,6:1). |
| `--jd-preto` | `#101010` | texto "CÂMARAS" do logo | Texto principal sobre claro. |
| `--jd-grafite` | `#1D1D1D` | fundos escuros do site | Fundos escuros. |
| `--jd-noite` | `#12111F` | fundo escuro do hero atual (medido no print) | Fundo escuro de seção, mesmo tom do hero do site. |
| `--jd-cinza-texto` | `#737373` | texto padrão do site | Texto de apoio. Contraste 4,7:1 sobre branco. |
| `--jd-cinza-aco` | `#9CADC2` | cinza-azulado do site | Bordas, ícones inativos, texto sobre escuro. |
| `--jd-gelo` | `#EBEEF5` | fundo claro do site | Fundo de seções alternadas. |
| `--jd-cinza-claro` | `#F5F5F5` | fundo claro do site | Fundo de cards. |
| `--jd-borda` | `#D8DDE3` | borda do site | Bordas e divisores. |
| `--jd-branco` | `#FFFFFF` | — | Fundo e texto sobre escuro. |

Regras de uso das cores:
1. **Um único CTA principal por dobra.** Escolha entre o verde (WhatsApp) e o amarelo (orçamento) por dobra, nunca os dois lado a lado com o mesmo peso. Defina no DS qual é o CTA principal global (sugestão: amarelo com texto preto para "Pedir orçamento", verde só para o ícone/botão de WhatsApp) e justifique em 2 linhas no README.
2. Todo par texto/fundo precisa de **contraste AA** (4,5:1 para texto normal, 3:1 para texto grande e componentes de interface). Inclua no showcase uma matriz de contraste dos pares permitidos e marque os proibidos (ex.: branco sobre amarelo, azul `#4181BC` pequeno sobre branco).
3. O gradiente ciano do logo **não** vira fundo de seção, nem botão, nem blob decorativo.

## REGRA 2: LIBERDADE CRIATIVA TOTAL NO RESTO

Fora das cores, **você decide**: tipografia, grid, formas, ícones, ilustração, movimento, textura, layout dos componentes. Quero um resultado **marcante e memorável**, que um comprador de câmara fria perceba como "fábrica séria, tecnologia de refrigeração, entrega rápida". Evite o genérico de template de landing page.

A fonte atual do site é Montserrat (corpo) com uma fonte de display pesada nos títulos do banner. Você pode manter Montserrat no corpo ou trocar, desde que tudo venha de **Google Fonts ou fonte local**, com no máximo **2 famílias e 3 pesos no total**, com `font-display: swap`.

### Referências (pasta Inspirações, anexadas)

Use como **repertório, não como cópia**. Meu critério de leitura de cada uma:

- **SABLE (Archivo, peso pesado em caixa alta, grid editorial, preto e osso):** referência de **peso tipográfico e rigor de grid**. Pegue a ideia de título industrial, forte e sem enfeite.
- **IX-7 Mission (Rajdhani + IBM Plex Mono, rótulos técnicos, painel de dados):** referência de **ficha técnica**. Pegue o tratamento de rótulos, valores e unidades (kcal/h, °C, m, V, kg) para o componente de especificação.
- **Moveflux (cards claros, anéis de progresso, dados com ícone):** referência de **card de produto com dados** e de números em destaque.
- **Aurora Garden (tiles de cor saturada, cantos grandes, vidro leve):** referência para a **faixa de provas** em blocos de cor sólida, usando só as cores da tabela acima.
- **Otto (palco de cor única, produto 3D no centro, muito respiro):** referência para o **hero da LP B**, com a câmara fria como protagonista sobre um fundo de cor sólida de marca.
- **Clarix, Hanzo, GenLabs, Noema, Sonic.Link, Lando Norris, Lumina, Fluxora, Auragen, Sora, Terrasprint, Barbershop, Developer Monetization:** olhe todas. Use só ideias pontuais de microinteração, transição e acabamento. **Não herde** o clima "SaaS de IA", neon, blobs de gradiente, glassmorphism pesado ou roxo/rosa. O público é industrial/comercial e masculino 40+.

Antes de decidir a direção visual, escreva em 5 linhas (no topo do README) qual conceito você escolheu e de quais referências tirou o quê.

### Ideias de conceito (você pode escolher uma ou propor outra)
- "Chão de fábrica de precisão": tipografia pesada, números grandes, rótulos técnicos, linhas finas de projeto (planta/cota), pouco enfeite.
- "Frio em movimento": detalhes de gelo/frost em linhas finas e flocos geométricos sutis, só como acento, nunca como cenário pesado.
- Cuidado: nada de pinguim, urso polar ou clip-art de gelo.

## ESCOPO TÉCNICO

- **HTML + CSS + JS puros**, mobile-first, sem Elementor, sem WordPress, sem framework. Tailwind via CDN **não** (produção precisa ser leve). Pode usar CSS puro com variáveis.
- Metas: **LCP < 2,5 s no mobile, CLS ≈ 0**, imagens em WebP/AVIF com `width`/`height`, `loading="lazy"` fora da primeira dobra, sem biblioteca de JS acima de 30 kB. Ícones em **SVG inline** de um único estilo (linha), nada de Font Awesome inteiro.
- Acessibilidade: foco visível, alvos de toque ≥ 44 px, `prefers-reduced-motion` respeitado, HTML semântico, labels em todos os campos.
- Breakpoints: 360, 768, 1024, 1280. Teste mentalmente em 360 px de largura.
- **Camada de efeitos separada:** todo efeito de movimento ou decoração vai em `effects.css` / `effects.js`, **desligado por padrão** (classe `.fx` no `<body>` liga). A LP A não usa; a LP B usa. Assim o mesmo DS serve às duas.

## ESTRUTURA DE ARQUIVOS (entregue exatamente assim)

```
/ds-jd-camaras
  design-system.html      ← página de showcase com TUDO
  /css  tokens.css  base.css  components.css  effects.css
  /js   ds.js  effects.js
  /assets  logo placeholder, ícones SVG, imagens placeholder (cinza com rótulo)
  README.md               ← conceito, regras, tabela de tokens, contraste, do/don't
```

## TOKENS (tokens.css, CSS variables)

Cores (tabela acima), tipografia (família, pesos, escala fluida com `clamp()`: 12/14/16/20/28/40/56+), espaçamento (base 8 px), **um único raio de borda** (defina), sombras (máx. 2 níveis), bordas, z-index, durações e easing de animação, largura máxima de container.

## COMPONENTES (components.css) — cada um com variantes e estados (normal, hover, foco, desabilitado, erro quando couber)

1. **Botões:** primário (amarelo + texto preto), WhatsApp (verde + texto branco, com ícone), secundário (contorno), link com seta.
2. **Cabeçalho enxuto:** logo + botão "Pedir orçamento". Sem menu de site. Versão fixa ao rolar no mobile.
3. **Hero A** (título + 3 provas curtas + formulário na tela) e **Hero B** (foto/ilustração da câmara + CTA).
4. **Formulário em 2 etapas:** etapa 1 (nome + WhatsApp); etapa 2 (tipo de câmara, medida aproximada opcional, cidade/UF, o que vai armazenar). Indicador de etapa, máscara de telefone BR, validação inline, estado de sucesso, estado de erro. **Sem** campo de energia, **sem** dois telefones. Inclua campos ocultos para `utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `gclid` preenchidos por `ds.js` a partir da URL.
5. **Card de produto:** mini câmara, expositora/walk-in, resfriados, congelados. Foto, uso ideal, faixa de temperatura, botão.
6. **Ficha técnica** (tabela de especificação): dimensões, kcal/h, tensão, potência, peso, garantia. **Valores placeholder marcados** (ver regra de conteúdo).
7. **Faixa de provas** (3 a 4 números/argumentos) com placeholders.
8. **Passo a passo** (projeto, fabricação, entrega, instalação, suporte) horizontal no desktop, vertical no mobile.
9. **Galeria de obras** (grid de 6 a 9 fotos, com lightbox simples sem biblioteca).
10. **Depoimento** (nome + empresa + cidade; variante "sem foto").
11. **Faixa de logos de clientes** (placeholders).
12. **FAQ** em acordeão acessível.
13. **CTA final** com formulário.
14. **Rodapé:** razão social, CNPJ, endereço, telefone, links de privacidade.
15. **Botão flutuante de WhatsApp** (mobile) e **banner de cookies** leve (3 botões: aceitar, recusar, ajustar), **sem bloquear** a medição de conversão (preparado para Consent Mode v2).
16. **Selos/chips** ("Projeto sob medida", "Chave na mão", "Instalação inclusa") e **aviso de estado** (sucesso/erro/info), usando só as cores da tabela.

## REGRAS DE CONTEÚDO (anti-invenção)

- **Não invente** números, anos de mercado, quantidade de obras, selos, prêmios, depoimentos, nomes de clientes, certificações ou preços. Use placeholders **visivelmente marcados**: fundo hachurado ou etiqueta `[CONFIRMAR]`, texto tipo `00 anos`, `Nome do cliente`, `Empresa`.
- Claims que o cliente **ainda não validou** e portanto **não podem aparecer** em nenhum exemplo: "supercongelados -125 °C", "entregamos em todo o Brasil", "garantia de 5 anos", "a mais famosa do Brasil". Se precisar de um exemplo, use `[CONFIRMAR]`.
- Rodapé: razão social e CNPJ como **placeholder** (`[RAZÃO SOCIAL]`, `[CNPJ]`); o CNPJ correto ainda será confirmado.
- Telhas térmicas **não** entram. Só câmaras frias.
- Textos de exemplo em **português do Brasil**, tom direto e técnico, sem exagero de marketing.
- Imagens: placeholders cinza com o rótulo do que vai ali (ex.: "Foto de obra: câmara instalada em supermercado"). Não use imagens de banco que simulem obra real da JD.

## COMO TRABALHAR (importante)

1. Antes de gerar qualquer componente, confirme internamente: "essa cor está na tabela? isso é decisão do DS ou herdei de uma referência sem adaptar?"
2. Se faltar algo para um componente (ex.: não tenho foto, não tenho ícone), **não invente**: use placeholder marcado e liste a pendência no README, na seção "Pendências do cliente".
3. Não crie tokens ou componentes além dos listados sem avisar. Se achar que falta algum, proponha no final, separado, sem implementar.
4. Entregue o `design-system.html` navegável, com menu lateral por seção (Cores, Tipografia, Espaçamento, Botões, Formulário, Cards, etc.), mostrando **cada componente em versão mobile (360 px) e desktop**.
5. No final, rode uma autoverificação e escreva no README: (a) lista de cores usadas e confirmação de que todas estão na tabela, (b) matriz de contraste, (c) peso estimado do CSS+JS, (d) o que ficou como placeholder.

## ENTREGA

Devolva a pasta completa com a estrutura acima. No fim da resposta, liste em até 8 linhas: o conceito escolhido, as 3 decisões visuais mais importantes e o que você recomenda eu revisar primeiro.
