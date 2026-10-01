# Scripts

Os scripts são os programas que fazem a parte mecânica do método: o trabalho que tem de
sair sempre igual, não importa quem rode nem quantas vezes. Nenhum deles tem nome de
disciplina no código — tudo vem dos arquivos do projeto.

Pra rodar um script, abra um terminal na pasta do projeto (no VSCode, menu
**Terminal → Novo Terminal**, ou `` Ctrl+` ``) e digite o comando que aparece na seção
dele. Cada script explica também, no começo do próprio arquivo, as opções que aceita.

## `validar_dados.py` — confere um arquivo de dados

Entra logo no começo, depois de gravar as respostas do
[Descubra seu modelo](../DESCUBRA-SEU-MODELO.md) em `docs/formato.json`, e de novo
sempre que um arquivo de dados mudar.

Confere o arquivo contra o schema dele, que fica em `scripts/esquemas/` com o mesmo nome
(o de `formato.json` é `formato.schema.json`): campos obrigatórios, tipos e ids
repetidos. Campo novo é aceito, porque o formato pode crescer.

- `python scripts/validar_dados.py docs/formato.json`

Usa só o Python, sem nada a instalar.

## `registrar_fonte.py` — liga o documento gerado à fonte dele

Entra assim que uma transcrição, ou outro documento gerado de uma fonte, é criada.

Grava no topo do documento de qual arquivo ele veio: o caminho e a impressão digital
(o hash) do arquivo. É esse registro que liga o gerado à fonte, não o nome dos arquivos.
Um documento que junta várias fontes leva uma linha por fonte, cada uma com uma chave
curta.

- `python scripts/registrar_fonte.py [documento] [arquivo de origem]`
- `python scripts/registrar_fonte.py [documento] [arquivo de origem] --chave [CHAVE]`

Usa só o Python, sem nada a instalar.

## `conferencia.py` — monta a conferência das transcrições

Entra com as transcrições prontas e registradas, antes de escrever qualquer material
(seção 5 da [metodologia](../metodologia-de-conteudo.md)).

Gera `docs/material-base/gerados-ocr/CONFERENCIA-COM-IMAGEM.md`: cada página do PDF, com a
imagem e o que a transcrição tem pra ela, e duas caixas de tique, uma pra IA e outra pra
pessoa, que é sempre o último elo. O script não julga o conteúdo, só mostra. Se o texto
de uma página ou o PDF mudar depois do tique, o tique é retirado.

- `python scripts/conferencia.py`

Precisa do Poppler, que traz os comandos `pdfinfo` e `pdftoppm`.

## `montar_deck.py` — das planilhas de pergunta ao baralho do Anki

Entra no fim, com as planilhas de pergunta prontas e conferidas (seção 6 da
[metodologia](../metodologia-de-conteudo.md)).

Lê cada planilha `perguntas-*.csv` de `docs/material-gerado/` e grava um `.apkg` por
planilha em `anki-decks/`, pronto pra importar no Anki. As colunas `pergunta` e
`resposta` são obrigatórias, e qualquer outra vira campo do cartão, com o mesmo nome.
Uma coluna `disciplina` separa os cartões em subdecks; `ordem` vira campo, mas não
aparece na linha de cima da pergunta; e a `fonte`, com a citação do fato, aparece no
verso, abaixo da resposta.

- `python scripts/montar_deck.py` gera todos os baralhos.
- `python scripts/montar_deck.py [trecho]` gera só os das planilhas cujo nome contém o
  trecho.
- `python scripts/montar_deck.py --listar` só lista as planilhas, sem gerar nada.

Precisa da biblioteca `genanki`: na primeira vez, rode `pip install genanki`.

---

*Este documento está licenciado sob [CC BY-NC-SA 4.0](../LICENSE-CONTENT.txt).*
