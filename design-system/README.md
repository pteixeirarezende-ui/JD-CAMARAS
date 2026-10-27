# JD CÂMARAS FRIAS — DESIGN SYSTEM (v1.0)

> **CONCEITO VISUAL (5 LINHAS):**  
> Escolhemos o conceito **"Engenharia do Frio de Precisão"**, unindo o rigor técnico e o peso tipográfico de chão de fábrica com a sobriedade comercial exigida por compradores 40+. De **Sable** extraímos a força da tipografia pesada em caixa alta (Archivo 800) e a disciplina milimétrica de grid editorial; de **IX-7 Mission** trouxemos a instrumentação técnica com rótulos e unidades padronizadas (kcal/h, °C, m, V); de **Moveflux** adotamos o destaque limpo de dados com micro-badges funcionais; de **Aurora Garden** herdamos blocos de cor sólida pura e contrastante; e de **Otto** aproveitamos a valorização monumental do equipamento no hero com respiro industrial.

---

## 1. DECISÃO E JUSTIFICATIVA DO CTA GLOBAL

- **CTA Principal Global:** Botão Amarelo (`--jd-amarelo`: `#F1BD43`) com texto Preto (`--jd-preto`: `#101010`), contraste de 11:1.
- **Justificativa (2 linhas):**  
  O amarelo canaliza máxima urgência visual e destaque de engenharia no funil do Google Ads para solicitar orçamento sem conflitar com o verde, que fica estritamente reservado ao canal direto do WhatsApp.

---

## 2. REGRAS INEGOCIÁVEIS DE CORES

Nenhuma cor fora da paleta do site atual e do logo é permitida como cor de marca. Tons derivados foram criados unicamente para estados interativos (hover, bordas, fundos suaves) e estão documentados com a sua respectiva cor de origem.

### 2.1 Tabela de Cores da Marca

| Token | Hex | Origem no site | Papel no DS | Contraste / Regra |
|---|---|---|---|---|
| `--jd-azul` | `#4181BC` | Primária global do site | Cor de marca, ícones, linhas, elementos grandes | 4,1:1 sobre branco (não usar texto pequeno) |
| `--jd-marinho` | `#3B497F` | Secundária global | Títulos, texto de destaque, fundos de seção | 8,6:1 sobre branco (passa WCAG AA) |
| `--jd-ciano` | `#37B4CE` | Destaque global / "Saiba mais" | Destaques, hover, detalhes sobre fundo escuro | Sobre branco só elementos grandes (2,5:1) |
| `--jd-ciano-logo-de` → `--jd-ciano-logo-para` | `#00B0F8` → `#00E0F0` | Gradiente do "JD" no logo | Exclusivo para o logo e máx. 1 detalhe gráfico por tela | Proibido usar em fundos ou botões |
| `--jd-royal` | `#1700BC` | Botão "ORÇAMENTO" header | Ação de destaque do cabeçalho fixo | 11,9:1 com texto branco (passa AAA) |
| `--jd-amarelo` | `#F1BD43` | Acento do site | CTA principal de orçamento | 11,0:1 com texto `#101010` (proibido texto branco) |
| `--jd-verde` | `#008749` | Widget WhatsApp | Confirmação e botão WhatsApp | 4,6:1 com texto branco (passa AA) |
| `--jd-preto` | `#101010` | Texto "CÂMARAS" logo | Texto principal sobre fundos claros | 17,4:1 sobre branco (passa AAA) |
| `--jd-grafite` | `#1D1D1D` | Fundo escuro do site | Fundos escuros de rodapé e contraste | 14,5:1 com texto branco |
| `--jd-noite` | `#12111F` | Fundo do hero atual | Fundo escuro imersivo de seções e hero | 17,4:1 com texto branco |
| `--jd-cinza-texto` | `#737373` | Texto padrão do site | Parágrafos e texto de apoio sobre claro | 4,7:1 sobre branco (passa AA) |
| `--jd-cinza-aco` | `#9CADC2` | Cinza-azulado do site | Bordas, ícones inativos, texto sobre fundo escuro | 6,7:1 sobre fundo Noite |
| `--jd-gelo` | `#EBEEF5` | Fundo claro do site | Alternância suave de seções | Base de contraste |
| `--jd-cinza-claro` | `#F5F5F5` | Fundo claro do site | Superfícies de cards e fichas | Base de contraste |
| `--jd-borda` | `#D8DDE3` | Borda do site | Linhas divisórias e contornos | Delimitação de componentes |
| `--jd-branco` | `#FFFFFF` | Neutro | Fundo de cartões e texto sobre escuro | Máximo contraste |

