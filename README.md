# Modelo de núcleo de conteúdo por recorte

Ponto de partida pra montar um núcleo de material de estudo (documentos de teoria,
dicionário de gatilhos, ficha determinística, planilhas de pergunta, baralho de Anki)
pra qualquer disciplina de graduação, a partir do material de aula dela. Pra usar,
comece pelos dois primeiros itens da lista abaixo, nessa ordem.

## Uso de IA

O método deste modelo usa IA na produção do material: propor o formato da disciplina
(no [Descubra seu modelo](DESCUBRA-SEU-MODELO.md)), transcrever o material de aula,
redigir os documentos, gerar as planilhas de pergunta e, quando for preciso, escrever um
script novo (seções 2 a 10 da [metodologia](metodologia-de-conteudo.md)). O que a IA produz não vira material final
direto: passa primeiro por uma análise mecânica, a que um script consegue fazer, e depois
pela análise humana, contra o material de origem (o que é uma e o que é outra em cada
etapa está na [seção 11 da metodologia](metodologia-de-conteudo.md#11-confira-primeiro-o-script-depois-a-pessoa)).
A escolha do recorte, a decisão sobre cada fato e a palavra final são de uma pessoa.

Qualquer assistente de IA serve. Como usá-lo — gratuito ou pago, sozinho ou com
agentes trabalhando em equipe — é decisão de quem segue o modelo. Este repositório não
ensina a usar IA — só deixa claro onde ela entra: o
[Trabalhar com uma IA](trabalhar-com-ia.md) diz, etapa por etapa, o que pedir, o que
entregar e o que conferir depois, e o [método em dados](modelo-dados/fluxo-ia.json) é o
arquivo que a IA lê pra seguir as etapas.

## O que tem aqui

- **[Descubra seu modelo](DESCUBRA-SEU-MODELO.md)** — o primeiro passo: você diz o curso,
  a disciplina e o nível de estudo e responde, sozinho ou com ajuda de uma IA, às
  perguntas que decidem o formato do material, como os itens que a disciplina tem, os
  fatos que cada item precisa ter e as colunas que os cartões levam.
- **[Metodologia de conteúdo](metodologia-de-conteudo.md)** — o método inteiro, do
  material de aula ao cartão: o que vai em cada documento, como tratar o material de
  aula e como conferir, com os checklists de disciplina nova e de auditoria.
- **[Regras da ABNT](regras-abnt.md)** — o que as normas de citação e de referência
  pedem, item por item, em palavras simples, e quem cuida de cada regra: o script, os
  dados das fontes ou quem escreve o texto.
- **[Trabalhar com uma IA](trabalhar-com-ia.md)** — o que pedir à IA em cada etapa, o
  que entregar a ela, o que conferir depois e o que é sempre seu, pra qualquer
  assistente de IA.
- **[Modelo dos documentos de raiz](modelo-documentos-raiz/LEIA-ME.md)** — os quatro
  documentos que ficam na raiz do projeto da sua disciplina (a apresentação técnica, o
  índice, o manual de uso e o aviso de licenças), prontos pra copiar e preencher.
- **[Modelo de dados](modelo-dados/)** — os arquivos de dados do projeto da sua
  disciplina, pra copiar e preencher: o [mapa do projeto](modelo-dados/projeto.json), que
  diz aos scripts onde fica cada coisa; o [formato](modelo-dados/formato.json), com as
  respostas do Descubra seu modelo; as [fontes](modelo-dados/fontes.json), com os dados de
  cada fonte, de onde saem as referências; a [base](modelo-dados/base.json) de um item,
  com o que foi lido do material de fora e a decisão sobre cada frase; a
  [prova](modelo-dados/prova.json) dos cartões de uma planilha, com o trecho da fonte que
  prova cada um; o
  [estilo dos cartões](modelo-dados/estilo-cartao.css), com a aparência deles no Anki;
  e o [método em dados](modelo-dados/fluxo-ia.json), que não se preenche: é copiado e
  entregue à IA.
- **[Material de base](docs/material-base/README.md)** — a pasta do material de aula, da
  transcrição literal dele e das cópias do material de fora que completa a aula. Nada
  dela vai pro GitHub: esse material não é seu pra publicar.
- **[Scripts](scripts/README.md)** — os programas que fazem a parte mecânica do método,
  sempre do mesmo jeito: em que etapa cada um entra e como rodá-lo.
- **[Hook de commit](.githooks/README.md)** — confere a forma de cada mensagem de commit,
  um título, uma linha em branco e a descrição em prosa, sem lista, pra que o histórico
  do projeto se leia como texto.
- **[Licença do código](LICENSE)** e **[licença do conteúdo](LICENSE-CONTENT.txt)** — a
  GPL-3.0 vale pro código; a CC BY-NC-SA 4.0, pro resto.

---

*Este modelo está licenciado sob [CC BY-NC-SA 4.0](LICENSE-CONTENT.txt) — exceto o
código (os programas `.py` de `scripts/` e o `.githooks/commit-msg`), sob
[GPL-3.0](LICENSE).*
