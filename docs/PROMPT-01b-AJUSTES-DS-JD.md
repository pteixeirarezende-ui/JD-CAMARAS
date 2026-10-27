# PROMPT 01b — Ajustes no DS da JD Câmaras Frias (Antigravity)

> Como usar: no mesmo projeto do DS, cole tudo abaixo da linha. Anexe de novo `jd-logo-site-atual.png` se ele pedir. Depois traga o `design-system.html` e a pasta `ds-jd-camaras` completas (CSS e JS junto) para eu revisar.

---

Gostei do conceito "Engenharia do Frio", do fundo de planta técnica, da vista isométrica em corte e do simulador de dimensionamento. **Mantenha esses três.** Agora faça **somente os ajustes abaixo**. Não mude estrutura de arquivos, nomes de classes nem componentes que não foram citados. Se algo que eu pedir quebrar outro componente, avise no final em vez de improvisar.

## AJUSTE 1: Cores travadas (volte para a tabela)

Use **apenas** estas cores de marca, vindas do site atual. Todo o resto deve ser removido ou convertido para o token mais próximo.

| Token | Hex |
|---|---|
| `--jd-azul` | `#4181BC` |
| `--jd-marinho` | `#3B497F` |
| `--jd-ciano` | `#37B4CE` |
| `--jd-ciano-logo` | `#00E0F0` (gradiente `#00B0F8` → `#00E0F0`) |
| `--jd-royal` | `#1700BC` |
| `--jd-amarelo` | `#F1BD43` (texto sempre `#101010`) |
| `--jd-verde` | `#008749` |
| `--jd-preto` | `#101010` |
| `--jd-grafite` | `#1D1D1D` |
| `--jd-noite` | `#12111F` |
| `--jd-cinza-texto` | `#737373` |
| `--jd-cinza-aco` | `#9CADC2` |
| `--jd-gelo` | `#EBEEF5` |
| `--jd-cinza-claro` | `#F5F5F5` |
| `--jd-borda` | `#D8DDE3` |
| `--jd-branco` | `#FFFFFF` |

Mudanças obrigatórias:
1. **Remova o verde neon `#00E676`** (todas as ocorrências, inclusive o "COMPRESSOR OK", os ✔ e o bloco "35% mais econômico"). Troque por `--jd-verde` (`#008749`) com texto branco, ou por `--jd-ciano` sobre fundo escuro quando for indicador de status.
2. **Remova o vermelho `#E53935`.** Para erro de formulário, use `--jd-royal` com ícone e texto explícito ("Preencha o WhatsApp"), nunca só cor. Para alerta, use `--jd-amarelo`.
3. **Remova os azuis escuros próprios** (`#171A29`, `#1C2442`, `#1E2845`, `#1A284A`, `#2A3554`, `#2D3863`, `#09080F`, `#0D0C17` e similares). Fundos escuros usam só `--jd-noite`, `--jd-grafite` e variações de opacidade desses dois. Se precisar de um tom intermediário, derive de `--jd-noite` e declare o derivado em `tokens.css` com comentário de origem.
4. **O ciano `#00E0F0` só pode aparecer em:** o logo e **no máximo um detalhe gráfico por tela**. Hoje ele aparece mais de 30 vezes. Para todo o resto (bordas, rótulos, ícones, hover, linhas do desenho isométrico), use `--jd-ciano` (`#37B4CE`) ou `--jd-azul` (`#4181BC`).
5. Rode uma busca no HTML e CSS por qualquer hex fora da tabela e por `rgb()`/`rgba()` que gere matiz novo. No README, confirme que não restou nenhum.

## AJUSTE 2: Claro e escuro, não só escuro

O DS inteiro está em tema escuro. O comprador (dono de conveniência, supermercado, distribuidora) precisa sentir "fábrica séria e acessível", não "painel de controle".

- Crie dois temas por seção, controlados por classe: **`.tema-claro`** (fundo `--jd-branco` / `--jd-gelo` / `--jd-cinza-claro`, títulos `--jd-marinho`, texto `--jd-preto` e `--jd-cinza-texto`, CTA amarelo com texto preto) e **`.tema-escuro`** (o atual, só com `--jd-noite` e `--jd-grafite`).
- **Regra de uso, registre no README:** o **hero e a seção do simulador/raio-X** podem ser escuros. **Todas as demais** (produtos, ficha técnica, provas, passo a passo, galeria, depoimentos, FAQ, CTA final, rodapé) usam o tema claro por padrão.
- Todos os componentes do catálogo precisam existir **nos dois temas**. No `design-system.html`, mostre cada um em claro e em escuro lado a lado.
- Contraste AA em ambos. Se um par falhar, corrija e marque na matriz de contraste do README.

## AJUSTE 3: Linguagem do comprador (textos de exemplo)

Reescreva os textos do showcase em português direto, como um fabricante falaria com o dono de um mercadinho ou de uma distribuidora. Troque:

- "Supervisório de Engenharia", "Raio-X isométrico em corte técnico", "Motor de conversão acelerado para Google Ads", "Precisão termodinâmica classe II-A", "Sistema de Design proprietário" → termos como "Como a câmara é montada", "Veja por dentro", "Calcule o tamanho da sua câmara", "Projeto sob medida", "Instalação inclusa".
- Remova o botão/chip **"SFX: MUDO"** e qualquer efeito sonoro.
- Os chips de temperatura (-18 °C / +2 °C / +15 °C) **ficam**, mas rotule em linguagem de uso: "Congelados (-18 °C)", "Resfriados (0 a +15 °C)". Corrija o chip "+2 °C", que não existe como faixa de produto.
- Nada de texto no rodapé ou em qualquer exemplo sobre o DS ser "proprietário" ou sobre Google Ads. Isso é conversa interna, não vai para a LP.
- Mantenha o tom técnico apenas na **ficha técnica** (kcal/h, V, W, kg, dimensões).

## AJUSTE 4: Tipografia (máximo 2 famílias)

Hoje há 3 famílias (Archivo, Inter e JetBrains Mono, esta em cerca de 70 lugares).

- **Títulos:** Archivo (800/900) mantém.
- **Corpo e UI:** Inter (400/500/700).
- **JetBrains Mono: remova.** Para dados numéricos (valores do simulador, ficha técnica, rótulos de escala), use Inter com `font-variant-numeric: tabular-nums` e `letter-spacing` ligeiramente aberto, em caixa alta pequena para rótulos.
- Total: 2 famílias, 4 a 5 pesos no máximo. Mantenha `font-display: swap`.
- Rótulos pequenos devem ter no mínimo **12 px** (hoje há textos em 8 px e 11 px; "COMPRESSOR OK" em 8 px é ilegível no celular).

## AJUSTE 5: Números e claims de exemplo (etiquetar, não apagar)

Os números do showcase podem continuar como exemplo, mas **nenhum pode parecer real**. Faça isto:

1. Todo número, prazo, percentual, certificação, selo ou claim de exemplo recebe, no próprio componente, uma etiqueta visível **`EXEMPLO`** (pequena, fundo `--jd-amarelo`, texto `--jd-preto`). Vale para: contador de câmaras entregues, anos de mercado, prazo de entrega, "35% mais econômico", condutividade, classe de isolamento, norma/IT, "patente", garantia, capacidade de estocagem, depoimentos, logos de clientes.
2. **Remova por completo, mesmo como exemplo:**
   - "Patente industrial MG & GO" e qualquer menção a patente;
   - "35% mais econômico";
   - "Retardante a chamas comprovado (IT-10)" e "classe II-A", a menos que apareçam só como valor genérico de ficha técnica etiquetado `EXEMPLO`;
   - "Entrega em 7 a 15 dias" e "15 dias de prazo" como promessa de prazo;
   - "supercongelados -125 °C", "entregamos em todo o Brasil", "a mais famosa do Brasil".
3. A garantia aparece só como `00 anos [CONFIRMAR]`.
4. Faça um comentário HTML `<!-- EXEMPLO: não reutilizar na LP -->` ao lado de cada um desses blocos.
5. No README, crie a seção **"Números e claims de exemplo"** listando cada um, em qual componente aparece e o que o cliente precisa fornecer para virar dado real.
6. Rodapé com `[RAZÃO SOCIAL]` e `[CNPJ]` como placeholder.

## AJUSTE 6: Simulador térmico (manter, mas travar)

- **Mantenha** os três sliders, o resumo em tempo real e o botão "Solicitar orçamento com essas medidas".
- **Troque** o resultado "potência recomendada (BTU/h e HP)", "isolamento obrigatório" e "capacidade de estocagem em kg" por **valores de volume interno (m³) e área de painéis (m²)**, que são geometria exata e não dependem de engenharia. Mostre também o texto: "Potência e isolamento são definidos pelo projeto da JD. Envie as medidas e receba a proposta."
- Deixe a fórmula de potência/estocagem **desligada** e documentada no código com `// TODO: ativar quando a engenharia da JD validar a fórmula`.
- O botão deve **levar as medidas escolhidas (largura, comprimento, altura, aplicação) para campos ocultos do formulário de 2 etapas**, para chegarem no lead.
- Acessibilidade: os sliders precisam de rótulo, valor lido por leitor de tela e passo de teclado.

## AJUSTE 7: Mobile e detalhes

- Teste em **360 px**: o cabeçalho hoje quebra em várias linhas e os botões do topo (-18 °C, +2 °C, +15 °C, SFX) ocupam muito espaço. No mobile, simplifique para logo + botão "Pedir orçamento" e esconda os chips de temperatura (ou mova para uma barra horizontal rolável abaixo do hero).
- Botões, links e abas precisam ter **44 px de altura mínima** e estado de foco visível.
- Garanta que **o HTML funcione sozinho** ao abrir `design-system.html`, com os caminhos relativos de `css/` e `js/` corretos dentro de `ds-jd-camaras/`.

## AUTOVERIFICAÇÃO (obrigatória no fim)

No README, adicione a seção **"Verificação do ajuste 01b"** com:
1. Resultado da busca por hex/rgb fora da tabela (deve ser zero).
2. Quantidade de ocorrências de `--jd-ciano-logo` / `#00E0F0` e onde (deve ser logo + no máximo 1 detalhe por tela).
3. Famílias e pesos de fonte usados.
4. Lista de todos os blocos marcados `EXEMPLO`.
5. Matriz de contraste atualizada, nos dois temas.
6. Qualquer coisa que você não conseguiu cumprir e por quê.

No final da resposta, liste em até 6 linhas o que mudou e o que recomenda eu olhar primeiro.