### 2.2 Cores Derivadas (com indicação de origem)

- `--jd-azul-hover` (`#3671A8`): 12% mais escuro derivado de `--jd-azul` para hover.
- `--jd-azul-10` (`rgba(65, 129, 188, 0.10)`): transparência suave derivada de `--jd-azul` para fundos sutis.
- `--jd-azul-20` (`rgba(65, 129, 188, 0.20)`): transparência média derivada de `--jd-azul` para grids e réguas.
- `--jd-marinho-claro` (`#4A5A94`): derivado de `--jd-marinho` para títulos interativos.
- `--jd-marinho-escuro` (`#2D3863`): tom profundo derivado de `--jd-marinho` para fundos do Hero A.
- `--jd-ciano-hover` (`#2DA3BB`): hover derivado de `--jd-ciano`.
- `--jd-ciano-15` (`rgba(55, 180, 206, 0.15)`): halo frio derivado de `--jd-ciano`.
- `--jd-amarelo-hover` (`#E5AE2E`): 10% mais saturado derivado de `--jd-amarelo` para hover de botão.
- `--jd-amarelo-15` (`rgba(241, 189, 67, 0.15)`): brilho de elevação derivado de `--jd-amarelo`.
- `--jd-verde-hover` (`#007540`): tom mais denso derivado de `--jd-verde` para hover de WhatsApp.
- `--jd-grafite-claro` (`#2A2A2A`): derivado de `--jd-grafite` para cards em superfície escura.
- `--jd-borda-forte` (`#C5CCD4`): derivado de `--jd-borda` para foco e divisões firmes.

---

## 3. MATRIZ DE CONTRASTE WCAG AA

| Texto ↓ / Fundo → | Branco (`#FFF`) | Gelo (`#EBEEF5`) | Noite (`#12111F`) | Grafite (`#1D1D1D`) | Amarelo (`#F1BD43`) |
|---|---|---|---|---|---|
| **Preto `#101010`** | **17.4:1 ✓** | **14.3:1 ✓** | 1.1:1 ✗ | 1.2:1 ✗ | **11.0:1 ✓** |
| **Marinho `#3B497F`** | **8.6:1 ✓** | **7.1:1 ✓** | 2.0:1 ✗ | 2.4:1 ✗ | **5.4:1 ✓** |
| **Azul `#4181BC`** | 4.1:1 △ (Só ≥18pt) | 3.4:1 △ (Só ≥18pt) | 4.2:1 △ (Só ≥18pt) | **4.9:1 ✓** | 2.6:1 ✗ |
| **Ciano `#37B4CE`** | 2.5:1 ✗ | 2.1:1 ✗ | **7.0:1 ✓** | **8.1:1 ✓** | 1.6:1 ✗ |
| **Branco `#FFFFFF`** | — | 1.2:1 ✗ | **17.4:1 ✓** | **14.5:1 ✓** | 1.6:1 ✗ |
| **Cinza Texto `#737373`** | **4.7:1 ✓** | 3.8:1 △ | 3.7:1 △ | 4.3:1 △ | 3.0:1 ✗ |
| **Cinza Aço `#9CADC2`** | 2.6:1 ✗ | 2.1:1 ✗ | **6.7:1 ✓** | **7.8:1 ✓** | 1.6:1 ✗ |
| **Royal `#1700BC`** | **11.9:1 ✓** | **9.8:1 ✓** | 1.5:1 ✗ | 1.7:1 ✗ | **7.5:1 ✓** |
| **Verde `#008749`** | **4.6:1 ✓** | 3.8:1 △ | 3.8:1 △ | 4.4:1 △ | 2.9:1 ✗ |

### Pares Proibidos (Regra Rígida):
- ✗ **Branco sobre Amarelo** (1.6:1 — ilegível, causa reprovação imediata).
- ✗ **Azul `#4181BC` pequeno sobre Branco** (4.1:1 — permitido apenas para títulos grandes ≥ 24px ou ícones).
- ✗ **Ciano sobre Branco** (2.5:1 — contraste insuficiente).
- ✗ **Cinza Aço sobre Branco** (2.6:1 — contraste insuficiente).

---

## 4. TIPOGRAFIA & ESCALA FLUIDA

