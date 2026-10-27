# PROMPT 02b — Ajustes da Dobra 1 (LP A)

> Como usar: no mesmo projeto, cole tudo abaixo da linha. Anexe `logo-jd-branco.png` (versão do logo para fundo escuro). Depois traga o `index.html`, `css/`, `js/` e `assets/` atualizados.

---

A Dobra 1 está aprovada na copy, nos títulos dinâmicos, no formulário e nos eventos. Faça **somente os 5 ajustes abaixo**, sem mexer em copy, classes ou componentes que não foram citados.

## AJUSTE 1: Logo invisível no fundo escuro

O logo atual (`assets/logo-jd.png`) tem o texto "CÂMARAS" em `#101010`. Sobre o hero escuro (`--jd-noite`) ele some. Veja o cabeçalho em 390 px e em 1280 px.

1. Salve o arquivo anexado `logo-jd-branco.png` em `assets/logo-jd-branco.png`.
2. No **cabeçalho da LP** (fundo escuro), use `logo-jd-branco.png`. Mantenha `width="168" height="38"` e o `alt`.
3. O fallback em texto (`onerror`) deve continuar existindo e usar `--jd-branco`.
4. Mantenha `assets/logo-jd.png` (versão escura) no projeto, para as dobras de tema claro e o rodapé claro que virão depois.
5. Favicon: continue com o que está, não troque agora.

## AJUSTE 2: Formulário 100% visível na primeira tela do mobile

Hoje, em 390 × 844, o título "Peça o seu orçamento" começa em ~604 px e o botão "Continuar" termina em ~1020 px. Só o campo "Seu nome" aparece. **Meta: o botão "Continuar" visível por inteiro em 390 × 844 e em 360 × 740.**

Faça isto, nesta ordem de prioridade, parando quando bater a meta:
1. **Ordem no mobile:** eyebrow → H1 → **formulário** → (depois) subtítulo, chips de temperatura, botão WhatsApp, 3 provas e imagem. No desktop, mantenha o layout atual (texto à esquerda, formulário à direita).
2. No mobile, **reduza o espaçamento vertical** entre eyebrow, H1 e formulário (hoje há ~180 px de espaço só entre H1 e subtítulo). Use os tokens de espaço menores do DS.
3. Reduza o H1 no mobile para a escala do DS imediatamente menor, se ainda faltar espaço.
4. Na etapa 1, oculte o texto "Leva menos de 1 minuto." e esconda o indicador de etapas (mostre-o a partir da etapa 2).
5. **Não esconda nem corte nenhum texto da copy** (o subtítulo e os chips apenas passam para depois do formulário).

Depois de ajustar, **meça de verdade** com `getBoundingClientRect()` em 360 × 740 e 390 × 844, no estado inicial (sem rolar) e escreva os números reais no README. O README atual diz que o botão está em 782–830 px, e isso **não bate** com o arquivo entregue (medi ~971–1020 px). Corrija o README com a medição nova.

## AJUSTE 3: Tamanho mínimo de texto (12 px)

Há textos de **11 px**: eyebrow, `EXEMPLO`, rótulos "ETAPA 1/2", "Largura (m)", "Comprimento (m)", "Altura (m)", ajuda das medidas e microcopy de privacidade. Suba **todos** para no mínimo **12 px** (eyebrow pode ficar 12 px em caixa alta com `letter-spacing` do DS). Troque os `style="font-size:11px"` inline por classes/tokens do DS ou por uma classe utilitária já existente. Confirme com uma busca por `font-size` abaixo de 12 px em HTML e CSS (resultado esperado: zero).

## AJUSTE 4: WhatsApp sem número

Hoje, sem número, os botões de WhatsApp só rolam até o formulário e **não** mostram a etiqueta `[CONFIRMAR NÚMERO]`. Isso pode ir ao ar sem ninguém perceber. Ajuste:
1. Com `WHATSAPP_NUMBER` vazio, o botão do hero **continua rolando até o formulário** (comportamento bom para produção), mas **em `?debug=1`** ele mostra a etiqueta `[CONFIRMAR NÚMERO]` e imprime no console um aviso `⚠ WHATSAPP_NUMBER vazio`.
2. Com número preenchido, abre `https://wa.me/<número>?text=<mensagem>` e dispara `click_whatsapp`.
3. Marque no README, na lista de pendências, que **a LP não pode ir ao ar sem o número**.

## AJUSTE 5: Confirmar o item "12 anos" (apenas documentar)

A prova "12 anos — de experiência" está na página. **Não mude o texto.** No README, em "Placeholders pendentes", registre: `12 anos de experiência: confirmar com o cliente se são 12 anos de CNPJ ou de atuação no setor, antes de ir ao ar.`

## AUTOVERIFICAÇÃO (README, seção "Verificação 02b")

1. Posição real (px) do topo e da base do botão "Continuar" em 360 × 740 e 390 × 844, estado inicial.
2. Confirmação de que o logo do cabeçalho é legível sobre `--jd-noite` (diga qual arquivo está em uso).
3. Busca por `font-size` < 12 px: resultado.
4. Teste de `?debug=1` sem número de WhatsApp: o que aparece.
5. Rolagem horizontal em 360 / 390 / 768 / 1280.
6. Comparação do layout desktop (1280 × 800) antes e depois: **não pode mudar**.

No final, em até 4 linhas: o que mudou e qualquer ajuste que não foi possível.
