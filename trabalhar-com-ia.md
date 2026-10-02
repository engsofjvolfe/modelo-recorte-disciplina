# Trabalhar com uma IA

O método deste modelo usa IA em quase todas as etapas: propor o formato da disciplina,
transcrever as aulas, preencher os dados das fontes, escrever os documentos, gerar os
cartões. Este guia diz, etapa por etapa, o que pedir à IA, o que entregar a ela, o que
conferir depois e o que é sempre seu. Serve pra qualquer assistente de IA: o modelo não
depende de nenhum.

## Antes de começar: escolha como usar a sua IA

Cada IA tem os seus modos. Há versão gratuita e paga; há a que conversa no navegador e
a que trabalha dentro do editor, lendo as pastas do seu computador; há a que trabalha
sozinha e a que divide o trabalho entre vários agentes, como uma equipe. A escolha é
sua. O que muda de um modo pra outro é quanto a IA faz sozinha:

- **Se ela lê e escreve os arquivos do projeto**, ela mesma pode copiar arquivos,
  escrever as transcrições e rodar os scripts. Você confere o que ela fez.
- **Se ela só conversa**, você entrega cada arquivo na conversa, copia o que ela
  devolver pro arquivo certo e roda os scripts você mesmo (o
  [README dos scripts](scripts/README.md) explica como, passo a passo).

Nos dois casos, quem decide e quem dá a palavra final é você.

## Entregue o método à IA

O arquivo [`modelo-dados/fluxo-ia.json`](modelo-dados/fluxo-ia.json) é o método inteiro
em dados, escrito pra IA ler: as etapas na ordem, o que entra e o que sai de cada uma, o
script de cada etapa e as regras que valem sempre. Você não precisa ler esse arquivo;
basta entregá-lo.

1. Copie o `fluxo-ia.json` pra pasta principal do projeto da sua disciplina, junto do
   `projeto.json` (o mapa de onde fica cada coisa).
2. Na primeira conversa, entregue os dois arquivos e peça: "Leia o `fluxo-ia.json`
   inteiro e guarde na sua memória ou nas instruções do projeto."
3. Se a sua ferramenta não guarda nada de uma conversa pra outra, entregue o arquivo de
   novo no começo de cada conversa nova, com o pedido: "Releia este arquivo inteiro
   antes de continuar." O próprio arquivo pede isso à IA.

Se a IA não consegue abrir os arquivos do modelo, entregue também, em cada etapa, o
documento do modelo que ela indica (a seção da metodologia, o Descubra seu modelo, as
regras da ABNT).

E se você travar em qualquer passo — abrir o terminal, rodar um script, entender uma
mensagem que apareceu na tela —, peça ajuda à própria IA: descreva o que você fez e o
que apareceu, e peça o passo a passo pro seu computador.

## Etapa por etapa

