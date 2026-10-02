# Metodologia de Conteúdo

Guia prático de como montar e auditar o conteúdo de uma disciplina neste tipo de
projeto: dado que você tem material de aula de uma disciplina disponível, o que fazer
com ele pra chegar num material de estudo estruturado, de um jeito consistente entre
disciplinas diferentes.

Este documento é escrito sem amarrar a nenhuma disciplina específica — onde um exemplo
ajuda a entender uma instrução, ele é descrito de forma abstrata, não com conteúdo real
de nenhuma matéria.

Siga isto por padrão, mas corrija quando sua disciplina expuser um caso que não está
coberto aqui. Quando isso acontecer, atualize este documento também, não só o conteúdo
da sua disciplina.

Os caminhos de pasta e de arquivo citados aqui são os do modelo. Em cada projeto, quem
diz onde fica cada coisa é o `projeto.json`, na raiz dele: é dali que os scripts tiram
todo caminho (ver o [README dos scripts](scripts/README.md)).

As seções seguem a ordem do trabalho, que é uma cadeia: o formato da disciplina dá a
grade de tudo (seção 1); cada fonte vira uma transcrição conferida e uma referência
(seções 2 a 4); das transcrições e da base do material de fora nascem os documentos
(seções 5 a 8) e, dos documentos, os cartões (seções 9 e 10); e tudo passa primeiro por
uma análise mecânica, feita por script, e depois pela análise humana (seção 11). Cada
etapa nasce da anterior, nunca direto da fonte, e a pessoa é sempre o último elo da
conferência.

---

## 1. Descubra o formato da disciplina

Antes de qualquer material, decida o formato da disciplina: o curso, a disciplina e o
nível de estudo; os itens; os eixos da ficha e os subtópicos de cada um; os elos do
dicionário; e as colunas dos cartões. O [Descubra seu modelo](DESCUBRA-SEU-MODELO.md) traz
as perguntas, e as respostas vão para `docs/formato.json`, conferido com `python
scripts/validar_dados.py docs/formato.json`. Uma IA pode propor cada resposta, dizendo
por que ela cabe naquele curso e naquele nível; a decisão é da pessoa.

Esse arquivo é a grade de tudo o que vem depois: é por ele que se sabe o que cada item
precisa ter, o que a aula cobre e onde falta, antes de qualquer material ser escrito.

---

## 2. Trate as fontes da aula

Guarde o material de aula original da disciplina — slides, apostila, ou o que for —
numa pasta própria (`material-base/`, por convenção). Essa pasta carrega um arquivo
pequeno e próprio dela, `docs/material-base/README.md`, que só documenta a convenção
dessa pasta específica. Nunca disponibilize a pasta `material-base/` publicamente: quem olha o projeto de fora
normalmente não vai ver o conteúdo dela nem saber o que tem lá — ela existe só
localmente, pra você, enquanto organiza aquela disciplina.

Faça uma transcrição integral e literal desse material, usando OCR se ele estiver
digitalizado como imagem ou PDF escaneado (OCR é uma tecnologia que lê o texto de uma
imagem e devolve como texto comum). Essa transcrição não é opcional, com ou sem ajuda
de IA: ela é o que permite conferir, depois, que nada do material ficou de fora do que
você escreveu — texto literal e completo é mais fácil de conferir contra o que foi
escrito do que voltar num PDF escaneado toda vez. Guarde essa transcrição também sem
disponibilizar publicamente, no padrão de *Como transcrever*, logo abaixo.

Ao escrever o conteúdo de estudo — sozinho, ou com ajuda de um assistente de IA, o que
preferir — leia o material inteiro antes de escrever qualquer coisa, sem usar nenhuma
ferramenta que corte ou resuma automaticamente o texto antes dessa leitura completa
acontecer. Nunca invente ou deduza um fato que não esteja escrito no material — se um
dado parecer faltar ou for ambíguo, pergunte a alguém, não adivinhe.

