# Modelo de núcleo de conteúdo por recorte

Este modelo é um ponto de partida pra montar o material de estudo de qualquer disciplina
de graduação a partir do material de aula dela: documentos que explicam a matéria, uma
tabela de revisão por assunto e cartões de perguntas e respostas pra estudar no Anki (um
programa gratuito de revisão, pra computador e celular). Pra usar, comece pelos dois
primeiros itens da lista abaixo, nessa ordem.

Você não precisa saber programar. Algumas partes do trabalho são feitas por pequenos
programas que vêm prontos no modelo — os *scripts* —, e cada passo de como usá-los está
explicado em palavras simples.

## Uso de IA

O método deste modelo usa IA na produção do material: propor o formato da disciplina
(no [Descubra seu modelo](DESCUBRA-SEU-MODELO.md)), transcrever o material de aula,
redigir os documentos, gerar as perguntas e, quando for preciso, escrever um script novo
(seções 2 a 10 da [metodologia](metodologia-de-conteudo.md)). O que a IA produz não vira
material final direto: passa primeiro por uma análise mecânica, a que um script consegue
fazer sempre do mesmo jeito, e depois pela análise humana, contra o material de origem (o
que é uma e o que é outra em cada etapa está na
[seção 11 da metodologia](metodologia-de-conteudo.md#11-confira-primeiro-o-script-depois-a-pessoa)).
A escolha do que entra no material, a decisão sobre cada fato e a palavra final são de
uma pessoa.

Qualquer assistente de IA serve. Como usá-lo — gratuito ou pago, sozinho ou com vários
agentes trabalhando em equipe — é decisão de quem segue o modelo. Este modelo não ensina a
usar IA — só deixa claro onde ela entra: o [Trabalhar com uma IA](trabalhar-com-ia.md)
diz, etapa por etapa, o que pedir, o que entregar e o que conferir depois, e o
[método em dados](modelo-dados/fluxo-ia.json) é o arquivo que a IA lê pra seguir as
etapas.

## O que tem aqui

- **[Descubra seu modelo](DESCUBRA-SEU-MODELO.md)** — o primeiro passo: você diz o curso,
  a disciplina e o nível de estudo e responde, sozinho ou com ajuda de uma IA, às
  perguntas que decidem o formato do material, como os itens que a disciplina tem, os
  fatos que cada item precisa ter e o que cada cartão leva.
- **[Metodologia de conteúdo](metodologia-de-conteudo.md)** — o método inteiro, do
  material de aula ao cartão: o que vai em cada documento, como tratar o material de
  aula e como conferir, com as listas do que fazer numa disciplina nova e na revisão de
  uma disciplina pronta.
- **[Regras da ABNT](regras-abnt.md)** — o que as normas brasileiras de citação e de
  referência pedem, item por item, em palavras simples, e quem cuida de cada regra: o
  script, os dados das fontes ou quem escreve o texto.
- **[Trabalhar com uma IA](trabalhar-com-ia.md)** — o que pedir à IA em cada etapa, o
  que entregar a ela, o que conferir depois e o que é sempre seu, pra qualquer
  assistente de IA.
- **[Modelo dos documentos de apresentação](modelo-documentos-raiz/LEIA-ME.md)** — os
  quatro documentos que ficam na pasta principal do projeto da sua disciplina (a
  apresentação, o índice, o manual de uso e o aviso de licenças), prontos pra copiar e
  preencher.
- **[Modelo de dados](modelo-dados/)** — os arquivos que guardam as informações do
  projeto da sua disciplina, pra copiar e preencher: o [mapa do projeto](modelo-dados/projeto.json),
  que diz aos scripts onde fica cada coisa; o [formato](modelo-dados/formato.json), com
  as respostas do Descubra seu modelo; as [fontes](modelo-dados/fontes.json), com os
  dados de cada fonte, de onde saem as referências; a [base](modelo-dados/base.json) de
  um item, com o que foi lido do material de fora e a decisão sobre cada frase; a
  [prova](modelo-dados/prova.json) dos cartões de uma planilha, com o trecho da fonte que
  prova cada um; o [estilo dos cartões](modelo-dados/estilo-cartao.css), com a aparência
  deles no Anki; e o [método em dados](modelo-dados/fluxo-ia.json), que não se preenche:
  é copiado e entregue à IA.
- **[Material de base](docs/material-base/README.md)** — a pasta do material de aula, da
  transcrição dele e das cópias do material de fora que completa a aula. Nada dela é
  publicado, em lugar nenhum: esse material não é seu pra publicar.
- **[Scripts](scripts/README.md)** — os pequenos programas que fazem a parte mecânica do
  método, sempre do mesmo jeito: pra que serve cada um, quando usar e como rodar, passo a
  passo.
- **[Avisos de licença](NOTICE.md)** — o que você pode fazer com cada parte deste modelo.
  Em resumo: os scripts podem ser usados, mudados e repassados, desde que continuem
  abertos pra todo mundo ([licença dos scripts](LICENSE)); o resto pode ser usado e
  adaptado dando o crédito, sem fins comerciais e mantendo a mesma licença
  ([licença do conteúdo](LICENSE-CONTENT.txt)).

## Se você guarda o projeto no GitHub

O GitHub é um site que guarda um projeto na internet e o histórico de cada mudança nele.
Você não precisa dele pra usar o modelo. Se usar, duas coisas daqui servem pra você:

- **A lista do que nunca vai pro GitHub** — o arquivo `.gitignore`, que já vem pronto
  pra deixar de fora todo o material de aula e o material de fora.
- **[A conferência das mensagens](.githooks/README.md)** — cada vez que você grava uma
  versão do projeto pra mandar ao GitHub, escreve uma mensagem dizendo o que mudou. Este
  verificador, opcional, confere se a mensagem tem um título e uma explicação em texto
  corrido, pra que o histórico do projeto se leia como uma história.

---

*Este modelo está licenciado sob [CC BY-NC-SA 4.0](LICENSE-CONTENT.txt) — exceto os
programas (os scripts da pasta `scripts/` e o verificador de mensagens da pasta
`.githooks/`), sob [GPL-3.0](LICENSE).*
