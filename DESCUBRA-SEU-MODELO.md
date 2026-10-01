# Descubra o formato da sua disciplina

Este documento ajuda a decidir a estrutura de conteúdo de uma disciplina nova: quantos
elos o dicionário tem, quantos eixos a ficha tem, que colunas a planilha de perguntas
precisa. Nenhum desses números é fornecido aqui — cada disciplina responde essas
perguntas pra si mesma, a partir do próprio material.

Para ver esse formato aplicado numa disciplina real e concreta, veja:

**[recorte-parasitologia no GitHub — link a preencher quando o repositório for publicado]**

## O que é estável entre disciplinas

- Existe conteúdo que é teoria geral, sem ligação com um item específico — isso é
  sempre um documento próprio (ver `metodologia-de-conteudo.md`, seção 1A).
- Quando existe um item que se repete e que alguém precisa aprender individualmente,
  contar esse item de dois jeitos — uma história em cadeia, e uma tabela seca com os
  mesmos fatos — permite estudar de duas formas sem duplicar o trabalho de escrever.

O resto (quantos elos, quantos eixos, que nomes, se existem itens repetidos ou não) é
decisão de cada disciplina.

## Perguntas para decidir o formato

1. **Existem itens que se repetem no seu material** — coisas que alguém aprende uma por
   uma? Se não existem, sua disciplina provavelmente só precisa do documento de teoria
   fundamental, sem dicionário nem ficha por item.
2. **Se existem itens: quais fatos diferentes alguém precisa saber pra conhecer um item
   por completo?** Liste com suas próprias palavras, a partir do seu material — não a
   partir do que outra disciplina já usou.
3. **Existe uma cadeia de causa e efeito natural conectando esses fatos**? Se sim,
   quantos passos ela tem, de verdade, no seu material?
4. **Que colunas uma pergunta de revisão sobre um item precisa?** Escreva os nomes você
   mesmo, a partir do que o item efetivamente é.
5. **Seu material precisa de imagem, áudio ou outro anexo por item?** Se precisar, isso
   ainda não tem um formato pronto neste modelo — precisa ser desenhado.

## Depois de responder

Escreva o formato que as respostas pedem — nomes de coluna, categorias da ficha, passos
do dicionário — direto no material da sua disciplina. Não existe um arquivo de exemplo
pra copiar aqui: o exemplo é a disciplina real linkada no topo deste documento.

O gerador de baralho (`scripts/montar_deck.py`) só exige duas colunas por nome: uma
chamada `pergunta` e outra `resposta`. A metodologia pede mais uma em toda planilha, a
`fonte`, com a citação de cada fato, que o gerador mostra no verso do cartão (seção 5
da metodologia). Qualquer outra coluna que você criar vira parte do cartão
automaticamente, com o nome que você escolheu.

---

*Este documento está licenciado sob [CC BY-NC-SA 4.0](LICENSE-CONTENT.txt).*