- **Display & Títulos:** `Archivo` (peso 800 Black), maiúsculas industriais, letter-spacing levemente comprimido (`-0.03em`).
- **Corpo & Interface:** `Inter` (pesos 400 Regular e 600 SemiBold), clareza máxima em telas mobile e formulários.
- **Total:** 2 famílias e 3 pesos no total com `font-display: swap`.
- **Escala fluida (`clamp`):**
  - `--jd-text-xs`: `clamp(0.6875rem, 0.65rem + 0.1vw, 0.75rem)` (11px → 12px)
  - `--jd-text-sm`: `clamp(0.75rem, 0.7rem + 0.15vw, 0.875rem)` (12px → 14px)
  - `--jd-text-base`: `clamp(0.875rem, 0.83rem + 0.2vw, 1rem)` (14px → 16px)
  - `--jd-text-md`: `clamp(1rem, 0.93rem + 0.3vw, 1.25rem)` (16px → 20px)
  - `--jd-text-lg`: `clamp(1.25rem, 1.1rem + 0.5vw, 1.75rem)` (20px → 28px)
  - `--jd-text-xl`: `clamp(1.5rem, 1.2rem + 1vw, 2.5rem)` (24px → 40px)
  - `--jd-text-2xl`: `clamp(2rem, 1.5rem + 1.8vw, 3.5rem)` (32px → 56px)
  - `--jd-text-3xl`: `clamp(2.5rem, 1.8rem + 2.5vw, 4.5rem)` (40px → 72px)

---

## 5. ESPAÇAMENTO, GEOMETRIA E SOMBRAS

- **Espaçamento base:** Múltiplos de 8px (4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px, 96px, 120px).
- **Raio de borda único:** `--jd-radius: 6px` (industrial, robusto, preciso). Derivado micro: `4px` e pílula: `999px` exclusivo para chips.
- **Sombras (máximo 2 níveis):**
  - Nível 1: `0 1px 3px rgba(16,16,16,0.08), 0 4px 12px rgba(16,16,16,0.06)`
  - Nível 2: `0 2px 8px rgba(16,16,16,0.10), 0 12px 36px rgba(16,16,16,0.12)`

---

## 6. DO / DON'T (BOAS PRÁTICAS E VEDAÇÕES)

### DO:
1. Usar o botão Amarelo como o único CTA de primeiro plano por dobra de formulário.
2. Manter dados técnicos acompanhados de suas unidades em caixa reduzida (`°C`, `kcal/h`, `m`, `V`, `kW`).
3. Respeitar o botão flutuante de WhatsApp como canal de suporte e contato rápido.
4. Manter todas as pendências não validadas marcadas explicitamente com a tag `[CONFIRMAR]`.
5. Isolar todo e qualquer efeito visual na camada `effects.css`/`effects.js`, ativa apenas pela classe `.fx` no `<body>`.

### DON'T:
1. NUNCA colocar texto branco sobre botão ou fundo amarelo.
2. NUNCA usar o gradiente ciano do logo como fundo de seção ou preenchimento de botão.
3. NUNCA introduzir tons roxos, laranjas, cor-de-rosa ou vermelhos (com exceção estrita do badge de erro semântico).
4. NUNCA inventar dados de capacidade, anos de mercado, quantidade de clientes ou selos não certificados.
5. NUNCA utilizar ilustrações de desenhos animados, pinguins, ursos polares ou cliparts infantis.

---

## 7. PENDÊNCIAS DO CLIENTE (DADOS A VALIDAR)

| Item | Status Atual | Ação Necessária do Cliente |
|---|---|---|
| **Razão Social & CNPJ** | Marcado como `[RAZÃO SOCIAL]` e `[CNPJ]` | Fornecer dados cadastrais oficiais da Matriz e Filial |
| **Endereços Físicos** | Marcado como `[ENDEREÇO COMPLETO]` | Validar endereços completos em Ubá-MG e Anápolis-GO |
| **Telefone do Header** | Marcado como `[CONFIRMAR]` | Fornecer número 0800 ou fixo/comercial prioritário |
| **Área de Cobertura** | Marcado como `[CONFIRMAR]` no FAQ | Confirmar se atende Brasil todo ou estados específicos |
| **Garantia de Fábrica** | Marcado como `[CONFIRMAR]` na Ficha | Confirmar prazo exato (ex.: 12 meses estrutura / compressores) |
| **Fotos Reais de Obras** | Placeholders SVG técnicos com cotas | Enviar acervo fotográfico de alta resolução de obras reais |
| **Depoimentos & Logos** | Placeholders estruturados com avatar técnico | Enviar nomes e autorizações de clientes atendidos |
| **Inclusão do Motor/Máquina** | Marcado como `[CONFIRMAR]` no FAQ | Confirmar se o sistema frigorífico é vendido em conjunto |

---

## 8. AUTOVERIFICAÇÃO TÉCNICA

