# PROMPT 01c — Ajustes finais do DS da JD Câmaras Frias (Antigravity)

> Como usar: no mesmo projeto, cole tudo abaixo da linha. Ao terminar, traga o `design-system.html` atualizado (e a pasta `ds-jd-camaras`, incluindo `assets/logo-jd.png`) para eu validar. Esse é o último ajuste antes da LP.

---

O DS está aprovado no conceito, no tema claro/escuro e nas 2 famílias de fonte. Faça **somente os 6 ajustes abaixo**. Não altere mais nada: nomes de classes, tokens, componentes e textos não citados ficam exatamente como estão. Se um ajuste quebrar outro componente, avise no final.

## AJUSTE 1: Cabeçalho (o mais importante)

Hoje o cabeçalho do showcase mistura navegação interna do catálogo com o componente "Cabeçalho enxuto". Separe os dois.

1. **Componente `Cabeçalho da LP`** (é o que vai para a LP): somente **logo + botão "Pedir orçamento"** (amarelo, texto `#101010`). Altura **64 px no mobile e 72 px no desktop**, uma linha, sem quebra, sem menu, sem chips. Fixo ao rolar, com sombra leve só depois que rolar.
2. **Barra do showcase** (só do `design-system.html`, nunca vai para a LP): mantenha "Visão geral" e "Catálogo técnico", mas em uma **barra separada, discreta, acima do cabeçalho, em fonte 12 px, que rola junto com a página (não é fixa)**. Remova dela o chip **"Mobile 360px"**, os chips de temperatura e o mostrador "Núcleo: -18,0 °C".
3. Troque o texto "Catálogo técnico (22 módulos)" por **"Componentes"**. Troque "Visão geral (experiência)" por **"Visão geral"**.
4. Os chips de temperatura e o mostrador de núcleo, se quiser manter, passam a ser um **componente próprio chamado "Faixa de temperatura"** dentro do hero escuro (não no cabeçalho), em uma única linha rolável no mobile.
5. **Corrija a rolagem horizontal em 390 px** (hoje `scrollWidth > innerWidth`). Descubra qual elemento estoura (provavelmente a barra de navegação e os chips) e conserte. Teste em 360, 390, 768 e 1280. Entregue sem rolagem horizontal em nenhuma.
6. Logo: `assets/logo-jd.png` ainda não existe. Use `jd-logo-site-atual.png` (anexado antes) copiado para essa pasta com esse nome. Mantenha o fallback em texto, mas o fallback deve usar `--jd-branco` com "JD" e "CÂMARAS FRIAS", **sem** o ciano `#00E0F0`.

## AJUSTE 2: Remover claims regulatórios sem etiqueta

1. Na faixa de provas, remova **"100% PADRÃO ABNT E ANVISA"**. Em seu lugar, use um terceiro item de prova em placeholder: `[CONFIRMAR]` com a etiqueta `EXEMPLO`, texto: "Selo / norma a confirmar pelo cliente".
2. Procure no arquivo inteiro e remova (ou troque por `[CONFIRMAR]` com a etiqueta `EXEMPLO`) qualquer menção a: **ABNT, Anvisa, certificado/certificados, norma, patente, retardante, Inmetro, selo**.
3. Mantenha a regra da etiqueta `EXEMPLO` + comentário `<!-- EXEMPLO: não reutilizar na LP -->` em todo número ou claim de exemplo.

## AJUSTE 3: Descrição técnica construtiva (não afirmar o que a JD não confirmou)

Reescreva a descrição da seção "Veja por dentro: como a câmara é montada" e os rótulos do desenho em **linguagem genérica e marcada como a confirmar**. Troque:

- "Estrutura industrial com chapas de aço galvanizado pré-pintado na cor branca, núcleo isolante com encaixe macho-fêmea estanque e porta frigorífica semi-embutida com batente aquecido." →
  "Painéis isolantes que se encaixam, porta frigorífica e equipamento de refrigeração, montados sob medida para o seu espaço. `[CONFIRMAR: material do painel, espessura e tipo de porta com a fábrica]`"
