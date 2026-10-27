# PROMPT 04 — Correções (Dobras 1 e 2) + Dobra 3: Produtos (LP A)

> Como usar: no mesmo projeto, cole tudo abaixo da linha. Devolva `index.html` cumulativo, `css/`, `js/` e `README.md`. O Prompt tem 2 partes: **PARTE A (correções)** e **PARTE B (Dobra 3)**. Faça a A primeiro, confirme que funcionou, e só depois a B.

---

## REGRAS INEGOCIÁVEIS (valem para as duas partes)

1. Use **somente o DS** (`tokens.css`, `base.css`, `components.css`). **Não crie tokens, cores, componentes ou variantes novos.** Se faltar algo, use o mais próximo e liste em "O que faltou no DS".
2. **Use a copy exatamente como está.** Não reescreva nem adicione claims.
3. Sem `effects.css`/`effects.js`. Nenhum texto abaixo de **12 px**. Mobile-first; teste em 360 × 740, 390 × 844, 768 e 1280; **sem rolagem horizontal**.
4. **Proibido aparecer** (nem como exemplo): "supercongelados -125 °C", "entregamos em todo o Brasil", "a mais famosa do Brasil", "garantia de 5 anos", ABNT, Anvisa, patente, Inmetro, selo, certificação, norma, "fábrica", "fabricação própria", prazos em dias, prazo de resposta, preço ou "a partir de".

---

# PARTE A — CORREÇÕES

## A1. Os botões "Pedir orçamento" não rolam até o formulário no mobile (BUG)

No mobile, `#form-lead` usa `display: contents` (para reordenar o formulário antes do subtítulo). Elemento com `display: contents` **não tem caixa**, então `scrollIntoView` e a âncora `href="#form-lead"` não rolam. Resultado medido em 390 × 844: com a página rolada até a Dobra 2, tanto o botão do cabeçalho (`#cta-header`) quanto o da Dobra 2 (`#cta-porque-jd`) **não movem a tela**. No desktop funcionam.

Corrija:
1. Todos os atalhos para o formulário (`#cta-header`, `#cta-porque-jd` e os futuros) passam a rolar até o **elemento do formulário que tem caixa**: `#lp-form-lead` (o `<form>`). Troque `href="#form-lead"` por `href="#lp-form-lead"` e o `getElementById('form-lead')` por `getElementById('lp-form-lead')`.
2. Crie uma única função `irParaFormulario()` em `lp.js` usada por todos os CTAs: rola (suave, ou instantâneo se `prefers-reduced-motion`), **compensando a altura do cabeçalho fixo** (64 px mobile / 72 px desktop) com `scroll-margin-top` no `#lp-form-lead` usando o token de espaço do DS + a altura do cabeçalho, e depois foca `#lp-field-nome` com `preventScroll: true` (se estiver na etapa 1) ou o primeiro campo da etapa ativa.
3. Se o formulário já estiver visível na tela, não role: só foque.
4. **Teste obrigatório, com a página rolada até a Dobra 2**, em 390 × 844 e em 1280 × 800: clicar em `#cta-header` e em `#cta-porque-jd` e medir `getBoundingClientRect().top` do `#lp-field-nome` (deve ficar entre 80 px e 300 px) e `document.activeElement.id === 'lp-field-nome'`. Escreva os números no README.

## A2. O botão "Chamar no WhatsApp" sumiu do hero

O Prompt 02 pedia o botão verde "Chamar no WhatsApp" no hero. Ele não está mais no HTML do hero (só no estado de sucesso). **Restaure-o** com o mesmo markup de antes, `data-whatsapp-btn`, ícone SVG e a mesma regra do número vazio.
- No **mobile**, posição: depois do formulário, junto dos chips de temperatura e das 3 provas (não pode empurrar o formulário para baixo; o botão "Continuar" deve continuar inteiro na primeira tela em 390 × 844 e 360 × 740).
- No **desktop**, volta para a coluna de texto, abaixo dos chips, como antes.

## A3. Estilos inline na Dobra 2

Há ~33 `style="..."` no arquivo, vários novos na Dobra 2 (cabeçalho centralizado, margens, CTA e texto de apoio). Troque os da **Dobra 2** por classes: use as utilitárias do DS se existirem; se não, uma classe de layout com prefixo `lp-` **só em `lp.css`** (arquivo novo, apenas para espaçamento e alinhamento usando tokens do DS, sem cores nem tipografia novas). Não mexa nos inline da Dobra 1 agora.

## A4. Não mude

Textos, hierarquia, ícones e layout da Dobra 2 estão aprovados. O formulário na primeira tela do mobile está aprovado (botão em 586–635 px em 390 × 844). Não altere.

---

# PARTE B — DOBRA 3: PRODUTOS

Posição: logo depois da Dobra 2, dentro do `<main>`.

```html
<section class="jd-section tema-claro" id="produtos" aria-labelledby="produtos-title"> ... </section>
```
Tema claro com fundo `--jd-gelo` (alterna com a Dobra 2, que é branca).

## Copy definitiva