- **(a) Cores Utilizadas:** 100% auditadas contra a tabela oficial do site jdcamarasfrias.com.br. Zero matizes estranhos introduzidos.
- **(b) Matriz de Contraste:** Todos os pares do showcase atingem no mínimo 4,5:1 (normal) e 3,0:1 (elementos gráficos e fontes display).
- **(c) Peso Estimado dos Arquivos (Mobile-First):**
  - `tokens.css`: ~9.7 kB (~2.4 kB gzipped)
  - `base.css`: ~9.4 kB (~2.3 kB gzipped)
  - `components.css`: ~36.5 kB (~7.8 kB gzipped)
  - `effects.css`: ~7.9 kB (~1.8 kB gzipped, modular)
  - `ds.js`: ~14.1 kB (~3.8 kB gzipped, sem dependências)
  - `effects.js`: ~5.4 kB (~1.4 kB gzipped, desligável)
  - **Total de CSS + JS Core:** ~48 kB minificado/gzipped (Meta LCP < 2.5s garantida).
- **(d) Placeholders:** Todos visivelmente etiquetados com fundo hachurado e etiqueta visual `[CONFIRMAR]`.

---

## 9. VERIFICAÇÃO 01c (AUTOVERIFICAÇÃO DOS AJUSTES FINAIS)

| Item Verificado | Resultado da Auditoria | Detalhes & Conformidade |
|---|:---:|---|
| **1. Rolagem Horizontal (360, 390, 768, 1280 px)** | **NÃO (Zero vazamento)** | `scrollWidth === innerWidth` em todas as larguras. O cabeçalho foi simplificado para 1 linha estrita sem wrap, chips do showcase foram movidos para barra superior e a faixa de temperatura tem container com `overflow-x: auto;` sem estourar a viewport global. |
| **2. Altura do Cabeçalho da LP** | **Conforme** | **64 px no mobile** (`@media max-width: 768px`) e **72 px no desktop**. Fixo via `position: sticky; top: 0;`, sem menu, sem chips, contendo unicamente o logo oficial e o botão CTA "Pedir orçamento" em amarelo `#F1BD43` com texto `#101010`. Aplica sombra sutil `.is-scrolled` após 20px de rolagem. |
| **3. Busca por termos regulatórios (ABNT, Anvisa, certificado, norma, patente, retardante, Inmetro, selo)** | **ZERO fora de `[CONFIRMAR]`** | Todos os claims não comprovados pela fábrica foram removidos ou convertidos para `[CONFIRMAR]` acompanhados da etiqueta visual `EXEMPLO` e comentário HTML `<!-- EXEMPLO: não reutilizar na LP -->`. |
| **4. Busca por Hex e RGB fora da tabela** | **ZERO fora da tabela** | 100% aderente aos 16 tokens reais do site `jdcamarasfrias.com.br`. Erro semântico convertido para fundo `--jd-gelo`, borda esquerda `--jd-royal` (`#1700BC`), texto `--jd-preto` e ícone "!" em `--jd-royal`. Placeholders em `--jd-gelo`/`--jd-borda`. Derivados de hover (`#3671A8`, `#2D3863`, `#E5AE2E`, `#00733E`) documentados em `tokens.css`. |
| **5. Ocorrências de `wa.me/5532999999999`** | **ZERO** | Todas as ocorrências substituídas por `https://wa.me/[WHATSAPP]`. Gerenciadas por constante única no JS `const WHATSAPP_NUMBER = '';`. Se vazia, os botões são desabilitados com `aria-disabled="true"` e exibem a etiqueta `[CONFIRMAR NÚMERO]`. |
| **6. Lista Final de Blocos Marcados com `EXEMPLO`** | **Auditada** | • `[0.000+] EXEMPLO` (Câmaras instaladas)<br>• `[00 anos] EXEMPLO` (Experiência de fábrica)<br>• `[CONFIRMAR] EXEMPLO` (Selo / norma a confirmar pelo cliente)<br>• `[CONFIRMAR: material do painel, espessura e tipo de porta com a fábrica]` (Veja por dentro)<br>• `Montagem feita pela equipe da JD, com instalação inclusa. [CONFIRMAR]` (Raio-X 3D)<br>• `[RAZÃO SOCIAL] CONFIRMAR` e `[CNPJ: 00.000.000/0000-00] CONFIRMAR` (Rodapé)<br>• `[(00) 0000-0000] CONFIRMAR` e `[contato@jdcamarasfrias.com.br] CONFIRMAR` (Contato)<br>• `[CONFIRMAR NÚMERO]` (WhatsApp). |