- Rótulos do desenho: "Núcleo termoisolante de alta densidade" → **"Painel isolante"**; "Evaporador dual-fan ativo" → **"Unidade de refrigeração"**; "Porta semi-embutida + resistência" → **"Porta frigorífica"**.
- "Painéis certificados com montagem precisa e proteção térmica completa." → "Montagem feita pela equipe da JD, com instalação inclusa. `[CONFIRMAR]`"
- Também troque, nos textos de exemplo de todo o arquivo: "Projeto, fabricação e montagem própria" → **"Projeto sob medida, entrega e instalação"**.
- As 4 abas do raio-X ficam, com os novos nomes: "1. Vista geral", "2. Painéis", "3. Refrigeração", "4. Porta".

## AJUSTE 4: Cores fora da tabela

1. **Alerta de erro** (`#FDE8E8`, `#F5C6CB`, `#721C24`): substitua por um bloco com fundo `--jd-gelo`, borda esquerda de 4 px em `--jd-royal` (`#1700BC`), texto `--jd-preto` e ícone "!" em `--jd-royal`. O erro deve ser comunicado por **ícone + texto**, não só por cor.
2. **`#E0E5EC`** (placeholders de galeria e outros): troque por `--jd-gelo` (`#EBEEF5`) ou `--jd-borda` (`#D8DDE3`).
3. **`#252528`** (fundo do bloco do raio-X): troque por `--jd-grafite` (`#1D1D1D`).
4. Os derivados de hover (`#3671A8`, `#2D3863`, `#E5AE2E`) **podem ficar**, mas confirme que estão declarados em `tokens.css` com comentário de origem.
5. Rode a busca final por hex e `rgb()/rgba()` fora da tabela e registre o resultado no README (deve ser zero, além dos derivados declarados).

## AJUSTE 5: WhatsApp e dados de contato

1. O link `https://wa.me/5532999999999` é um número falso. Troque **todas** as ocorrências por **`https://wa.me/[WHATSAPP]`** e deixe uma constante única em `ds.js`: `const WHATSAPP_NUMBER = ''; // TODO: preencher com DDI+DDD+número (ex.: 5562900000000)`.
2. Se `WHATSAPP_NUMBER` estiver vazio, os botões de WhatsApp devem aparecer **desabilitados** (`aria-disabled="true"`) com a etiqueta `[CONFIRMAR NÚMERO]`, para ninguém publicar com número errado.
3. Telefone, e-mail, endereço, razão social e CNPJ no rodapé: todos como placeholder `[...]`.

## AJUSTE 6: Hero escuro (só detalhes)

1. A estatística "**100%**" ficou isolada em uma segunda linha e quebra o alinhamento. Com o ajuste 2 ela sai. Garanta que a faixa de provas do hero fique em **3 itens na mesma linha no desktop** e em coluna no mobile, com alinhamento consistente.
2. O botão "Chamar no WhatsApp" tem um círculo (radar) à esquerda que parece um ícone quebrado. Troque por **o ícone do WhatsApp em SVG inline** (linha, cor `--jd-branco`), mantendo o efeito de radar apenas como anel sutil atrás do ícone.

## AUTOVERIFICAÇÃO (no README, seção "Verificação 01c")

1. Rolagem horizontal em 360 / 390 / 768 / 1280: sim ou não.
2. Altura do cabeçalho da LP em mobile e desktop.
3. Resultado da busca por ABNT, Anvisa, certificad, norma, patente, retardante, Inmetro, selo (deve ser zero fora de `[CONFIRMAR]`).
4. Resultado da busca por hex/rgb fora da tabela.
5. Ocorrências de `wa.me/5532999999999` (deve ser zero).
6. Lista final de blocos marcados `EXEMPLO`.

No final da resposta, liste em até 5 linhas o que mudou e qualquer ajuste que não foi possível.