Faça todo fato relevante do material original aparecer em algum dos três documentos da
[seção 5](#5-escreva-três-documentos-de-conteúdo). Você pode deixar de fora elementos
puramente decorativos (piadas, mascotes, créditos de imagem) que não carregam
informação nenhuma — a linha é "isto é um fato" contra "isto é só enfeite", não "isto
parece pouco importante".

Se o nome de um arquivo de origem não bater com o conteúdo real dele, corrija o nome do
arquivo (registrando essa correção em algum lugar), em vez de conviver com o nome
errado.

### Como transcrever

Transcreva página por página (ou slide por slide), marcando duas coisas em cada uma: a
posição dela no arquivo, que é por onde se acha a imagem pra conferir, e o número
impresso na própria página, que é o que a citação usa. Os dois costumam ser diferentes
(capa, ficha técnica e páginas em algarismos romanos contam no arquivo, mas não na
numeração impressa). Quando a página não tem número impresso, como costuma acontecer
com slides, a citação usa a posição dela no arquivo, como slide. Entra todo texto que
está escrito na página, inclusive o de dentro de figuras, tabelas e esquemas, e cada
item junto do rótulo que lhe dá contexto (o título da lista, a legenda, o cabeçalho da
coluna), porque um item solto pode mudar de sentido. Não entra nada que não esteja
escrito: nem descrição de imagem, nem explicação, nem correção. Guarde a transcrição em
`docs/material-base/gerados-ocr/` e, assim que ela for criada, registre no topo dela de
qual arquivo veio, com `python scripts/registrar_fonte.py [transcrição] [arquivo
original] [chave]`. A chave é a mesma da referência dessa fonte (ver a
[seção 3](#3-cite-cada-fonte-conforme-a-abnt)); o script grava a chave, o caminho do
arquivo e a impressão digital dele (o hash), e em seguida atualiza as referências. É
esse registro que liga a transcrição ao original, não o nome dos arquivos.

Cada página vira uma seção da transcrição, com o título no formato
`## [como a citação chama a página] (arquivo p. [posição no arquivo])` — por exemplo,
`## p. 12 (arquivo p. 14)` ou `## slide 3 (arquivo p. 3)`. Uma página sem texto nenhum
fica com a seção e a marca `[sem texto]`.

Um fato que só a imagem mostra, sem texto, não está na transcrição. Se ele precisar
entrar no material, a prova dele é a própria imagem, conferida por uma pessoa, ou uma
fonte de fora que o diga por escrito.

Antes de usar a transcrição como base, ela é conferida contra a imagem de cada página:
OCR e IA trocam letras, pulam linhas e às vezes escrevem o que não está lá. Com a
transcrição pronta, gere o arquivo de conferência (`python scripts/conferencia.py`). Ele
nasce das transcrições, não do PDF, e mostra, página por página, a imagem da página no
arquivo registrado e o que a transcrição tem pra ela — se não tem nada, aparece vazio —,
com duas caixas de tique, uma pra IA e outra pra pessoa. O script não julga o conteúdo:
quem confere é quem tica. A IA pode ticar primeiro, como uma primeira passada; a pessoa é
sempre o último elo, e nenhuma página vale como conferida sem o tique dela. Se o texto
de uma página ou o arquivo original mudar depois do tique, o tique é retirado. Até essa
conferência, a transcrição não prova nada.

---

## 3. Cite cada fonte, conforme a ABNT

Todo documento que escreve algo tirado de uma fonte — teoria fundamental, dicionário,
ficha, planilha de perguntas — cita essa fonte ali mesmo, junto do fato, segundo a norma
de citações (no Brasil, a ABNT NBR 10520, no sistema autor-data): a mesma entrada da
referência (o autor, a instituição ou, sem autor, o começo do título), o ano e o local
do trecho: a página impressa no documento ou, se ela não tiver número impresso, a
posição do slide no arquivo. Diga o fato com suas palavras; se precisar transcrever
literalmente, use aspas e só um trecho curto, como a norma manda. Na planilha, a
citação vai numa coluna `fonte`, que aparece no cartão, e a resposta é sempre com
palavras próprias ([seção 9](#9-cartões-de-revisão-espaçada)). A chamada de cada fonte —
o nome e o ano, já com o *et al.* e as letras de desempate quando a norma pede — sai
pronta na conferência das referências; o que cada norma pede, item por item, e o que cabe
ao script, aos dados e a quem escreve, está nas [Regras da ABNT](regras-abnt.md).

As referências completas de todas as fontes citadas — as aulas e o material de fora —
ficam num documento só, `docs/FONTES.md`, como a lista de referências do fim de um
trabalho: em ordem alfabética, segundo a norma de referências (ABNT NBR 6023), e nada
além delas. Ele não diz onde cada fonte foi usada, porque isso é o papel da citação em
cada documento, nem onde a cópia está guardada. Toda citação tem a referência ali, e
toda referência é citada em algum lugar. Por exemplo:

```
[TÍTULO da aula]. [S. l.: s. n.], [20--]. 1 arquivo PDF ([n] slides). Material de aula, não publicado.

[AUTOR OU INSTITUIÇÃO]. [Título]. [Local]: [editora], [ano]. Disponível em: [endereço]. Acesso em: [data].
```

Esse documento é conteúdo do projeto e é versionado: o que fica fora do controle de
versão é a cópia do material, não a referência a ele.

Ninguém escreve esse documento à mão. Os dados de cada fonte — autoria, título, local,
editora, data, endereço, data de acesso, com uma chave curta — ficam em
`docs/fontes.json` (copiado de `modelo-dados/fontes.json`), e `python
scripts/referencias.py` monta cada referência pela norma, em ordem alfabética, e grava o
`docs/FONTES.md`. Junto, ele gera a conferência das referências: cada referência e a
chamada dela como ficaram, ao lado da cópia registrada da fonte (a primeira página, se
for PDF), com uma caixa de tique pra IA e outra pra pessoa. Confira cada referência contra
a folha de rosto ou a página do documento; se a referência, a chamada ou a cópia mudarem
depois do tique, o tique é retirado.

---

## 4. Complete a aula com material de fora

Se o material de aula não trouxer o que algum eixo da ficha pede pra um item (ver
[seção 5](#5-escreva-três-documentos-de-conteúdo)), busque esse fato num material de fora
— de preferência um documento oficial ou de referência da área. O material de fora
completa a aula, não a substitui: use-o só onde a aula não chega. Vale a mesma regra da
aula: o fato tem de estar escrito nesse material, nunca deduzido.

Guarde uma cópia de cada material de fora junto do material de aula, numa subpasta
própria (`docs/material-base/fontes-externas/`, por convenção), também sem versionar nem
disponibilizar publicamente: ele também não é de quem mantém o projeto. Dê a cada cópia
um nome que comece pela entrada e pelo ano da referência dela, pra achar o arquivo a
partir da citação.

Do material de fora, faça também uma base literal, item por item — e ninguém copia
trecho à mão. No arquivo de dados do item (`docs/bases/[item].json`, copiado de
`modelo-dados/base.json`), declare quais páginas de quais fontes foram lidas e marque
cada subtópico da grade do formato como coberto pela aula, pelo material de fora ou como
lacuna. `python scripts/base_externa.py` recolhe todo o texto dessas páginas, sem
filtro, separado em frases, cada uma com um código; a IA classifica cada frase — usada
(com o subtópico e se a fonte afirma ou trata como possibilidade), de outro item,
repetida, fora do recorte ou não é conteúdo —, e o script grava a base do item, só com
as frases usadas, letra por letra, com a citação e a página. Ele recusa frase sem classe,
subtópico sem marca, subtópico do material de fora sem frase nenhuma e frase usada onde
a aula já cobre ou num subtópico marcado como lacuna, e não grava a base enquanto houver
erro. A base e a conferência dela — cada página com as frases e a classe de
cada uma, com tique da IA e da pessoa — ficam fora do controle de versão; o arquivo de
dados, que só tem códigos e decisões, é versionado. É contra essa base que se confere
cada fato tirado do material de fora, e frase que a fonte trata como possibilidade entra
no material com a ressalva escrita, nunca como certeza.

---

## 5. Escreva três documentos de conteúdo

Escreva, no mínimo, três documentos pra cada disciplina, cada um com uma função própria
e exclusiva. Nos três, todo fato tirado de uma fonte leva a citação dela, como diz a
[seção 3](#3-cite-cada-fonte-conforme-a-abnt):

### A) Teoria fundamental

Escreva aqui o que vem **antes** de qualquer item específico: classificação geral,
conceitos comuns a toda a disciplina, categorias que os itens específicos vão usar sem
precisar redefinir. Organize em seções por tema, não uma seção por item. Você pode
citar um item específico como exemplo de um conceito geral, mesmo que esse item não
tenha (ainda, ou nunca venha a ter) seu próprio dicionário ou ficha — isso é esperado.
Escreva mais de um documento de teoria fundamental se a disciplina tiver mais de um
ramo claramente distinto de conteúdo introdutório.

### B) Dicionário de gatilhos

Escreva uma entrada por item específico, contando o item como uma história contínua,
dividida em partes que você vai chamar de **elos**. Em cada elo, explique o motivo que
leva ao elo seguinte — de forma que dê pra deduzir o item a partir de qualquer ponto da
história, em vez de decorar fatos soltos.

Decida quantos elos usar (a mesma quantidade pra todo item da sua disciplina) e dê um
nome a cada um. O processo central que um item passa muda completamente conforme o
assunto, então o elo do meio — o que faz aquele item "funcionar" — vai precisar de um
nome que só faz sentido pra sua disciplina; não herde o nome que outra disciplina usou.

Escreva num tom narrativo, em prosa corrida, sem tom pessoal e sem comentar sobre o
próprio texto (não escreva algo como "isto é uma lista completa"). Citar a fonte de um
fato não é comentar o texto: a citação continua valendo aqui, junto de cada fato que
veio de uma fonte. Sempre que um item usar uma categoria que você já definiu no
documento de teoria fundamental, cite essa categoria pelo nome (ver
[seção 7](#7-cite-uma-categoria-em-vez-de-redefinir)) em vez de explicá-la de novo ali.

### C) Ficha determinística

Reorganize os mesmos itens do dicionário numa tabela seca e direta. Use sempre o mesmo
conjunto de linhas — que você vai chamar de **eixos** — pra todo item da disciplina.
Isso é o que faz a ficha boa pra revisão rápida, ao contrário do dicionário, que é bom
pra entender o porquê.

Decida quantos eixos usar e o nome de cada um, do mesmo jeito que decidiu os elos do
dicionário. Dentro da sua disciplina, todo item tem a mesma quantidade de eixos — mas
esse número, e o nome de cada eixo, são uma escolha sua: outra disciplina pode escolher
um número diferente e nomes completamente diferentes.

Cubra, na ficha, o mesmo conteúdo principal do dicionário — mas não se limite a ele:
inclua aqui o detalhe que não cabe bem numa história corrida (números, listas
completas, critérios exatos). Siga a mesma regra de tom e de citação de categorias do
dicionário.

---

## 6. Mostre o mesmo conteúdo em dois níveis

Dicionário e ficha não são dois conteúdos independentes — são duas formas de contar o
mesmo conjunto de fatos principais sobre o mesmo item. No dicionário, conte só os fatos
que sustentam a história em cadeia. Na ficha, repita esses mesmos fatos, eixo por eixo,
e adicione o que a história não precisava citar pra fazer sentido.

Faça um fato principal de um item aparecer nos dois documentos, com a mesma conclusão —
só com mais ou menos detalhe. Se você perceber um fato que aparece nos dois documentos
de formas contraditórias (não apenas com detalhe diferente), corrija — isso é um erro.
O dicionário não precisar citar um detalhe que só está na ficha não é erro.

---

## 7. Cite uma categoria, em vez de redefinir

Se o seu documento de teoria fundamental define uma categoria (um grupo, um tipo de
processo, uma classificação), e um item específico se encaixa nela, cite o nome dessa
categoria no dicionário e na ficha desse item, em vez de descrever a mesma coisa de
novo sem nomeá-la.

Fazendo isso, você evita repetir a mesma explicação em todo item que usa aquela
categoria, garante que o documento de teoria fundamental realmente define tudo que os
itens vão precisar, e cria um caminho direto pra quem esqueceu o que a categoria
significa. Se você usar um conceito de teoria fundamental num item sem citar esse
conceito pelo nome em nenhum documento desse item, corrija — isso é uma lacuna.

---

## 8. Escreva um arquivo novo só quando a função for nova

Antes de criar um documento novo, pergunte a si mesmo: que função esse conteúdo cumpre,
e algum dos três tipos da [seção 5](#5-escreva-três-documentos-de-conteúdo) já cumpre
essa função?

Se o conteúdo for teoria geral — não a história de um item específico (dicionário), nem
a tabela de um item específico (ficha) —, coloque-o como uma seção dentro do documento
de teoria fundamental, mesmo que essa teoria tenha vindo de uma parte separada do
material de aula original; não crie um arquivo à parte só por isso. Só crie um arquivo
novo quando a função em si for genuinamente nova, sem nenhum dos três tipos cobrindo
ela — e nesse caso, descreva esse quarto tipo aqui também, porque ele passa a valer pra
qualquer disciplina futura que usar este documento.

---

## 9. Cartões de revisão espaçada

Um cartão de revisão espaçada é uma técnica de estudo: uma pergunta de um lado, uma
resposta do outro, revisada em intervalos crescentes de tempo, num programa como o
Anki (gratuito, disponível pra computador e celular). Isso é opcional — nem toda
disciplina precisa ter cartões, mas quem tiver, siga o resto desta seção.

As perguntas ficam guardadas numa planilha CSV: um arquivo de texto simples,
organizado em linhas e colunas como uma tabela (abre e edita no Excel, no Google
Sheets, ou como texto comum), com uma pergunta por linha. Nomeie o arquivo começando
sempre com a mesma primeira parte, em toda planilha do projeto — por exemplo,
`perguntas-` no início de `perguntas-fundamentos.csv` e de `perguntas-nucleo.csv`.
Assim, o script da [seção 10](#10-peça-um-script-em-vez-de-escrever-um) sabe quais
arquivos são planilhas de pergunta só pelo nome, sem que ninguém precise listar cada
arquivo um por um dentro do código.

Você não precisa extrair essas perguntas à mão. Envie o dicionário e a ficha (já
escritos, seção 5) pra um assistente de IA, com uma instrução como esta:

> A partir do dicionário de gatilhos e da ficha determinística em anexo, gere uma
> planilha CSV de perguntas e respostas de revisão espaçada. Use uma coluna `pergunta`,
> uma `resposta`, escrita com palavras próprias, e uma `fonte`, com a citação que o fato
> já tem no dicionário ou na ficha (as três obrigatórias), mais as colunas [nomeie as
> que fizerem sentido pra sua disciplina — por exemplo, o que identifica o item, o tipo
> de pergunta]. Para cada item específico, gere uma quantidade pequena e fixa de perguntas (a
> mesma quantidade pra todo item da disciplina), cobrindo os fatos de maior valor de
> revisão espalhados pelos diferentes elos/eixos daquele item — não repita sempre o
> mesmo tipo de pergunta pra todos os itens se isso deixar de fora um fato importante e
> específico de um item em particular. Para a teoria fundamental, gere uma pergunta pra
> cada conceito testável, já que cada conceito aparece uma única vez. Não invente
> nenhum fato que não esteja no texto do dicionário/ficha fornecido. Na coluna `fonte`,
> ponha só as chamadas, cada uma com a página ou o slide. Gere também a prova de cada
> pergunta, no arquivo de prova: a pergunta igual à da planilha, o trecho da
> transcrição ou da base do material de fora que diz o fato, copiado letra por letra, e
> se a fonte afirma (`categorica`) ou trata como possibilidade (`possibilidade`).

A prova fica num arquivo por planilha, copiado de `modelo-dados/prova.json`. Como ela
tem texto de terceiros, fica com o material de base, fora do controle de versão
(`docs/material-base/gerados-ocr/provas/`, por convenção). Quando a fonte trata o fato
como possibilidade, a resposta do cartão diz isso: nenhum cartão apresenta como certo o
que a fonte não afirma. `python scripts/confere_cartoes.py` confere cada cartão contra a
prova — se o trecho está, letra por letra, no lugar que a citação do cartão diz, e se
não falta prova pra nenhum cartão nem cartão pra nenhuma prova — e gera a conferência dos
cartões, com tique da IA e da pessoa.

Depois, confira a planilha lado a lado com o dicionário e a ficha, e cada cartão na
conferência dos cartões: a planilha cobre tudo que deveria cobrir, sem inventar nem
perder nada? A resposta de cada cartão diz o que o trecho diz, com a ressalva quando a
fonte trata como possibilidade? Essa conferência é sua, não da IA — é o que garante que
nada ficou de fora.

Uma vez com a planilha pronta e conferida, o baralho do Anki será gerado automaticamente
por um script criado e acionado por você (veja seção 10). Você pode editar um cartão direto dentro do app Anki — mas se
depois você mudar a planilha (ou o dicionário/ficha de origem) e rodar o script de
novo, o cartão é gerado de novo a partir da planilha, e essa edição feita direto no
Anki não sobrevive em caso de enviar novamente o baralho recriado pelo script para o app. Ou seja: enquanto você for regenerando o baralho a partir da
planilha, é a planilha (ou o dicionário/ficha) que precisa estar certa com suas modificações. 

Então se você precisa modificar um baralho, saiba qual o cartão ou quais os cartões, dê instruções para a IA que você usa ou altere você mesmo direto no CSV (no caso de IA, confira o que ela criar). Em seguida recrie o deck utilizando o script.

---

## 10. Peça um script, em vez de escrever um

Depois que a planilha da seção 9 existe, falta um último passo mecânico: ler cada linha
dela e montar o arquivo `.apkg` que o Anki importa. Esse passo é sempre o mesmo tipo de
trabalho, não importa a disciplina — por isso é feito por um script (um programa de
computador que faz um trabalho automático e repetitivo), em vez de à mão: rodando o
script de novo, o baralho inteiro é reconstruído em segundos toda vez que a planilha
mudar.

Você não precisa saber programar pra ter esse script, nem entender tecnicamente tudo
que a instrução abaixo pede — ela é pra copiar e enviar, não pra decifrar. Envie-a pra
um assistente de IA: o mesmo que te ajudou a escrever o conteúdo, um assistente de IA
integrado ao editor de código, ou um assistente de IA comum na internet. Se um script
assim já existir (reaproveitado de outra disciplina), use-o sem editar, antes de pedir
um novo.

> Escreva um script em Python que:
> 1. Encontre sozinho, na pasta do material gerado que o `projeto.json` do projeto
>    indica, todos os arquivos CSV cujo nome comece com o prefixo que o mesmo arquivo
>    indica (ex.: `perguntas-`) — sem que ninguém precise listar nomes de arquivo ou de
>    pasta dentro do código.
> 2. Para cada arquivo encontrado, gere um baralho do Anki (`.apkg`) separado, com um
>    cartão por linha. Toda planilha tem uma coluna `pergunta` (frente do cartão) e uma
>    `resposta` (verso). Qualquer outra coluna que existir no arquivo também deve virar
>    um campo do cartão, com esse mesmo nome — os nomes dessas colunas variam de
>    planilha pra planilha, e o script não deve esperar nenhum nome específico. A única
>    exceção é a coluna `fonte`, com a citação do fato: se existir, ela aparece no
>    verso, abaixo da resposta.
> 3. Não escreva, em nenhum lugar do código, o nome de uma disciplina, de um item
>    específico, um caminho de pasta ou uma quantidade de perguntas fixada — descubra
>    tudo a partir do `projeto.json` e do que
>    existir nos arquivos a cada execução, pra funcionar com uma planilha nova sem
>    precisar editar o código.
> 4. Gere o identificador de cada baralho (o ID que o Anki usa internamente)
>    automaticamente, a partir de um hash do nome do arquivo — nunca escolhido à mão.

O que essa instrução garante, em termos simples: se você adicionar uma planilha nova,
com colunas de nomes diferentes das que usa hoje, e rodar o script de novo, ele gera os
cartões certos sem ninguém precisar abrir o código pra ajustar nada. E se duas
disciplinas diferentes gerarem baralhos, o Anki nunca vai confundir um com o outro,
mesmo que ninguém tenha escolhido os números de identificação à mão.

Teste isso: peça pra rodar o script contra uma planilha de teste com nomes de coluna
diferentes dos que sua disciplina usa (mantendo só `pergunta` e `resposta`) — se os
cartões saírem certos mesmo assim, está funcionando do jeito certo.

---

## 11. Confira: primeiro o script, depois a pessoa

Tudo o que a IA produz passa por duas análises antes de valer. A primeira é mecânica:
um script confere, sempre do mesmo jeito, o que dá pra conferir sem julgar — se o dado
tem a forma certa, se o trecho está na fonte, se nada falta dos dois lados. A segunda é
humana: a pessoa confere o conteúdo contra a fonte. O `validar_dados.py` confere a forma
de cada arquivo de dados, e cada um dos scripts abaixo grava um arquivo de conferência,
fora do controle de versão, com duas caixas de tique em cada parte: a da IA, uma
primeira passada, e a da pessoa, que é sempre o último elo.

| O que se confere | Contra o quê | Script | Arquivo de conferência (no modelo) |
|---|---|---|---|
| Cada página da transcrição | A imagem da página no original | `conferencia.py` | `CONFERENCIA-COM-IMAGEM.md` |
| Cada referência e a chamada dela | A folha de rosto ou a página da fonte | `referencias.py` | `CONFERENCIA-REFERENCIAS.md` |
| Cada frase do material de fora e a classe dela | A página da fonte | `base_externa.py` | `CONFERENCIA-TRECHOS.md` |
| Cada cartão | O trecho da prova, no lugar que a citação diz | `confere_cartoes.py` | `CONFERENCIA-CARTOES.md` |

Uma linha `ERRO` ou `FALTA` de um script se resolve antes de ticar: ela diz o que falta
ou não bate nos dados. O script nunca diz se um conteúdo está certo — isso é a análise humana, parte
por parte nas conferências e, no fim, na auditoria da
[seção 16](#16-checklist-auditando-uma-disciplina-existente). Nada vale como conferido
sem o tique da pessoa, e o tique sai sozinho se a parte mudar depois dele.

---

## 12. Documente o recorte que você escolheu

Não tente cobrir um tema por completo e de forma objetiva. Escolha quais itens entram,
o quão fundo cada um vai, e o que é mais importante — geralmente em torno de uma grade
curricular específica — e diga isso claramente no guia não técnico da disciplina, sem
esconder que é um julgamento seu.

Densidades diferentes entre tipos de documento não são, por si só, inconsistência: é
esperado que os cartões de revisão de um item específico
([seção 9](#9-cartões-de-revisão-espaçada)) tenham uma quantidade pequena e fixa,
enquanto os cartões de teoria fundamental sejam completos por conceito — desde que você
siga cada regra de forma consistente dentro dela mesma.

Não pule um fato do material original sem tocar nele em nenhum documento, e não deixe
dois documentos mostrarem o mesmo fato central de formas contraditórias — nenhuma das
duas coisas é aceitável sob a desculpa do recorte.

---

## 13. Escreva os quatro documentos de navegação raiz

Acompanhe toda disciplina de quatro documentos na raiz do projeto, com papéis fixos que
não mudam de disciplina pra disciplina — só o conteúdo dentro de cada seção muda (veja
[LEIA-ME](modelo-documentos-raiz/LEIA-ME.md) antes de adicionar os documentos):

| Documento | Papel fixo |
|---|---|
| `README.md` | Documentação técnica: o que é o projeto, aviso sobre o recorte, origem do material, licença, estrutura de arquivos, como usar, referências. |
| `INDICE.md` | Índice do projeto: lista e linka os documentos que existem (teoria fundamental, dicionário, ficha, planilhas, fontes), sem explicação. |
| `MANUAL.md` (ou equivalente não técnico) | Guia em níveis, sem jargão, pra quem só quer estudar. Abra com o aviso do recorte e tenha um canal pra reportar erro. |
| `NOTICE.md` | Mapa de licenciamento: qual licença cobre qual categoria de arquivo, e a exceção do material de terceiros. |

O índice da raiz lista documentos, não itens de dentro deles: cada documento de
conteúdo (teoria fundamental, dicionário, ficha) mantém seu próprio índice interno, no
topo do próprio arquivo, se tiver itens ou seções suficientes pra precisar de um. Sem
essa distinção, o índice da raiz cresce junto com o conteúdo e acaba duplicando a
estrutura de cada documento dentro de si mesmo.

Existe um esqueleto pronto desses quatro arquivos em `modelo-documentos-raiz/`, na raiz
deste repositório-modelo — copie-os pra raiz do projeto da disciplina nova e preencha
os colchetes, em vez de escrever cada um do zero (o `LEIA-ME.md` de dentro dessa pasta
explica a convenção com mais detalhe).

Ao adicionar uma disciplina nova a um projeto que já tem essa estrutura, edite as
seções desses quatro documentos com o conteúdo novo — não crie uma segunda versão
paralela deles, e não pule uma seção só porque a disciplina nova ainda não tem o
equivalente pronto (nesse caso, deixe a seção dizendo isso).

---

## 14. Licencie código, conteúdo e material de terceiros separadamente

Trate cada uma dessas três categorias com um papel fixo, independente de disciplina:

- **Código** (os scripts): escolha uma licença de código aberto que exija que qualquer
  trabalho derivado também seja aberto.
- **Conteúdo gerado** (teoria fundamental, dicionário, ficha, planilhas, o documento
  de fontes, e os documentos de metodologia): escolha uma licença de conteúdo que exija
  dar crédito.
- **Material de terceiros** (o material de aula original, sua transcrição literal, as
  cópias do material de fora, a base de trechos dele e a prova dos cartões — ver as
  seções [2](#2-trate-as-fontes-da-aula), [4](#4-complete-a-aula-com-material-de-fora) e
  [9](#9-cartões-de-revisão-espaçada)):
  não coloque sob nenhuma licença deste projeto, porque quem mantém o projeto não é
  quem escreveu esse material. Nunca disponibilize publicamente, de forma permanente —
  não "por enquanto".

Em todo arquivo de código e todo documento de conteúdo, indique de forma breve qual
licença o cobre — um comentário de uma ou duas linhas no topo do código, uma linha no
fim do documento de conteúdo. Deixe as planilhas e os arquivos de dados (JSON) fora
dessa regra: um comentário quebraria a leitura de quem abre o arquivo como tabela, e o
JSON nem aceita comentário.

---

## 15. Checklist: adicionando uma disciplina nova

1. Prepare o projeto: copie pra raiz dele, do modelo, a pasta `scripts/` inteira (com
   `esquemas/` e `normas/`), o `.gitignore`, o `LICENSE` e o `LICENSE-CONTENT.txt`, e
   `modelo-dados/projeto.json`, `modelo-dados/estilo-cartao.css` e
   `modelo-dados/fluxo-ia.json` — o `projeto.json` é o mapa de onde fica cada coisa, e os
   scripts tiram todo caminho dali (se mudar uma pasta de lugar, mude também o
   `.gitignore`, pra o material de terceiros continuar fora do GitHub); o estilo é a
   aparência dos cartões; o fluxo é o método em dados, que a IA lê (ver
   [Trabalhar com uma IA](trabalhar-com-ia.md)) — e ative o hook de commit: copie
   `.githooks/` pra raiz do projeto novo, adicione `.githooks/` ao `.gitignore` desse
   projeto (a pasta é ferramenta local de quem mantém, não faz parte do pacote
   versionado de cada disciplina — só é versionada aqui, no modelo, que é a fonte de
   onde ela é copiada) e rode `git config core.hooksPath .githooks` mais `git config
   commit.template .githooks/commit-template.txt` uma vez (ver `.githooks/README.md`).
2. Guarde o material de aula original por convenção e decida o formato da disciplina
   (seção 1): o nome do elo central do dicionário e os nomes dos eixos da ficha — tome
   essa decisão de forma explícita, sem herdar de outra disciplina — gravados em
   `docs/formato.json`, como diz o `DESCUBRA-SEU-MODELO.md`.
3. Transcreva o material de aula por inteiro, literalmente, e confira a transcrição,
   página por página, no arquivo de conferência (seção 2); grave os dados da referência
   de cada aula em `docs/fontes.json` (seção 3) e leia tudo antes de escrever qualquer
   coisa.
4. Marque, item por item, o que a aula cobre de cada subtópico da grade; onde não
   cobrir, complete com material de fora, guardado, com base de trechos e citado (seções
   3 e 4).
5. Escreva o documento de teoria fundamental primeiro — é onde as categorias que os
   itens específicos vão citar precisam estar definidas (seção 5).
6. Escreva dicionário e ficha por item, citando os termos de teoria fundamental que se
   aplicam a cada um (seções 5 a 7).
7. Gere as planilhas a partir do dicionário/ficha, com a prova de cada cartão, rode a
   conferência dos cartões e confira se as planilhas cobrem tudo que deveriam cobrir
   (seção 9).
8. Reaproveite um script existente, ou peça um novo (seção 10), pra gerar o baralho.
9. Atualize as quatro seções correspondentes nos quatro documentos de navegação raiz
   (seção 13).
10. Faça a auditoria de consistência (seção 16) antes de considerar a disciplina pronta.

## 16. Checklist: auditando uma disciplina existente

### Análise mecânica

1. Rode `python scripts/validar_dados.py` em cada arquivo de dados do projeto, e
   `conferencia.py`, `referencias.py`, `base_externa.py` e `confere_cartoes.py`: nenhum
   deles pode deixar linha `ERRO` nem `FALTA` (ver a
   [seção 11](#11-confira-primeiro-o-script-depois-a-pessoa)).

### Análise humana

1. Confira se o título de cada documento cobre 100% do que está dentro dele.
2. Pegue um item específico: confira se o dicionário e a ficha mostram os mesmos fatos
   principais, sem contradição entre eles.
3. Procure um termo definido em teoria fundamental que algum item usa implicitamente
   sem citar pelo nome em nenhum documento desse item.
4. Procure um arquivo cujo nome não corresponda a nenhuma das funções da seção 5.
5. Confira se os quatro documentos de navegação raiz têm as mesmas seções que outras
   disciplinas já cobertas, mesmo que o conteúdo ainda seja "isto não foi feito ainda".
6. Procure um fato do material original que não apareça em nenhum documento gerado.
7. Confira a planilha de perguntas linha por linha contra o dicionário/ficha de origem
   — procure um fato inventado que não está na fonte, ou um fato da fonte que ficou de
   fora — e veja se cada cartão tem prova, sem erro e com o tique da pessoa, na
   conferência dos cartões.
8. Confira as citações: todo fato tirado de uma fonte, em qualquer documento ou cartão,
   cita essa fonte; toda citação tem a referência em `docs/FONTES.md`; toda referência
   de lá é citada em algum lugar e tem o tique da pessoa na conferência das referências;
   e a cópia de cada material de fora está guardada em
   `docs/material-base/fontes-externas/`.
9. Confira a base literal: a transcrição de cada página tem só o que está escrito nela,
   com a posição no arquivo e o número impresso, e tem o tique da pessoa no arquivo de
   conferência; o arquivo de base de cada item não deixa frase sem classe nem subtópico
   sem marca, e cada página da conferência dos trechos tem o tique da pessoa.

---

## 17. Isto não é definitivo

Siga cada seção acima como o que já funcionou, não como uma imposição. Se sua
disciplina tiver uma necessidade genuína que não se encaixa bem em algum ponto deste
guia, mude o guia — e registre a mudança aqui, com o motivo, pra que a próxima pessoa
se beneficie dela em vez de reabrir a mesma discussão.

---

*Este documento está licenciado sob [CC BY-NC-SA 4.0](LICENSE-CONTENT.txt).*
