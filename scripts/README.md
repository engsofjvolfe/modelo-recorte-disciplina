# Scripts

## O que é um script, e por que o método usa

Um script é um programa pequeno que faz sozinho um trabalho repetitivo, sempre do mesmo
jeito, não importa quem rode nem quantas vezes. É por isso que o método confia neles pra
parte mecânica: montar as referências, as conferências e o baralho sem esquecer nada e
sem inventar nada. O que um script não faz é julgar se um conteúdo está certo — isso é
sempre de uma pessoa.

Nenhum script tem nada de disciplina dentro dele, nem caminho de pasta: o que muda de um
projeto pra outro fica nos arquivos de dados do projeto. Os únicos nomes fixos são os do
próprio motor — a pasta `scripts/`, tudo o que está dentro dela e o `projeto.json` — e
eles nunca se mudam: é por esses nomes que os scripts se acham uns aos outros.

## Antes da primeira vez

Você precisa de três coisas. Faça uma vez só, no seu computador.

1. **O Python**, o programa que roda os scripts. Pra saber se já tem, abra o terminal
   (veja abaixo como) e digite `python --version`. Se aparecer algo como
   `Python 3.12.1`, está pronto. Se aparecer erro, tente `python3 --version`; se as duas
   derem erro, instale o Python pelo site [python.org](https://www.python.org/downloads/).
   Se no seu computador o que funcionou foi `python3`, use `python3` no lugar de
   `python` em todos os comandos deste guia.
2. **O mapa do projeto**, o arquivo `projeto.json`. Copie
   [`modelo-dados/projeto.json`](../modelo-dados/projeto.json) pra pasta principal do
   projeto da sua disciplina. Ele diz aos scripts onde fica cada coisa: onde estão as
   aulas, onde ficam as transcrições, onde sai o baralho. Se um dia você mudar uma pasta
   de lugar, muda só nesse arquivo — nenhum script precisa ser mexido. Só lembre de mudar
   também o `.gitignore`, se a pasta mudada for a do material de base: é ele que mantém o
   material de terceiros fora do GitHub. No mesmo arquivo ficam a resolução das imagens
   das conferências e o nome da pasta onde elas são gravadas. Copie junto o
   [`modelo-dados/estilo-cartao.css`](../modelo-dados/estilo-cartao.css): é a aparência
   dos cartões do Anki (cores, tamanho da letra), e você pode mudá-la ali. E copie a
   pasta `scripts/` inteira, com as subpastas `esquemas/` e `normas/`: são os próprios
   scripts e os arquivos que eles leem. Não mude o nome dela nem de nada lá dentro.
3. **Dois complementos**, só pra alguns scripts:
   - pro `montar_deck.py`, a biblioteca `genanki`: no terminal, digite
     `pip install genanki` (ou `pip3 install genanki`) e aperte Enter;
   - pro `conferencia.py` e o `base_externa.py`, e pro `referencias.py` e o
     `registrar_fonte.py` quando a fonte é PDF, o Poppler, que é o que lê o texto de uma
     página de PDF e a transforma em imagem: no Linux, `sudo apt install
     poppler-utils`; no Mac, `brew install poppler`; no Windows, siga as instruções do
     Poppler pra Windows, ou peça à IA que você usa o passo a passo pro seu computador.

## Como rodar um script

1. **Abra o terminal.** O terminal é a janela onde se digita um comando em vez de clicar.
   No VSCode: menu **Terminal → Novo Terminal** (ou as teclas `` Ctrl+` ``). Ele abre
   embaixo, já dentro da pasta do projeto.
2. **Digite o comando** que aparece na seção do script, aqui embaixo, e aperte Enter.
   Você pode estar em qualquer pasta dentro do projeto: o script sobe de pasta em pasta
   até achar o `projeto.json`, e calcula todo o resto a partir dali.
3. **Leia o que aparece.** O script sempre diz o que fez. Uma linha que começa com
   `ERRO`, `FALTA` ou `CONFERIR` pede alguma coisa sua e diz o quê.

Os comandos usam `scripts/...` porque os scripts ficam na pasta `scripts` do projeto. Se
eles estiverem em outro lugar, troque pelo caminho de onde estão. Os caminhos de exemplo,
como `docs/formato.json`, são os do modelo; no seu projeto, valem os do `projeto.json`.

## A ordem em que eles entram

| Quando | Script |
| --- | --- |
| Depois de responder o Descubra seu modelo | `validar_dados.py` |
| Assim que cada transcrição é criada | `registrar_fonte.py`, que já roda o `referencias.py` |
| Sempre que mudar os dados das fontes | `referencias.py` |
| Com as transcrições prontas, antes de escrever o material | `conferencia.py` |
| Quando a aula não cobre um eixo de um item | `base_externa.py`, que também roda o `referencias.py` |
| Com as planilhas de pergunta e as provas dos cartões prontas | `confere_cartoes.py` |
| Com as planilhas de pergunta prontas e conferidas | `montar_deck.py` |

## `validar_dados.py` — confere um arquivo de dados

**Pra que serve.** Os arquivos de dados do projeto (o `projeto.json`, o `formato.json`, o
`fontes.json`, o arquivo de base de cada item, o de prova de cada planilha e o
`fluxo-ia.json`) têm uma forma certa, descrita num molde —
o *schema* — que fica em `scripts/esquemas/`. Este script confere se o arquivo segue o
molde: se não falta campo obrigatório, se nada está no tipo errado, se nenhum código (id
ou chave) se repete.

**Quando usar.** Depois de preencher qualquer um desses arquivos, e sempre que mexer
neles.

**Como rodar.** Escreva o caminho do arquivo depois do nome do script:

    python scripts/validar_dados.py docs/formato.json

O script acha o molde pelo nome do arquivo (o de `formato.json` é `formato.schema.json`).
Os arquivos de base têm o nome do item, e os de prova, o nome da planilha, então pra eles
diga o molde com `--schema` (`base.schema.json` ou `prova.schema.json`):

    python scripts/validar_dados.py docs/bases/AG1.json --schema scripts/esquemas/base.schema.json

**O que aparece.** `0 erro(s)` quer dizer que está tudo na forma certa. Senão, cada
linha `ERRO` diz onde está o problema. Por exemplo, `$.itens[2].id: deve ser string` quer
dizer: no terceiro item da lista `itens`, o `id` tem de ser um texto (a contagem começa
do zero, então `[2]` é o terceiro).

Usa só o Python: não precisa instalar nada.

## `registrar_fonte.py` — liga a transcrição à fonte dela

**Pra que serve.** Grava, no topo da transcrição (ou de outro documento gerado de uma
fonte), de qual arquivo ela veio: a chave da fonte, o caminho do arquivo e a impressão
digital dele — um código que muda se o arquivo mudar. É assim que os outros scripts sabem
qual PDF corresponde a qual transcrição: pelo registro, não pelo nome dos arquivos, que
pode ter erro de digitação.

**Quando usar.** Assim que uma transcrição é criada.

**Como rodar.** Três coisas depois do nome do script: a transcrição, o arquivo de onde
ela veio e a chave da fonte — a mesma chave da referência dela no `fontes.json`:

    python scripts/registrar_fonte.py docs/material-base/gerados-ocr/AULA-1.md docs/material-base/AULA-1.pdf AULA-1

**O que aparece.** A linha gravada e, logo depois, o resultado do `referencias.py`, que
este script roda sozinho no fim: se a chave ainda não tem referência, aparece
`FALTA REFERÊNCIA`; se há referências sem o tique da pessoa, aparece `CONFERIR`.

Precisa do Poppler quando a fonte é PDF, porque o `referencias.py`, que ele roda, mostra a
primeira página dela.

## `referencias.py` — monta as referências e a conferência delas

**Pra que serve.** Você, ou a IA, preenche no `fontes.json` os dados de cada fonte:
autoria, título, local, editora, data, endereço, data de acesso. O script escreve cada
referência no padrão da ABNT (NBR 6023), coloca em ordem alfabética e grava o arquivo de
referências do projeto (no modelo, `docs/FONTES.md`). Ninguém digita a referência à mão.
Ele monta também a chamada de cada fonte, o que vai no meio do texto, como
`(Silva, 2020)`, pela norma de citações (NBR 10520). As [Regras da ABNT](../regras-abnt.md)
explicam cada campo do `fontes.json` e o que cada norma pede.

Junto, ele monta a conferência das referências (no modelo, `CONFERENCIA-REFERENCIAS.md`,
na pasta das transcrições): cada referência e a chamada dela como ficaram, ao lado da
cópia da fonte — a primeira página, se for PDF —, com duas caixas de tique, uma pra IA e
outra pra pessoa. Confira se a referência bate com a folha de rosto ou com a página do
documento.

Três coisas dependem de você, nos dados: o campo `et_al`, no topo do arquivo, diz se uma
fonte com quatro autores ou mais aparece só com o primeiro, seguido de *et al.*, ou com
todos; o campo `idioma` de cada fonte diz em que língua sai o mês da data, e é
obrigatório quando a data tem mês; e o campo `participacao` (`org.`, `coord.`...) diz que
os autores organizaram a obra. O mês da data de acesso sai no idioma do texto, que vem
do formato da disciplina (`docs/formato.json`, no modelo). As expressões "Disponível em:"
e "Acesso em:" são as da norma e saem sempre assim. A abreviatura dos meses de cada
idioma fica em `scripts/normas/meses.json`: são as abreviaturas que a norma adota.

**Quando usar.** Sempre que mudar o `fontes.json`. O `registrar_fonte.py` já roda este
script sozinho.

**Como rodar.**

    python scripts/referencias.py

**O que aparece.** Quantas referências foram gravadas e onde. `ERRO` aponta o que falta
ou não pode ser nos dados, como uma data com mês numa fonte sem `idioma`; nesse caso nada
é gravado. `FALTA REFERÊNCIA` lista fonte registrada que ainda não tem dados no
`fontes.json`; `CONFERIR` lista as referências que ainda não têm o tique da pessoa.

Precisa do Poppler quando alguma fonte é PDF, pra mostrar a primeira página.

## `conferencia.py` — monta a conferência das transcrições

**Pra que serve.** Monta um arquivo pra conferir cada transcrição contra o original,
página por página: a imagem da página no PDF, ao lado do que a transcrição tem pra ela, e
duas caixas de tique, uma pra IA e outra pra pessoa. O script não julga nada, só mostra.
Quem confere é quem tica, e a pessoa é sempre o último elo.

**Quando usar.** Com as transcrições prontas e registradas, antes de escrever qualquer
material, e de novo sempre que uma transcrição mudar.

**Como rodar.**

    python scripts/conferencia.py

**O que aparece.** Quantas páginas há e quantas ainda estão sem o tique da pessoa. Uma
linha `ERRO` aparece pra transcrição sem registro, com mais de uma fonte registrada ou
cujo PDF mudou ou não existe, e pra PDF da pasta do material de base que não é a fonte de
nenhuma transcrição. O arquivo gerado (no modelo, `CONFERENCIA-COM-IMAGEM.md`, na pasta das transcrições) fica
melhor de ler na visualização do VSCode: abra o arquivo e aperte `Ctrl+Shift+V`.

Precisa do Poppler.

## `base_externa.py` — monta a base do material de fora

**Pra que serve.** Quando a aula não traz o que algum eixo pede pra um item, o fato vem
de um material de fora — um guia oficial, um livro, uma página da internet. Este script
monta a base desse material: um arquivo só com as frases que o item usa, copiadas letra
por letra da fonte, com a página de cada uma. Ninguém copia trecho à mão: o script
recolhe todo o texto das páginas que você declarar, a IA decide o que cada frase é, e a
pessoa confere.

**Como funciona, passo a passo.**

1. Copie [`modelo-dados/base.json`](../modelo-dados/base.json) pra `docs/bases/`, com o id
   do item no nome (por exemplo, `docs/bases/AG1.json`), e preencha:
   - em `lugares`, cada fonte lida: a chave da referência dela, o arquivo e as páginas
     do arquivo que foram lidas (em PDF). Em `desloca`, quanto somar à página do arquivo
     pra chegar ao número impresso — se a página 47 do arquivo tem impresso "45", é `-2`.
     Se a diferença não for a mesma em todas as páginas, use `impressas`, com o número
     impresso de cada página do arquivo: `{"47": "45", "48": "xii"}`;
   - em `cobertura`, cada subtópico da grade do formato da disciplina: `aula` (a aula
     cobre), `fonte` (vem do material de fora) ou `lacuna` (nenhuma fonte cobre). Um eixo
     sem subtópicos é marcado pelo id do próprio eixo.
2. Rode o script. Na primeira vez, todas as frases aparecem como **sem classe** no
   arquivo de conferência, cada uma com um código, como `GUIA-2020:p47:3f2a91c0`: uma
   frase da página 47 do arquivo da fonte GUIA-2020. O final do código é uma impressão
   digital do texto da própria frase. Se a frase mudar — o PDF foi trocado, ou a
   separação em frases mudou —, o código muda junto: a classe antiga aparece como
   "classe para frase que não existe" e a frase nova como "sem classe". Assim uma classe
   nunca passa de uma frase para outra sem ninguém ver.
3. A IA, ou você, classifica cada frase em `classes`, no arquivo de dados, pelo código:
   - `usa`, com o `subtopico` e a `afirmacao`: `categorica` se a fonte afirma,
     `possibilidade` se ela trata como possível ou provável;
   - `outro-item`, `repetida` (com `de`: o código da frase que ela repete),
     `fora-do-recorte` ou `nao-e-conteudo` (referência, cabeçalho, legenda solta).

   A separação em frases é mecânica: se ela partir uma frase em duas, junte os códigos em
   `juntar`; se juntar dois pedaços numa frase só, a classe vale pro pedaço inteiro.
4. Rode de novo. Com tudo classificado, sai a base do item, e a conferência mostra cada
   página com as frases e a classe de cada uma, com os tiques da IA e da pessoa.

**Como rodar.**

    python scripts/base_externa.py

Ele refaz sempre todos os itens de uma vez: a conferência é um arquivo só, e é assim que
os tiques de todos os itens continuam nela.

**O que aparece.** Uma linha `ERRO` pra tudo o que falta ou se contradiz: frase sem
classe, subtópico sem marca, subtópico marcado como `fonte` sem nenhuma frase usada,
frase usada num subtópico que a aula já cobre ou que está marcado como `lacuna`. Com
`ERRO`, a base do item não é gravada: o arquivo dela fica só com esse aviso. O script não
julga se a classe está certa — isso é a conferência. Logo depois aparece o resultado das referências: este script
também roda o `referencias.py`, porque a base registra as fontes que usa.

Precisa do Poppler quando alguma fonte é PDF.

## Como ticar uma conferência

Os arquivos de conferência têm, em cada parte, duas linhas assim:

    - [ ] IA
    - [ ] pessoa

Pra ticar, abra o arquivo no VSCode, no modo de texto (não na visualização), e troque o
espaço entre os colchetes por um `x`: `- [x] pessoa`. Salve. Quando o script gerar o
arquivo de novo, o tique continua lá — a não ser que o conteúdo daquela parte tenha
mudado depois do tique: aí o tique sai, e a parte diz isso, pra ninguém achar que o texto
novo já foi conferido.

## `confere_cartoes.py` — confere cada cartão contra a prova dele

**Pra que serve.** Cada cartão diz um fato com palavras próprias e traz, atrás, a citação
da fonte, na coluna `fonte`. A prova do cartão é o trecho da fonte que diz esse fato,
copiado letra por letra. Ela fica num arquivo à parte, um por planilha, fora do GitHub,
porque é texto de terceiros. Este script confere, cartão por cartão, se o trecho está
mesmo no lugar que a citação diz — a página ou o slide da transcrição da aula, ou uma
frase da base do material de fora — e monta a conferência dos cartões, com os tiques da
IA e da pessoa.

**Como funciona, passo a passo.**

1. Copie [`modelo-dados/prova.json`](../modelo-dados/prova.json) pra pasta das provas,
   com o nome da planilha: no modelo, a prova da planilha `perguntas-nucleo.csv` fica em
   `docs/material-base/gerados-ocr/provas/perguntas-nucleo.json`.
2. Pra cada cartão, a IA, ou você, escreve ali três coisas:
   - a `pergunta`, igual à da planilha — é por ela que o cartão e a prova se acham;
   - os `trechos`, copiados da transcrição ou da base, letra por letra;
   - a `afirmacao`: `categorica`, se a fonte afirma, ou `possibilidade`, se ela trata
     como possível. Nesse caso, a resposta do cartão tem de dizer isso.
3. Na coluna `fonte` da planilha vão só as chamadas, cada uma com o lugar:
   `(Silva, 2020, p. 12)`, ou, com duas fontes, `(Silva, 2020, p. 12; Souza, 2019,
   slide 3)`. O nome e o ano de cada fonte são os que a conferência das referências
   mostra; o lugar é o título da página na transcrição (`p. 12`, `slide 3`) ou a página da
   frase na base. Fonte sem páginas, como uma página da internet, vai sem lugar.
4. Rode o script. Ele não julga se a resposta está certa: confere só o que é mecânico. O
   resto é a pessoa que confere, na conferência dos cartões.

**Como rodar.**

    python scripts/confere_cartoes.py

**O que aparece.** Uma linha `ERRO` pra cada coisa que não bate: cartão sem prova, prova
sem cartão (a pergunta mudou só de um lado), chamada que não é de nenhuma fonte, lugar
que a fonte não tem, trecho que não está no lugar citado, lugar citado sem trecho, prova
que diz que a fonte afirma quando a base marca o trecho como possibilidade. Na
comparação, a quantidade de espaços, as quebras de linha e as marcas de destaque
(itálico, negrito) não contam; as letras e a pontuação contam. No
fim, quantos cartões há, quantos têm erro e quantos estão sem o tique da pessoa. A
conferência (no modelo, `CONFERENCIA-CARTOES.md`, na pasta das transcrições) mostra cada
cartão com a pergunta, a resposta, a fonte, os trechos e onde cada um foi achado. Se o
cartão, a prova ou o texto da fonte mudarem depois do tique, o tique sai.

Usa só o Python: não precisa instalar nada.

## `montar_deck.py` — das planilhas de pergunta ao baralho do Anki

**Pra que serve.** Transforma cada planilha de perguntas (no modelo, os arquivos
`perguntas-*.csv` de `docs/material-gerado/`) num baralho pronto pra importar no Anki —
um arquivo `.apkg`, que aparece em `anki-decks/`. No Anki, os cartões ficam numa pasta
com o nome da disciplina, que vem do formato da disciplina, e dentro dela uma pasta pra
cada planilha: planilhas e disciplinas diferentes nunca se misturam. As colunas
`pergunta` e `resposta` são obrigatórias; qualquer outra vira campo do cartão, e a
`fonte`, com a citação do fato, aparece atrás do cartão, embaixo da resposta. Duas coisas
você escolhe no `projeto.json`: em `colunas_ocultas`, as colunas que ficam guardadas no
cartão sem aparecer (no modelo, `ordem`); e em `coluna_subdecks`, uma coluna que separa
os cartões de cada planilha em pastas menores, uma pra cada valor que aparece nela — ou
`null`, pra não separar. A aparência dos cartões vem do arquivo de estilo do projeto (no
modelo, `estilo-cartao.css`).

**Quando usar.** Com as planilhas prontas e conferidas, e de novo sempre que uma
planilha mudar.

**Como rodar.**

    python scripts/montar_deck.py

Também dá pra gerar só uma planilha (`python scripts/montar_deck.py [parte do nome]`) ou
só ver quais seriam usadas, sem gerar nada (`python scripts/montar_deck.py --listar`).

**O que aparece.** Cada baralho gerado, com as pastas e quantos cartões tem. Uma planilha
sem a coluna `pergunta` ou `resposta` aparece com `ERRO` e fica sem baralho. Pra usar,
abra o Anki e arraste o arquivo `.apkg` pra dentro dele (ou use o menu
**Arquivo → Importar**).

Precisa da biblioteca `genanki`.

## `comum.py`

Não se roda: é a parte que os outros scripts compartilham (achar o `projeto.json` e as
planilhas de pergunta, ler o registro da fonte, guardar os tiques).

---

*Este documento está licenciado sob [CC BY-NC-SA 4.0](../LICENSE-CONTENT.txt).*
