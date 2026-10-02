# Descubra o formato da sua disciplina

Este documento ajuda a decidir a estrutura de conteúdo de uma disciplina nova. O método
monta, pra cada assunto que se estuda um por um (os *itens*), dois documentos: o
*dicionário*, que conta o item como uma história dividida em partes, os *elos*; e a
*ficha*, uma tabela seca com uma linha pra cada tipo de fato que todo item tem, os
*eixos*. Os cartões de pergunta saem de uma *planilha*, uma tabela com uma coluna pra
cada informação do cartão. Aqui você decide quantos elos o dicionário tem, quantos eixos
a ficha tem e que colunas a planilha precisa. Nenhum desses números é fornecido aqui —
cada disciplina responde essas perguntas pra si mesma, a partir do próprio material.

## O que é estável entre disciplinas

- Existe conteúdo que é teoria geral, sem ligação com um item específico — isso é
  sempre um documento próprio (ver `metodologia-de-conteudo.md`, seção 5A).
- Quando existe um item que se repete e que alguém precisa aprender individualmente,
  contar esse item de dois jeitos — uma história em cadeia, e uma tabela seca com os
  mesmos fatos — permite estudar de duas formas sem duplicar o trabalho de escrever.

O resto (quantos elos, quantos eixos, que nomes, se existem itens repetidos ou não) é
decisão de cada disciplina.

## Antes das perguntas: para quem é o material

Diga o curso, a disciplina e o nível de estudo de que você precisa (uma revisão pra
prova, uma base pra disciplinas seguintes, um aprofundamento). Tudo o que vem depois
depende disso: o mesmo assunto pede itens, eixos e profundidade diferentes em cursos e
níveis diferentes.

Você pode responder às perguntas abaixo com ajuda de uma IA. Passe a ela o curso, a
disciplina, o nível e o material de aula — e, se tiver, a ementa ou o plano de ensino
da disciplina, que é a referência mais firme do que ela cobre — e peça que proponha
cada resposta dizendo por que ela cabe, ou não cabe, nesse curso e nesse nível. A
decisão é sua; no arquivo de formato vai só a resposta, não a justificativa.

## Perguntas para decidir o formato

1. **Existem itens que se repetem no seu material** — coisas que alguém aprende uma por
   uma? Se não existem, sua disciplina provavelmente só precisa do documento de teoria
   fundamental, sem dicionário nem ficha por item.
2. **Se existem itens: quais fatos diferentes alguém precisa saber pra conhecer um item
   por completo?** Liste com suas próprias palavras, a partir do seu material — não a
   partir do que outra disciplina já usou. Esses são os eixos da ficha. Se um eixo se
   divide em partes menores que todo item também tem, liste essas partes: são os
   subtópicos dele.
3. **Existe uma cadeia de causa e efeito natural conectando esses fatos**? Se sim,
   quantos passos ela tem, de verdade, no seu material?
4. **Que colunas uma pergunta de revisão sobre um item precisa?** Escreva os nomes você
   mesmo, a partir do que o item efetivamente é.
5. **Seu material precisa de imagem, áudio ou outro anexo por item?** Se precisar, isso
   ainda não tem um formato pronto neste modelo — precisa ser desenhado.

## Depois de responder

Grave as respostas no arquivo de formato da disciplina, `docs/formato.json`. É um
arquivo de texto com as respostas organizadas de um jeito que os scripts (os pequenos
programas do modelo) conseguem ler. Copie
[`modelo-dados/formato.json`](modelo-dados/formato.json) pra lá e troque cada trecho entre
colchetes pela resposta, sem mexer no resto. O arquivo guarda só as respostas — nomes e
listas, sem explicação — e cada informação dele, com o nome que aparece entre aspas no
arquivo, responde a uma pergunta:

| Informação | Pergunta |
|---|---|
| `itens` | 1 (lista vazia, se não houver itens) |
| `eixos` e os `subtopicos` de cada eixo | 2 (lista vazia de subtópicos, se o eixo não se dividir) |
| `elos` | 3 (lista vazia, se não houver cadeia) |
| `colunas_extras` | 4 (só as que vão além de `pergunta`, `resposta` e `fonte`) |
| `curso`, `disciplina` e `nivel` | *Antes das perguntas* |
| `idioma` | o idioma do material gerado |

Depois, confira se o arquivo ficou bem preenchido com o script `validar_dados.py`: o
[README dos scripts](scripts/README.md) diz, passo a passo, como rodar. É desse arquivo
que sai a grade do que cada item precisa ter, antes de qualquer material ser escrito. Se
a sua disciplina precisar de uma informação que o formato ainda não tem, acrescente: o
arquivo aceita informações novas, e os scripts ignoram o que não conhecem. Registre a
mudança na metodologia (seção 17), pra que o formato cresça no modelo também.

O script que monta os cartões do Anki (`montar_deck.py`) só exige duas colunas com nome
certo na planilha: uma chamada `pergunta` e outra `resposta`. A metodologia pede mais
uma em toda planilha, a `fonte`, com a citação de onde veio cada fato, que aparece atrás
do cartão, embaixo da resposta (seções 3 e 9 da metodologia). Qualquer outra coluna que
você criar vira parte do cartão automaticamente, com o nome que você escolheu; no Anki,
o nome aparece sem o sublinhado e com cada palavra em maiúscula (`tipo_pergunta` vira
`TipoPergunta`).

---

*Este documento está licenciado sob [CC BY-NC-SA 4.0](LICENSE-CONTENT.txt).*
