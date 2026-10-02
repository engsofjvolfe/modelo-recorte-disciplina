# Núcleo de [Nome da Disciplina]

![Licenca codigo](https://img.shields.io/badge/C%C3%B3digo-GPL--3.0-blue)
![Licenca conteudo](https://img.shields.io/badge/Conte%C3%BAdo-CC_BY--NC--SA_4.0-blue)

## O que é isto

Um material de estudo de [disciplina]. O [`INDICE.md`](INDICE.md) tem um link pra cada
documento, e o [`MANUAL.md`](MANUAL.md) é um guia rápido de como estudar com o material.
Este README apresenta o projeto: o aviso sobre o recorte, como o material foi feito, de
onde ele veio, as licenças e onde fica cada arquivo.

## Aviso importante — leia antes de usar

Este conteúdo foi construído a partir do material de [disciplina] disponibilizado (ver
[Origem do conteúdo](#origem-do-conteúdo) abaixo) e organizado em torno da grade
específica de uma disciplina de graduação:

- A seleção de quais itens entraram, qual [achado/fato] é "o mais cobrado" e qual
  [resposta/conduta] é "a resposta esperada" reflete a escolha daquele material e daquele
  professor específico — não é a cobertura completa da literatura da área.
- Simplificações foram feitas pra organizar o conteúdo em histórias de causa e efeito e
  em fichas secas, com uma resposta só pra cada tipo de fato, o que pode deixar de fora
  nuances e controvérsias que um material de referência completo traria.
- Este material serve como ferramenta de revisão, não como fonte principal de estudo —
  fatos importantes devem ser conferidos com a bibliografia oficial da disciplina antes
  de uma prova.

## Como este material foi feito

Parte do trabalho pode ter sido feita por processos automáticos, e a parte mais difícil
— transcrever as aulas, redigir os documentos, gerar as perguntas — pode ter sido feita
com ajuda de IA. Cada parte do trabalho é uma de duas coisas:

- **Mecânica:** feita por um programa, sempre do mesmo jeito, sem julgar o conteúdo —
  montar as referências, conferir se cada trecho citado está na fonte, montar os cartões
  do Anki.
- **Julgamento:** de uma pessoa, contra a fonte — escolher o recorte, decidir cada fato
  e conferir, por último, cada página transcrita, cada referência e cada cartão.

[Diga em que etapas a IA entrou neste projeto, ou que ela não foi usada.] O que é
mecânico e o que é julgamento em cada etapa está explicado na metodologia do
projeto-modelo `modelo-recorte-disciplina`, seção 11 ("Confira: primeiro o script,
depois a pessoa").

## Origem do conteúdo

O material de [disciplina] original que serviu de base para este núcleo fica em
[`docs/material-base/`](docs/material-base/). Cada documento e cada cartão cita, junto
do fato, a fonte de onde ele veio, no sistema autor-data da ABNT; as referências
completas estão em [`docs/FONTES.md`](docs/FONTES.md).

[Origem do material de base: de onde veio, se foi produzido por quem mantém o projeto ou
por outras pessoas, se está coberto pela licença deste projeto.] Por isso esse material
nunca é publicado nem repassado: fica só no computador de quem mantém o projeto. O mesmo
vale para a transcrição das aulas, a base de trechos do material de fora e a prova de
cada cartão, em `docs/material-base/gerados-ocr/`: são cópias de material de terceiros,
usadas só para conferir o que se escreve.

Onde a aula não cobre o que algum eixo da ficha pede, o material usa [quais fontes de
fora — ou diga que a aula cobriu tudo e apague o resto deste parágrafo]. As cópias
dessas fontes ficam em `docs/material-base/fontes-externas/`, também sem publicar, e as
referências delas estão em [`docs/FONTES.md`](docs/FONTES.md).

## Licença

Uma licença diz o que cada pessoa pode fazer com um trabalho. Este projeto usa duas,
para duas partes diferentes, mais uma exceção — os detalhes estão em
[`NOTICE.md`](NOTICE.md):

| Parte | Licença | Significa que... |
|---|---|---|
| Programas (os scripts de `scripts/`) | [GPL-3.0](LICENSE) | Pode usar, mudar e repassar, mas as versões mudadas também precisam ficar abertas pra todo mundo |
| Conteúdo (tudo o que não é programa nem material de terceiros: documentos, planilhas, referências, dados) | [CC BY-NC-SA 4.0](LICENSE-CONTENT.txt) | Pode usar e adaptar dando o crédito, sem fins comerciais, mantendo a mesma licença |
| Material de terceiros em `docs/material-base/` | Nenhuma — é de terceiros | Não publicar nem repassar |

## Onde fica cada coisa

| Arquivo | O que é |
|---|---|
| [`docs/material-gerado/`](docs/material-gerado/) | Os documentos de teoria, dicionário e ficha, e as planilhas de pergunta |
| [`docs/FONTES.md`](docs/FONTES.md) | As referências, conforme a ABNT, de todas as fontes citadas nos documentos e nos cartões — feitas a partir de `docs/fontes.json` |
| [`docs/fontes.json`](docs/fontes.json) | Os dados de cada fonte (autoria, título, local, editora, data, endereço), de onde saem as referências |
| [`docs/formato.json`](docs/formato.json) | O formato da disciplina: curso, nível, itens, eixos, elos e colunas dos cartões |
| [`docs/bases/`](docs/bases/) | Um arquivo por item: o que foi lido do material de fora, a decisão sobre cada frase e a cobertura de cada subtópico (só códigos e decisões; o texto das fontes nunca é publicado) |
| [`projeto.json`](projeto.json) | O mapa do projeto: onde fica cada coisa; os scripts tiram todo caminho daqui |
| [`fluxo-ia.json`](fluxo-ia.json) | O método em dados, que a IA lê pra seguir as etapas (copiado do projeto-modelo) |
| [`estilo-cartao.css`](estilo-cartao.css) | A aparência dos cartões no Anki |
| [`INDICE.md`](INDICE.md) | O índice, com um link para cada documento; os itens ficam no índice do topo de cada um |
| [`MANUAL.md`](MANUAL.md) | O guia rápido de como estudar com o material e como ajudar a corrigi-lo |
| [`LICENSE`](LICENSE) | O texto completo da GPL-3.0 (programas) |
| [`LICENSE-CONTENT.txt`](LICENSE-CONTENT.txt) | O texto completo da CC BY-NC-SA 4.0 (conteúdo) |
| [`NOTICE.md`](NOTICE.md) | Qual licença vale pra qual arquivo, e a exceção do material de terceiros |
| [`.gitignore`](.gitignore) | Pra quem guarda o projeto no GitHub: a lista do que nunca vai pra lá (o material de terceiros e arquivos temporários) |
| [`scripts/`](scripts/README.md) | Os pequenos programas que fazem a parte mecânica do método — o README deles diz, em palavras simples, pra que serve cada um e como rodar |
| [`anki-decks/`](anki-decks/) | Os baralhos prontos pra importar no Anki (os arquivos `.apkg`) |

## Como usar

Para estudar, importe no Anki os baralhos de `anki-decks/` (os arquivos `.apkg`), ou leia
os documentos direto em `docs/material-gerado/` (ver o [MANUAL.md](MANUAL.md)). Para achar
um item, abra o documento pelo [`INDICE.md`](INDICE.md) e use o índice do topo dele. Para
mudar o conteúdo, mude o documento e a planilha correspondente em `docs/material-gerado/`
e gere os baralhos de novo com o script `montar_deck.py` (o
[README dos scripts](scripts/README.md) diz como rodar).

## Referências

As referências de todas as fontes citadas no projeto — as aulas e o material de fora
(ver [Origem do conteúdo](#origem-do-conteúdo)) —, conforme a ABNT NBR 6023, estão em
[`docs/FONTES.md`](docs/FONTES.md).

---

*Este documento está licenciado sob [CC BY-NC-SA 4.0](LICENSE-CONTENT.txt). Ver
[NOTICE.md](NOTICE.md) para detalhes.*
