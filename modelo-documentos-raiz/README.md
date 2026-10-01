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
[`docs/material-base/`](docs/material-base/) — "referências completas" na seção
[Referências](#referências), ao final deste documento.

[Origem do material de base: de onde veio, se foi produzido por quem mantém o
repositório ou por terceiros, se está coberto pela licença deste projeto.] Por isso
esse material nunca é versionado nem redistribuído: fica só localmente, fora do
controle de versão (`.gitignore`).

## Licença

Este projeto usa duas licenças, para duas partes diferentes, mais uma exceção — texto
completo em [`NOTICE.md`](NOTICE.md):

| Parte | Licença | Significa que... |
|---|---|---|
| Código (`scripts/*.py`) | [GPL-3.0](LICENSE) | Pode usar/modificar/redistribuir, mas derivados também precisam ficar abertos |
| Conteúdo (documentos de teoria, dicionário, ficha) | [CC BY-NC-SA 4.0](LICENSE-CONTENT.txt) | Pode usar/adaptar com crédito, sem fins comerciais, mantendo a mesma licença |
| Material de terceiros em `docs/material-base/` | Nenhuma — são de terceiros | Não redistribuir; fica fora do controle de versão |

## Estrutura do projeto

| Arquivo | O que é |
|---|---|
| [`docs/material-gerado/`](docs/material-gerado/) | Documentos de teoria, dicionário, ficha, e as planilhas de pergunta |
| [`INDICE.md`](INDICE.md) | Índice com um link para cada documento; os itens ficam no índice interno de cada um |
| [`MANUAL.md`](MANUAL.md) | Guia rápido e não técnico de como usar o material e como colaborar |
| [`LICENSE`](LICENSE) | Texto completo da GPL-3.0 (código) |
| [`LICENSE-CONTENT.txt`](LICENSE-CONTENT.txt) | Texto completo da CC BY-NC-SA 4.0 (conteúdo) |
| [`NOTICE.md`](NOTICE.md) | Explica qual licença cobre qual arquivo, e a exceção do material de terceiros |
| [`.gitignore`](.gitignore) | Exclui o material de terceiros e arquivos temporários do controle de versão |
| [`scripts/montar_deck.py`](scripts/montar_deck.py) | Gera um `.apkg` para cada planilha de pergunta encontrada em `docs/material-gerado/` |
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

Material de aula que serviu de fonte primária para o conteúdo deste projeto (ver
[Origem do conteúdo](#origem-do-conteúdo)):

[NOME DA FONTE]. [S.l.: s.n., s.d.]. Material de aula, não publicado. Localização:
`docs/material-base/[arquivo]` (arquivo de terceiros, não versionado neste repositório).

---

*Este documento está licenciado sob [CC BY-NC-SA 4.0](LICENSE-CONTENT.txt). Ver
[NOTICE.md](NOTICE.md) para detalhes.*