Em cada etapa, a IA faz uma primeira passada e marca o tique dela nas conferências. O
tique que vale é o seu: nada está conferido sem ele (ver a
[seção 11 da metodologia](metodologia-de-conteudo.md#11-confira-primeiro-o-script-depois-a-pessoa)).

### 1. Preparar o projeto

- **Peça:** que copie do modelo pra pasta principal do projeto a pasta `scripts/`
  inteira, a lista do que nunca vai pro GitHub (`.gitignore`), os dois arquivos de
  licença (`LICENSE` e `LICENSE-CONTENT.txt`) e, de `modelo-dados/`, o mapa do projeto
  (`projeto.json`), o estilo dos cartões (`estilo-cartao.css`) e o `fluxo-ia.json`.
- **Confira depois:** se as pastas que o mapa do projeto indica são as que você quer.
- **Se você guarda o projeto no GitHub:** pode ativar a conferência das mensagens, que é
  opcional (ver o [README dela](.githooks/README.md)).

### 2. Formato da disciplina

- **Entregue:** o curso, a disciplina, o nível de estudo, o material de aula e, se
  tiver, a ementa.
- **Peça:** que proponha cada resposta do [Descubra seu modelo](DESCUBRA-SEU-MODELO.md),
  dizendo por que ela cabe, ou não, nesse curso e nesse nível.
- **Confira depois:** se o arquivo de formato (`formato.json`) tem só as respostas que
  você aceitou.
- **Sempre seu:** cada resposta. A IA propõe; você decide.

### 3. Transcrição da aula

- **Entregue:** o material de aula.
- **Peça:** a transcrição de cada página, só com o que está escrito, no padrão da
  [seção 2 da metodologia](metodologia-de-conteudo.md#2-trate-as-fontes-da-aula), o
  registro de cada transcrição e a conferência delas.
- **Confira depois:** cada página, na conferência das transcrições, contra a imagem.
- **Sempre seu:** o tique de cada página.

### 4. Referências das fontes

- **Peça:** que preencha os dados de cada fonte no arquivo de fontes (`fontes.json`), como
  estão na folha de rosto ou na página do documento, e gere as referências.
- **Confira depois:** cada referência e a chamada dela, na conferência das referências,
  contra a fonte. As [regras da ABNT](regras-abnt.md) dizem o que cada informação leva.
- **Sempre seu:** a escolha do *et al.* e o tique de cada referência.

### 5. Material de fora

- **Peça:** que marque, item por item, o que a aula cobre de cada subtópico do formato,
  e proponha um material oficial ou de referência pra cada subtópico que a aula não
  cobre; depois, que monte a base dele e classifique cada frase (ver a
  [seção 4 da metodologia](metodologia-de-conteudo.md#4-complete-a-aula-com-material-de-fora)).
- **Confira depois:** a cobertura e a classe de cada frase, na conferência dos trechos.
- **Sempre seu:** aceitar ou não cada material de fora, e o tique de cada página.

### 6. Documentos de conteúdo

- **Peça:** que leia inteiras as transcrições conferidas e as bases e só então escreva a
  teoria fundamental, o dicionário e a ficha, com a chamada de cada fato (seções 5 a 8
  da metodologia).
- **Confira depois:** cada documento contra as fontes, com a auditoria da
  [seção 16 da metodologia](metodologia-de-conteudo.md#16-checklist-auditando-uma-disciplina-existente).
- **Sempre seu:** o recorte — o que entra, o quão fundo e o que é mais importante.

### 7. Cartões

- **Peça:** as planilhas de pergunta a partir do dicionário e da ficha, a prova de cada
  cartão e a conferência dos cartões (ver a
  [seção 9 da metodologia](metodologia-de-conteudo.md#9-cartões-de-revisão-espaçada)).
- **Confira depois:** cada cartão, na conferência dos cartões, contra o trecho que o
  prova; e se a resposta traz a ressalva quando a fonte trata o fato como possibilidade.
- **Sempre seu:** o tique de cada cartão.

### 8. Baralho

- **Peça:** que gere os baralhos com o script `montar_deck.py`.
- **Confira depois:** no Anki, se os cartões aparecem como na planilha.

### 9. Documentos de apresentação

- **Peça:** que copie pra pasta principal do projeto e preencha os quatro documentos de
  [`modelo-documentos-raiz/`](modelo-documentos-raiz/LEIA-ME.md).
- **Sempre seu:** o aviso do recorte, a origem do material e o contato pra relatar erros.

### 10. Conferência final

- **Peça:** que rode todos os scripts, resolva cada linha `ERRO` ou `FALTA` e aponte toda
  parte das conferências que ainda não tem o seu tique.
- **Sempre seu:** o tique final em cada parte e a análise humana da lista de revisão
  da [seção 16 da metodologia](metodologia-de-conteudo.md#16-checklist-auditando-uma-disciplina-existente).

## O que é sempre seu

A IA propõe, escreve e confere primeiro; você decide e confere por último. São sempre
seus: o formato da disciplina, o recorte, a escolha de cada material de fora, o tique
final de cada conferência e a decisão de publicar. E, se a IA disser algo que não está
na fonte, a fonte vale, não a IA.

---

*Este documento está licenciado sob [CC BY-NC-SA 4.0](LICENSE-CONTENT.txt).*
