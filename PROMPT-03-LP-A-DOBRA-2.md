# PROMPT 03 — LP A (direta) · Dobra 2: "Por que a JD" (Antigravity)

> Como usar: no mesmo projeto, **depois** de aplicar o Prompt 02b. Cole tudo abaixo da linha. Devolva o `index.html` completo e cumulativo, mais `css/` e `js/` atualizados.

---

## CONTEXTO

Continuamos a **LP A da JD Câmaras Frias**, dobra por dobra. A Dobra 1 (cabeçalho + hero com formulário) está aprovada. Agora vem a **Dobra 2**, logo abaixo do hero: três argumentos curtos que respondem ao medo do comprador ("e se a câmara vier do tamanho errado, ou eu ficar sem instalação e sem suporte?").

Estrutura da LP A: 1. Hero + formulário ✅ · **2. Por que a JD ← esta etapa** · 3. Produtos · 4. Como funciona · 5. Obras · 6. FAQ + CTA final + rodapé.

## REGRAS INEGOCIÁVEIS

1. **Não altere nada da Dobra 1** (HTML, classes, textos, ordem no mobile, comportamento do formulário). Devolva o arquivo cumulativo com a Dobra 1 idêntica. Se algo da Dobra 1 precisar mudar, **avise no final em vez de mudar**.
2. Use **somente o DS** (`tokens.css`, `base.css`, `components.css`). **Não crie tokens, cores, componentes ou variantes novos.** Pode usar `.jd-section`, `.jd-container`, `.jd-passos`/`.jd-passo`, `.jd-btn--primary` e as classes de tema já existentes. Se faltar algo, use o mais próximo e liste em "O que faltou no DS", sem implementar.
3. **Use a copy exatamente como está abaixo.** Não reescreva, não "melhore", não adicione claims.
4. **Tema claro** nesta dobra (`.tema-claro`: fundo `--jd-branco` ou `--jd-gelo`, títulos `--jd-marinho`, texto `--jd-cinza-texto` / `--jd-preto`). Sem `effects.css` e sem `effects.js`.
5. Nenhum texto abaixo de **12 px**. Nenhum estilo inline novo: use classes/tokens do DS.
6. Mobile-first. Teste em 360, 390, 768 e 1280. **Sem rolagem horizontal.**
7. **Proibido aparecer** (nem como exemplo): "supercongelados -125 °C", "entregamos em todo o Brasil", "a mais famosa do Brasil", "garantia de 5 anos", ABNT, Anvisa, patente, Inmetro, selo, certificação, norma, "fábrica", "fabricação própria", prazos em dias, prazo de resposta, preço ou "a partir de".

## ENTREGA: DOBRA 2

### Estrutura

```html
<section class="jd-section tema-claro" id="porque-jd" aria-labelledby="porque-title">
  <div class="jd-container"> ... </div>
</section>
```
Posição: imediatamente depois da `</section>` do hero (Dobra 1), dentro do `<main>`.

### Copy definitiva

- **Eyebrow:** `POR QUE A JD`
- **Título (H2, `id="porque-title"`):** `Do projeto à câmara funcionando, com um fornecedor só`

**Card 1**
- Título: `Projeto sob medida`
- Texto: `A câmara é dimensionada para o que você vai guardar e para o espaço que você tem.`

**Card 2**
- Título: `Entrega e instalação`
- Texto: `A equipe da JD entrega e monta a câmara no seu local.`
- Etiqueta pequena ao lado do título, usando o componente de etiqueta já existente (`.tag-exemplo` ou `.jd-chip--amarelo`): `[CONFIRMAR]` — com o comentário HTML `<!-- CONFIRMAR: instalação feita pela equipe própria da JD? -->`

**Card 3**
- Título: `Suporte depois da obra`
- Texto: `Ampliação, manutenção e correção com quem montou a sua câmara.`

**CTA abaixo dos cards**
- Botão `.jd-btn--primary`: `Pedir orçamento` (com a seta do DS), que **rola suavemente até `#form-lead`** e foca o primeiro campo do formulário (`#lp-field-nome`) sem fazer a página saltar.
- Texto de apoio abaixo do botão (12 px, `--jd-cinza-texto`): `Sem compromisso. A JD chama você no WhatsApp para entender o seu projeto.`

### Componente e visual

- Use `.jd-passo` / `.jd-passos` como base dos 3 cards (ícone + título + descrição). **Sem número** (estes não são passos). Se o `.jd-passo` só existir com número visível, esconda o número pela classe/modificador existente; se isso não for possível sem criar classe nova, use o `.jd-passo` com número e **liste em "O que faltou no DS"**. **Não invente classe.**
- Ícones em **SVG inline**, estilo linha (stroke 1.5–2, `currentColor`), coerentes com os que já existem no DS (`ds-jd-camaras/assets/icons.svg`). Sugestão: régua/esquadro (projeto sob medida), caminhão ou chave (entrega e instalação), escudo ou chave inglesa (suporte). Se não existir um ícone adequado no DS, desenhe um simples no mesmo estilo e liste em "O que faltou no DS".
- Layout: **3 colunas no desktop (≥1024)**, **1 coluna empilhada no mobile e no tablet**, com espaçamento do DS. Alturas dos cards iguais no desktop.
- A dobra deve ser **curta**: no mobile, no máximo uma tela e meia de altura (390 × 844). Sem imagem de fundo, sem animação, sem efeitos.

### Tracking e acessibilidade

- Ao clicar em `Pedir orçamento` desta dobra, envie `dataLayer.push({ event: 'click_cta_porque', lp_version: 'A', titulo_variante: <valor atual> })`. Documente no README, junto à tabela de eventos existente.
- Hierarquia de títulos: o H1 está no hero; esta dobra usa H2; os títulos dos cards usam H3.
- Contraste AA nos pares usados. Alvo de toque do botão ≥ 44 px, foco visível. Respeite `prefers-reduced-motion` na rolagem suave (sem animação se reduzido).

## AUTOVERIFICAÇÃO (README, seção "Dobra 2")

1. A Dobra 1 foi alterada? (deve ser **não**; compare o HTML do hero antes/depois e diga se há diferença).
2. Classes e componentes do DS usados e confirmação de que **nenhum token ou componente novo** foi criado.
3. Busca por hex ou `rgb()` fora do DS e por `font-size` abaixo de 12 px nesta dobra (zero).
4. Busca pelos termos proibidos (zero fora de `[CONFIRMAR]`).
5. Rolagem horizontal em 360 / 390 / 768 / 1280.
6. Altura da dobra em px em 390 × 844 e em 1280 × 800.
7. Tabela de eventos do dataLayer atualizada (inclui `click_cta_porque`).
8. Placeholders pendentes (lista atualizada) e **O que faltou no DS**.

No final da resposta, em até 4 linhas: o que foi entregue, o que ficou pendente e qualquer decisão sua que eu deva revisar.
