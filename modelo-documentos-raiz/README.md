# Núcleo de [Nome da Disciplina]

![Licenca codigo](https://img.shields.io/badge/C%C3%B3digo-GPL--3.0-blue)
![Licenca conteudo](https://img.shields.io/badge/Conte%C3%BAdo-CC_BY--NC--SA_4.0-blue)

## O que é isto

Um material de estudo de [disciplina]. O [`INDICE.md`](INDICE.md) lista e linka todos
os documentos, e o [`MANUAL.md`](MANUAL.md) é um guia rápido e não técnico de como usar o
material gerado para estudo. Este README é a documentação técnica do projeto.

## Aviso importante — leia antes de usar

Este conteúdo foi construído a partir do material de [disciplina] disponibilizado (ver
[Origem do conteúdo](#origem-do-conteúdo) abaixo) e organizado em torno da grade
específica de uma disciplina de graduação:

- A seleção de quais itens entraram, qual [achado/fato] é "o mais cobrado" e qual
  [resposta/conduta] é "a resposta esperada" reflete a escolha daquele material e daquele
  professor específico — não é a cobertura completa da literatura da área.
- Simplificações foram feitas para organizar o conteúdo em cadeias causais e fichas
  determinísticas (uma resposta "canônica" por eixo), o que pode omitir nuances e
  controvérsias que um material de referência completo traria.
- Este material serve como ferramenta de revisão, não como fonte primária de estudo —
  fatos clinicamente ou tecnicamente relevantes devem ser conferidos com a bibliografia
  oficial da disciplina antes de uma prova.

## Origem do conteúdo

O material de [disciplina] original que serviu de base para este núcleo está em
[`docs/material-base/`](docs/material-base/). Cada documento e cada cartão cita, junto
do fato, a fonte de onde ele veio, no sistema autor-data da ABNT; as referências
completas estão em [`docs/FONTES.md`](docs/FONTES.md).

[Origem do material de base: de onde veio, se foi produzido por quem mantém o
repositório ou por terceiros, se está coberto pela licença deste projeto.] Por isso
esse material nunca é versionado nem redistribuído: fica só localmente, fora do
controle de versão (`.gitignore`). O mesmo vale para a transcrição literal das aulas,
para a base de trechos literais do material de fora e para a prova de cada cartão, em
`docs/material-base/gerados-ocr/`: são cópia de material de terceiros, usadas só para
conferir o que se escreve.

Onde a aula não cobre o que algum eixo da ficha pede, o material usa [quais fontes de
fora — ou diga que a aula cobriu tudo e apague o resto deste parágrafo]. As cópias
dessas fontes ficam em `docs/material-base/fontes-externas/`, também fora do controle de
versão, e as referências delas estão em [`docs/FONTES.md`](docs/FONTES.md).

## Licença

Este projeto usa duas licenças, para duas partes diferentes, mais uma exceção — texto
completo em [`NOTICE.md`](NOTICE.md):

| Parte | Licença | Significa que... |
|---|---|---|
| Código (`scripts/*.py`) | [GPL-3.0](LICENSE) | Pode usar/modificar/redistribuir, mas derivados também precisam ficar abertos |
| Conteúdo (tudo o que não é código nem material de terceiros: documentos, planilhas, referências, dados) | [CC BY-NC-SA 4.0](LICENSE-CONTENT.txt) | Pode usar/adaptar com crédito, sem fins comerciais, mantendo a mesma licença |
| Material de terceiros em `docs/material-base/` | Nenhuma — são de terceiros | Não redistribuir; fica fora do controle de versão |

## Estrutura do projeto

| Arquivo | O que é |
|---|---|
| [`docs/material-gerado/`](docs/material-gerado/) | Documentos de teoria, dicionário, ficha, e as planilhas de pergunta |
| [`docs/FONTES.md`](docs/FONTES.md) | Referências, conforme a ABNT, de todas as fontes citadas nos documentos e nos cartões — geradas a partir de `docs/fontes.json` |
| [`docs/fontes.json`](docs/fontes.json) | Os dados de cada fonte (autoria, título, local, editora, data, endereço), de onde saem as referências |
| [`docs/formato.json`](docs/formato.json) | O formato da disciplina: curso, nível, itens, eixos, elos e colunas dos cartões |
| [`docs/bases/`](docs/bases/) | Um arquivo por item: o que foi lido do material de fora, a decisão sobre cada frase e a cobertura de cada subtópico (só códigos e decisões; o texto fica fora do controle de versão) |
| [`projeto.json`](projeto.json) | O mapa do projeto: onde fica cada coisa; os scripts tiram todo caminho daqui |
| [`fluxo-ia.json`](fluxo-ia.json) | O método em dados, que a IA lê pra seguir as etapas (copiado do projeto-modelo) |
| [`estilo-cartao.css`](estilo-cartao.css) | A aparência dos cartões no Anki |
| [`INDICE.md`](INDICE.md) | Índice com um link para cada documento; os itens ficam no índice interno de cada um |
| [`MANUAL.md`](MANUAL.md) | Guia rápido e não técnico de como usar o material e como colaborar |
| [`LICENSE`](LICENSE) | Texto completo da GPL-3.0 (código) |
| [`LICENSE-CONTENT.txt`](LICENSE-CONTENT.txt) | Texto completo da CC BY-NC-SA 4.0 (conteúdo) |
| [`NOTICE.md`](NOTICE.md) | Explica qual licença cobre qual arquivo, e a exceção do material de terceiros |
| [`.gitignore`](.gitignore) | Exclui o material de terceiros e arquivos temporários do controle de versão |
| [`scripts/`](scripts/README.md) | Os programas que fazem a parte mecânica do método — o README deles diz, em linguagem simples, pra que serve cada um e como rodar |
| [`anki-decks/`](anki-decks/) | Os arquivos `.apkg` prontos para importar no Anki |

Este projeto também usa um hook de commit local (`.githooks/`, copiado do projeto-modelo
`modelo-recorte-disciplina`) que verifica o formato da mensagem de commit — título mais
descrição em prosa, sem bullets. Essa pasta não é versionada aqui de propósito (é
ferramenta local de quem mantém o projeto, não conteúdo do repositório); se ela não
existir na sua cópia, veja `.githooks/README.md` no projeto-modelo para copiá-la e
ativá-la de novo.

## Como usar

Para estudar, importe os `.apkg` de `anki-decks/` no Anki, ou leia os documentos direto
em `docs/material-gerado/` (ver [MANUAL.md](MANUAL.md)). Para consultar um item
específico, abra o documento pelo [`INDICE.md`](INDICE.md) e use o índice interno do topo
dele. Para editar conteúdo, mude o
documento e a planilha correspondente em `docs/material-gerado/` e rode
`python scripts/montar_deck.py` para regerar os `.apkg`.

## Referências

As referências de todas as fontes citadas no projeto — as aulas e o material de fora
(ver [Origem do conteúdo](#origem-do-conteúdo)) —, conforme a ABNT NBR 6023, estão em
[`docs/FONTES.md`](docs/FONTES.md).

---

*Este documento está licenciado sob [CC BY-NC-SA 4.0](LICENSE-CONTENT.txt). Ver
[NOTICE.md](NOTICE.md) para detalhes.*