- **Eyebrow:** `NOSSAS CÂMARAS`
- **Título (H2, `id="produtos-title"`):** `Qual câmara serve para o seu negócio?`

Use o componente **`.jd-card-produto`** do DS (imagem, nome, tipo, temperatura, uso, rodapé com botão), 4 cards:

| # | Nome (`__nome`) | Tipo (`__tipo`) | Temperatura (`__temp`) | Uso (`__uso`) |
|---|---|---|---|---|
| 1 | `Mini câmara` | `Para espaço pequeno` | `[CONFIRMAR faixa]` | `Para quem tem pouco espaço e precisa de frio.` `[CONFIRMAR dimensões e uso]` |
| 2 | `Câmara expositora (walk-in cooler)` | `Para produtos à vista do cliente` | `[CONFIRMAR faixa]` | `Para bebidas e produtos que ficam à vista do cliente.` `[CONFIRMAR formato]` |
| 3 | `Câmara de resfriados` | `Produtos que não podem congelar` | `0 a +15 °C` | `Para hortifrúti, laticínios, bebidas e produtos que não podem congelar.` |
| 4 | `Câmara de congelados` | `Alimentos congelados` | `-18 °C` | `Para carnes, sorvetes e alimentos congelados.` |

- Os trechos `[CONFIRMAR ...]` aparecem como etiqueta visível (componente `.tag-exemplo` ou `.jd-chip--amarelo`) + comentário HTML `<!-- CONFIRMAR: ... -->`.
- **Não cite farmácia, medicamentos ou vacinas nos cards** (faixa 0 a +15 °C não serve a vacinas e não queremos prometer nada regulatório).
- Imagem de cada card: placeholder do DS (`assets/placeholder-camara.svg` ou o componente `.hero-img-placeholder`) com o rótulo `Foto: <nome do card>`, `width`/`height` definidos, `loading="lazy"`. Sem foto de banco.
- **Botão de cada card (`.jd-btn--primary`, no rodapé do card):** `Pedir orçamento`.
- **Nota abaixo dos cards** (12 px mínimo, `--jd-cinza-texto`, centralizada): `Não achou a sua? Cada projeto é feito sob medida. Conte o que você precisa e a JD indica o tipo certo.`

## Comportamento dos botões dos cards

Ao clicar em `Pedir orçamento` de um card:
1. **Pré-selecione o tipo de câmara** no campo `#lp-field-tipo_camara`, mapeando: card 1 → `Mini câmara`; card 2 → `Câmara expositora (walk-in cooler)`; card 3 → `Câmara de resfriados (0 a +15 °C)`; card 4 → `Câmara de congelados (-18 °C)`. Se o usuário já escolheu outro tipo, **sobrescreva** com o do card clicado.
2. Use a função `irParaFormulario()` da correção A1 (rolar e focar).
3. Envie `dataLayer.push({ event: 'click_cta_produto', produto: '<mini|expositora|resfriados|congelados>', lp_version: 'A', titulo_variante: <valor atual> })`.
4. Se o formulário estiver na etapa 2 (ou já enviado com sucesso), apenas troque o select (e, no sucesso, não reabra o formulário).

## Layout

- **Mobile (<768):** 1 coluna. **Tablet (768–1199):** 2 colunas. **Desktop (≥1200):** 4 colunas se couberem com legibilidade; se os cards ficarem apertados (texto quebrando em muitas linhas), use 2 × 2 também no desktop. Alturas iguais por linha, rodapé (botão) alinhado na base.
- Sem carrossel, sem animação, sem efeitos.
- Altura total da dobra no mobile: informe no README (não precisa caber em uma tela).

## Acessibilidade

H2 da dobra, H3 no nome de cada card. Imagens placeholder com `alt` descritivo. Botões com 44 px de altura mínima e foco visível. Contraste AA.

---

## AUTOVERIFICAÇÃO (README, seções "Correções 04A" e "Dobra 3")

**Correções**
1. Medições do teste do A1: `#lp-field-nome` top e `activeElement` após clicar em `#cta-header` e `#cta-porque-jd`, rolando a página desde a Dobra 2, em 390 × 844 e 1280 × 800.
2. Posição (px) do topo e da base do botão "Continuar" em 360 × 740 e 390 × 844 **depois** de restaurar o WhatsApp (deve continuar inteiro visível).
3. Quantos `style="` restam na Dobra 2 (esperado: zero).

**Dobra 3**
4. Busca por hex/`rgb()` fora do DS e por `font-size` < 12 px (zero).
5. Busca pelos termos proibidos (zero fora de `[CONFIRMAR]`).
6. Rolagem horizontal em 360 / 390 / 768 / 1280.
7. Teste dos 4 botões dos cards: valor do `#lp-field-tipo_camara` depois do clique e evento disparado.
8. A Dobra 1 e a Dobra 2 foram alteradas além do pedido na Parte A? Compare antes/depois e diga.
9. Tabela de eventos do dataLayer atualizada (`click_cta_produto`).
10. Placeholders pendentes e **O que faltou no DS**.

No final da resposta, em até 5 linhas: o que foi entregue, o que ficou pendente e qualquer decisão sua que eu deva revisar.
