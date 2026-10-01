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

---

## 1. Escreva três documentos de conteúdo

Escreva, no mínimo, três documentos pra cada disciplina, cada um com uma função própria
e exclusiva:

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
próprio texto (não escreva algo como "isto é uma lista completa", nem cite de qual
material a informação veio — isso fica nos documentos da raiz do projeto, não dentro do
texto de estudo). Sempre que um item usar uma categoria que você já definiu no
documento de teoria fundamental, cite essa categoria pelo nome (ver
[seção 3](#3-cite-uma-categoria-em-vez-de-redefinir)) em vez de explicá-la de novo ali.

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

## 2. Mostre o mesmo conteúdo em dois níveis

Dicionário e ficha não são dois conteúdos independentes — são duas formas de contar o
mesmo conjunto de fatos principais sobre o mesmo item. No dicionário, conte só os fatos
que sustentam a história em cadeia. Na ficha, repita esses mesmos fatos, eixo por eixo,
e adicione o que a história não precisava citar pra fazer sentido.

Faça um fato principal de um item aparecer nos dois documentos, com a mesma conclusão —
só com mais ou menos detalhe. Se você perceber um fato que aparece nos dois documentos
de formas contraditórias (não apenas com detalhe diferente), corrija — isso é um erro.
O dicionário não precisar citar um detalhe que só está na ficha não é erro.

---

## 3. Cite uma categoria, em vez de redefinir

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

## 4. Escreva um arquivo novo só quando a função for nova

Antes de criar um documento novo, pergunte a si mesmo: que função esse conteúdo cumpre,
e algum dos três tipos da [seção 1](#1-escreva-três-documentos-de-conteúdo) já cumpre
essa função?

Se o conteúdo for teoria geral — não a história de um item específico (dicionário), nem
a tabela de um item específico (ficha) —, coloque-o como uma seção dentro do documento
de teoria fundamental, mesmo que essa teoria tenha vindo de uma parte separada do
material de aula original; não crie um arquivo à parte só por isso. Só crie um arquivo
novo quando a função em si for genuinamente nova, sem nenhum dos três tipos cobrindo
ela — e nesse caso, descreva esse quarto tipo aqui também, porque ele passa a valer pra
qualquer disciplina futura que usar este documento.

---

## 5. Trate o material de aula original

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
disponibilizar publicamente.

Ao escrever o conteúdo de estudo — sozinho, ou com ajuda de um assistente de IA, o que
preferir — leia o material inteiro antes de escrever qualquer coisa, sem usar nenhuma
ferramenta que corte ou resuma automaticamente o texto antes dessa leitura completa
acontecer. Nunca invente ou deduza um fato que não esteja escrito no material — se um
dado parecer faltar ou for ambíguo, pergunte a alguém, não adivinhe.

Faça todo fato relevante do material original aparecer em algum dos três documentos da
[seção 1](#1-escreva-três-documentos-de-conteúdo). Você pode deixar de fora elementos
puramente decorativos (piadas, mascotes, créditos de imagem) que não carregam
informação nenhuma — a linha é "isto é um fato" contra "isto é só enfeite", não "isto
parece pouco importante".

Se o nome de um arquivo de origem não bater com o conteúdo real dele, corrija o nome do
arquivo (registrando essa correção em algum lugar), em vez de conviver com o nome
errado.

---

## 6. Cartões de revisão espaçada

Um cartão de revisão espaçada é uma técnica de estudo: uma pergunta de um lado, uma
resposta do outro, revisada em intervalos crescentes de tempo, num programa como o
Anki (gratuito, disponível pra computador e celular). Isso é opcional — nem toda
disciplina precisa ter cartões, mas quem tiver, siga o resto desta seção.

As perguntas ficam guardadas numa planilha CSV: um arquivo de texto simples,
organizado em linhas e colunas como uma tabela (abre e edita no Excel, no Google
Sheets, ou como texto comum), com uma pergunta por linha. Nomeie o arquivo começando
sempre com a mesma primeira parte, em toda planilha do projeto — por exemplo,
`perguntas-` no início de `perguntas-fundamentos.csv` e de `perguntas-nucleo.csv`.
Assim, o script da [seção 7](#7-peça-um-script-em-vez-de-escrever-um) sabe quais
arquivos são planilhas de pergunta só pelo nome, sem que ninguém precise listar cada
arquivo um por um dentro do código.

Você não precisa extrair essas perguntas à mão. Envie o dicionário e a ficha (já
escritos, seção 1) pra um assistente de IA, com uma instrução como esta:

> A partir do dicionário de gatilhos e da ficha determinística em anexo, gere uma
> planilha CSV de perguntas e respostas de revisão espaçada. Use uma coluna `pergunta`
> e uma `resposta` (obrigatórias), mais as colunas [nomeie as que fizerem sentido pra
> sua disciplina — por exemplo, o que identifica o item, o tipo de pergunta, de onde
> veio]. Para cada item específico, gere uma quantidade pequena e fixa de perguntas (a
> mesma quantidade pra todo item da disciplina), cobrindo os fatos de maior valor de
> revisão espalhados pelos diferentes elos/eixos daquele item — não repita sempre o
> mesmo tipo de pergunta pra todos os itens se isso deixar de fora um fato importante e
> específico de um item em particular. Para a teoria fundamental, gere uma pergunta pra
> cada conceito testável, já que cada conceito aparece uma única vez. Não invente
> nenhum fato que não esteja no texto do dicionário/ficha fornecido.

Depois de gerada, confira a planilha à mão, lado a lado com o dicionário e a ficha: ela
cobre tudo que deveria cobrir, sem inventar nem perder nada? Essa conferência é sua,
não da IA — é o que garante que nada ficou de fora.

Uma vez com a planilha pronta e conferida, o baralho do Anki será gerado automaticamente
por um script criado e acionado por você (veja seção 7). Você pode editar um cartão direto dentro do app Anki — mas se
depois você mudar a planilha (ou o dicionário/ficha de origem) e rodar o script de
novo, o cartão é gerado de novo a partir da planilha, e essa edição feita direto no
Anki não sobrevive em caso de enviar novamente o baralho recriado pelo script para o app. Ou seja: enquanto você for regenerando o baralho a partir da
planilha, é a planilha (ou o dicionário/ficha) que precisa estar certa com suas modificações. 

Então se você precisa modificar um baralho, saiba qual o cartão ou quais os cartões, dê instruções para a IA que você usa ou altere você mesmo direto no CSV (no caso de IA, confira o que ela criar). Em seguida recrie o deck utilizando o script.

---

## 7. Peça um script, em vez de escrever um

Depois que a planilha da seção 6 existe, falta um último passo mecânico: ler cada linha
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
> 1. Encontre sozinho, dentro de `docs/material-gerado/`, todos os arquivos CSV já
>    gerados cujo nome comece com o mesmo prefixo (ex.: `perguntas-`) — sem que ninguém
>    precise listar nomes de arquivo dentro do código.
> 2. Para cada arquivo encontrado, gere um baralho do Anki (`.apkg`) separado, com um
>    cartão por linha. Toda planilha tem uma coluna `pergunta` (frente do cartão) e uma
>    `resposta` (verso). Qualquer outra coluna que existir no arquivo também deve virar
>    um campo do cartão, com esse mesmo nome — os nomes dessas colunas variam de
>    planilha pra planilha, e o script não deve esperar nenhum nome específico.
> 3. Não escreva, em nenhum lugar do código, o nome de uma disciplina, de um item
>    específico, ou uma quantidade de perguntas fixada — descubra tudo a partir do que
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

## 8. Documente o recorte que você escolheu

Não tente cobrir um tema por completo e de forma objetiva. Escolha quais itens entram,
o quão fundo cada um vai, e o que é mais importante — geralmente em torno de uma grade
curricular específica — e diga isso claramente no guia não técnico da disciplina, sem
esconder que é um julgamento seu.

Densidades diferentes entre tipos de documento não são, por si só, inconsistência: é
esperado que os cartões de revisão de um item específico
([seção 6](#6-cartões-de-revisão-espaçada)) tenham uma quantidade pequena e fixa,
enquanto os cartões de teoria fundamental sejam completos por conceito — desde que você
siga cada regra de forma consistente dentro dela mesma.

Não pule um fato do material original sem tocar nele em nenhum documento, e não deixe
dois documentos mostrarem o mesmo fato central de formas contraditórias — nenhuma das
duas coisas é aceitável sob a desculpa do recorte.

---

## 9. Escreva os quatro documentos de navegação raiz

Acompanhe toda disciplina de quatro documentos na raiz do projeto, com papéis fixos que
não mudam de disciplina pra disciplina — só o conteúdo dentro de cada seção muda (veja
[LEIA-ME](modelo-documentos-raiz/LEIA-ME.md) antes de adicionar os documentos):

| Documento | Papel fixo |
|---|---|
| `README.md` | Documentação técnica: o que é o projeto, aviso sobre o recorte, origem do material, licença, estrutura de arquivos, como usar, referências. |
| `INDICE.md` | Índice do projeto: lista e linka os documentos que existem (teoria fundamental, dicionário, ficha, planilhas), sem explicação. |
| `MANUAL.md` (ou equivalente não técnico) | Guia em níveis, sem jargão, pra quem só quer estudar. Abra com o aviso do recorte e feche com um canal pra reportar erro. |
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

## 10. Licencie código, conteúdo e material de terceiros separadamente

Trate cada uma dessas três categorias com um papel fixo, independente de disciplina:

- **Código** (os scripts): escolha uma licença de código aberto que exija que qualquer
  trabalho derivado também seja aberto.
- **Conteúdo gerado** (teoria fundamental, dicionário, ficha, planilhas, e os
  documentos de metodologia): escolha uma licença de conteúdo que exija dar crédito.
- **Material de terceiros** (o material de aula original e sua transcrição literal):
  não coloque sob nenhuma licença deste projeto, porque quem mantém o projeto não é
  quem escreveu esse material. Nunca disponibilize publicamente, de forma permanente —
  não "por enquanto".

Em todo arquivo de código e todo documento de conteúdo, indique de forma breve qual
licença o cobre — um comentário de uma ou duas linhas no topo do código, uma linha no
fim do documento de conteúdo. Deixe as planilhas fora dessa regra: um comentário
quebraria a leitura de quem abre o arquivo só como tabela de dados.

---

## 11. Checklist: adicionando uma disciplina nova

1. Ative o hook de commit: copie `.githooks/` pra raiz do projeto novo, adicione
   `.githooks/` ao `.gitignore` desse projeto (a pasta é ferramenta local de quem
   mantém, não faz parte do pacote versionado de cada disciplina — só é versionada
   aqui, no modelo, que é a fonte de onde ela é copiada) e rode
   `git config core.hooksPath .githooks` mais `git config commit.template
   .githooks/commit-template.txt` uma vez (ver `.githooks/README.md`).
2. Guarde o material de aula original por convenção, com transcrição literal completa,
   e leia tudo antes de escrever qualquer coisa.
3. Decida o nome do elo central do dicionário e os nomes dos eixos da ficha — tome essa
   decisão de forma explícita, sem herdar de outra disciplina.
4. Escreva o documento de teoria fundamental primeiro — é onde as categorias que os
   itens específicos vão citar precisam estar definidas.
5. Escreva dicionário e ficha por item, citando os termos de teoria fundamental que se
   aplicam a cada um.
6. Gere as planilhas a partir do dicionário/ficha, e confira se cobrem tudo que
   deveriam cobrir.
7. Atualize as quatro seções correspondentes nos quatro documentos de navegação raiz.
8. Reaproveite um script existente, ou peça um novo (seção 7), pra gerar o material.
9. Faça a auditoria de consistência (seção 12) antes de considerar a disciplina pronta.

## 12. Checklist: auditando uma disciplina existente

1. Confira se o título de cada documento cobre 100% do que está dentro dele.
2. Pegue um item específico: confira se o dicionário e a ficha mostram os mesmos fatos
   principais, sem contradição entre eles.
3. Procure um termo definido em teoria fundamental que algum item usa implicitamente
   sem citar pelo nome em nenhum documento desse item.
4. Procure um arquivo cujo nome não corresponda a nenhuma das funções da seção 1.
5. Confira se os quatro documentos de navegação raiz têm as mesmas seções que outras
   disciplinas já cobertas, mesmo que o conteúdo ainda seja "isto não foi feito ainda".
6. Procure um fato do material original que não apareça em nenhum documento gerado.
7. Confira a planilha de perguntas linha por linha contra o dicionário/ficha de origem
   — procure um fato inventado que não está na fonte, ou um fato da fonte que ficou de
   fora.

---

## 13. Isto não é definitivo

Siga cada seção acima como o que já funcionou, não como uma imposição. Se sua
disciplina tiver uma necessidade genuína que não se encaixa bem em algum ponto deste
guia, mude o guia — e registre a mudança aqui, com o motivo, pra que a próxima pessoa
se beneficie dela em vez de reabrir a mesma discussão.

---

*Este documento está licenciado sob [CC BY-NC-SA 4.0](LICENSE-CONTENT.txt).*
