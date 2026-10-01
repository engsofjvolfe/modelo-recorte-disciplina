# Scripts

Os scripts são os programas que fazem a parte mecânica do método: o trabalho que tem de
sair sempre igual, não importa quem rode nem quantas vezes. Nenhum deles tem nome de
disciplina no código — tudo vem dos arquivos do projeto.

Pra rodar um script, abra um terminal na pasta do projeto (no VSCode, menu
**Terminal → Novo Terminal**, ou `` Ctrl+` ``) e digite o comando que aparece na seção
dele. Cada script explica também, no começo do próprio arquivo, as opções que aceita.

## `montar_deck.py` — das planilhas de pergunta ao baralho do Anki

Entra no fim, com as planilhas de pergunta prontas e conferidas (seção 6 da
[metodologia](../metodologia-de-conteudo.md)).

Lê cada planilha `perguntas-*.csv` de `docs/material-gerado/` e grava um `.apkg` por
planilha em `anki-decks/`, pronto pra importar no Anki. As colunas `pergunta` e
`resposta` são obrigatórias, e qualquer outra vira campo do cartão, com o mesmo nome.
Uma coluna `disciplina` separa os cartões em subdecks; `ordem` e `fonte` viram campo,
mas não aparecem na linha de cima da pergunta.

- `python scripts/montar_deck.py` gera todos os baralhos.
- `python scripts/montar_deck.py [trecho]` gera só os das planilhas cujo nome contém o
  trecho.
- `python scripts/montar_deck.py --listar` só lista as planilhas, sem gerar nada.

Precisa da biblioteca `genanki`: na primeira vez, rode `pip install genanki`.

---

*Este documento está licenciado sob [CC BY-NC-SA 4.0](../LICENSE-CONTENT.txt).*
