# Regras da ABNT para citar e referenciar

Todo fato que o material tira de uma fonte é citado ali mesmo, junto do fato, e a fonte
aparece inteira na lista de referências. As duas coisas seguem normas da ABNT, a
Associação Brasileira de Normas Técnicas:

- a **NBR 10520**, edição de 2023, para a **citação**: a indicação curta, no meio do
  texto, de onde veio o fato, como (Silva, 2020, p. 12);
- a **NBR 6023**, edição de 2025, para a **referência**: a descrição completa da fonte, na
  lista do fim, como SILVA, Ana. **Título do livro**. São Paulo: Editora, 2020.

As normas são vendidas pela ABNT e protegidas por direito autoral, por isso este
documento não as copia: diz com outras palavras o que cada uma pede, com o número do item
entre parênteses, pra quem quiser conferir na própria norma (a biblioteca da universidade
costuma dar acesso). Os exemplos daqui são inventados.

Cada regra diz também quem cuida dela:

- **o script**: o `referencias.py` faz sozinho, a partir dos dados;
- **os dados**: você, ou a IA, escreve do jeito certo no `fontes.json`, e o script usa como
  está;
- **o texto**: quem escreve o material segue a regra ao citar.

E quem confere é sempre uma pessoa: a conferência das referências mostra cada referência
e a chamada dela ao lado da cópia da fonte, com o tique da IA e o da pessoa (ver o
[README dos scripts](scripts/README.md)).

## Citação no texto (NBR 10520:2023)

Tudo nesta seção vem da NBR 10520 (Associação Brasileira de Normas Técnicas, 2023).

### O sistema

- O método usa o sistema **autor-data**: a citação diz quem responde pela fonte e o ano.
  Um trabalho usa um sistema só, do começo ao fim (6). *O texto.*
- Notas de rodapé não são usadas pra citar: a citação vai no próprio texto (8). *O texto.*
- A citação tem de levar à referência certa na lista: ela começa pela mesma entrada da
  referência (5.1). A conferência das referências mostra a chamada de cada fonte já
  pronta, montada dos mesmos dados que a referência. *O script.*

### Quem aparece na chamada

- **Pessoa:** o sobrenome, com maiúscula só na primeira letra: (Silva, 2020) (6.1.1.1).
  *O script.*
- **Instituição:** o nome completo ou a sigla, com as maiúsculas que o nome tem; sigla vai
  toda em maiúsculas: (Instituto Nacional de Exemplo, 2020) ou (INE, 2020) (6.1.1.2). A
  chamada usa a forma que estiver na entrada da referência. *O script, a partir dos
  dados.*
- **Órgão de governo:** o nome da jurisdição a que ele pertence, como o país ou o
  estado: (Brasil, 2019) (6.1.1.3). *O script, a partir dos dados.*
- **Sem autoria:** o começo do título. Título de uma palavra só: essa palavra. Senão, a
  primeira palavra e [...]; se o título começa por artigo (o, a, um, uma...) ou por
  palavra de uma sílaba, essa palavra, a seguinte e [...]: (O manual [...], 2018)
  (6.1.1.4). O script usa as palavras do começo do título que estão em maiúsculas nos
  dados, e é por isso que elas vão em maiúsculas lá (ver [Autoria](#autoria), mais
  abaixo). *O script, a partir dos dados.*
- **Dois ou três autores:** dentro dos parênteses, separados por ponto e vírgula —
  (Silva; Souza, 2020); na frase, com vírgula e "e" — Silva e Souza (2020) (6.1.3,
  6.1.4). *O script.*
- **Quatro autores ou mais:** pode-se citar só o primeiro, seguido de *et al.* em
  itálico — (Silva *et al.*, 2020) —, mesmo que a referência traga todos; o que for
  escolhido vale pra todas as citações (6.1.2). No método, a escolha é uma só, no campo
  `et_al` do `fontes.json`, e vale pra citação e pra referência. *Os dados.*

### Ano e lugar do trecho

- Entre parênteses, o nome e o ano vão juntos: (Silva, 2020). Com o nome dentro da frase,
  só o ano fica entre parênteses: Silva (2020) (6.1.3, 6.1.4). *O texto.*
- Quando o texto copia as palavras da fonte, o lugar do trecho vem depois do ano: a
  página, (Silva, 2020, p. 12), ou, se o documento não tem páginas numeradas, a
  localização que ele tiver, como o slide (6.1.3, 7.1.4). Quando o texto diz o fato com
  outras palavras, a norma deixa o lugar opcional (7.2), mas o método pede o lugar sempre:
  é por ele que se confere o fato na fonte (ver a
  [seção 3 da metodologia](metodologia-de-conteudo.md#3-cite-cada-fonte-conforme-a-abnt)). *O texto.*
- Volume, tomo ou seção, quando houver, vêm antes da página, abreviados: (Silva, 2020,
  v. 2, p. 30) (7.1.3). *O texto.*

### Quando duas chamadas ficariam iguais

- **Mesmo sobrenome, mesmo ano, pessoas diferentes:** entram as iniciais dos prenomes,
  (Silva, A., 2020) e (Silva, B., 2020), ou os prenomes inteiros, se as iniciais também
  forem iguais. Na frase, as iniciais vêm antes do sobrenome: A. Silva (2020) (6.1.5).
  *O script.*
- **Mesma entrada, mesmo ano:** uma letra minúscula logo depois do ano, na ordem em que as
  fontes aparecem na lista de referências, (Brasil, 2019a) e (Brasil, 2019b), e a
  referência leva a mesma letra (6.1.6). *O script.*

### Várias fontes na mesma chamada

- Do mesmo autor, anos diferentes: os anos em ordem, separados por vírgula, (Silva, 2018,
  2020) (6.1.7). *O texto.*
- De autores diferentes: separadas por ponto e vírgula, de preferência em ordem
  alfabética, (Silva, 2020; Souza, 2019) (6.1.8). *O texto.*

### Copiar as palavras da fonte

O método pede o fato com palavras próprias. Quando for preciso copiar:

- Até três linhas: entre aspas duplas; uma citação dentro da citação vai entre aspas
  simples (7.1). *O texto.*
- Mais de três linhas: em parágrafo próprio, com recuo, letra menor, espaço simples e sem
  aspas (7.1.1). No método, evite: copie só um trecho curto. *O texto.*
- Trecho cortado: [...]. Algo que você acrescentou ou comentou: entre colchetes. Destaque
  seu: "grifo nosso" no fim da chamada. Tradução sua: "tradução nossa" no fim da chamada
  (5.2, 7.1.5, 7.1.6). *O texto.*
- O ponto final fecha a frase e vem depois da chamada: "... o trecho copiado" (Silva,
  2020, p. 12). (5.2, 7.1.2). *O texto.*

### Fonte que você não leu

- Se o fato vem de um autor que você só leu citado por outro, a chamada traz os dois,
  ligados por *apud* em itálico, (Lima, 1990 *apud* Silva, 2020, p. 12), e só a fonte que
  você leu entra na lista de referências (7.3, 8.1.3). No método, prefira sempre ler a
  fonte original. *O texto, e nos dados só a fonte lida.*

### O que não vira referência

- O que foi só dito, numa palestra, numa conversa ou numa entrevista, e não está
  publicado é indicado no texto ou em nota, e não entra na lista (5.3, 7.1.7). O método,
  de todo jeito, não usa como fonte o que não está escrito no material (ver a
  [seção 2 da metodologia](metodologia-de-conteudo.md#2-trate-as-fontes-da-aula)); o material
  escrito da aula, como os slides, é documento e tem referência. *O texto.*

## Referência (NBR 6023:2025)

Tudo nesta seção vem da NBR 6023 (Associação Brasileira de Normas Técnicas, 2025), que
substituiu a edição de 2018.

### A lista

- Uma lista só, no fim, em ordem alfabética; números contam pelo valor, 9 antes de 12
  (9.1). *O script.*
- Espaço simples, alinhada à esquerda, com uma linha em branco entre uma referência e
  outra (6.3). *O script.*
- A mesma pontuação e o mesmo destaque em todas: no método, o título vai em **negrito**
  (6.4, 6.7). *O script.*
- Os elementos seguem uma ordem fixa pra cada tipo de documento (6.1, 6.2). *O script.*
- Um elemento complementar (número de páginas, ISBN, série...) usado numa referência
  entra em todas as do mesmo tipo (6.8). *Os dados.*
- O que você acrescenta — "Disponível em:", "Acesso em:", as notas — vai no idioma do seu
  texto, não no da fonte (6.5). *O script* pras duas expressões e pro mês da data de
  acesso, que sai no idioma do formato da disciplina; *os dados* pras notas.

### Autoria

- **Pessoa:** o último sobrenome em maiúsculas, vírgula e os prenomes, SILVA, Ana Maria
  (8.1.1). Até três autores, todos, separados por ponto e vírgula (8.1.1.1). *O script.*
- **Quatro autores ou mais:** o recomendado é pôr todos; pode-se pôr só o primeiro,
  seguido de *et al.* (8.1.1.2). É o campo `et_al` do `fontes.json`: `false` põe todos.
  *Os dados.*
- **Sobrenome composto, hispânico, com Filho, Neto ou Júnior, ou com partícula como D',
  La, O':** tudo entra no sobrenome, SOUZA FILHO, PÉREZ GÓMEZ, D'ÁVILA (8.1.1.3). Nos
  dados, escreva o sobrenome assim, com maiúsculas e minúsculas normais ("Souza Filho");
  uma partícula como "de" fica no fim dos prenomes ("Ana Maria de"). *Os dados.*
- **Organizador, coordenador, editor, compilador:** a abreviatura em minúsculas e no
  singular, entre parênteses, uma vez só, depois do último nome: SILVA, Ana; SOUZA, Rui
  (org.) (8.1.1.4). É o campo `participacao`: `"org."`, `"coord."`, `"ed."`, `"comp."`.
  *Os dados; o script põe no lugar.*
- **Tradutor, revisor, ilustrador:** podem vir depois do título (8.1.1.6). O script não
  monta isso; se precisar, use o tipo `outro`, com a referência escrita à mão.
- **Instituição:** pelo nome conhecido ou como está no documento, em maiúsculas (8.1.2).
  Órgão de governo: primeiro a jurisdição, depois o órgão, BRASIL. Ministério de Exemplo
  (8.1.2.2). Estado e município de mesmo nome: (Estado) ou (Município) depois do nome
  (8.1.2.3). Instituição de mesmo nome em lugares diferentes: o lugar entre parênteses
  (8.1.2.5). Nos dados, cada nível da hierarquia é um item de `entidade`, e o que vai
  entre parênteses é o `qualificador`. *Os dados; o script põe as maiúsculas e a
  pontuação.*
- **Sem autoria:** a referência começa pelo título; nunca "Anônimo" nem "Autor
  desconhecido" (8.1.4). A primeira palavra do título vai em maiúsculas e, se ela for
  artigo ou palavra de uma sílaba, a seguinte também; o título fica sem negrito (6.7,
  8.2.1). Nos dados, escreva o título já assim: `"titulo": "O MANUAL de exemplo"`. *Os
  dados; o script tira o negrito.*

### Título

- Como está no documento, com o subtítulo depois de dois-pontos (8.2). Nos dados,
  `titulo` e `subtitulo` vão separados. *Os dados.*
- Título longo pode ser cortado no fim, com [...] no lugar do que saiu, sem mudar o
  sentido (8.2.2). *Os dados.*
- Documento sem título: um título que descreva o conteúdo, entre colchetes (8.2.7).
  *Os dados.*
- Em negrito quando há autoria (6.7). *O script.*

### Edição

- Só se constar no documento, abreviada no idioma dele: "2. ed.", "3rd ed."; emendas e
  acréscimos também abreviados, como estão no documento: "2. ed. rev." (8.3, 8.3.1).
  *Os dados.*

### Local e editora

- **Local:** a cidade, como está no documento; cidades de mesmo nome levam a sigla do
  estado ou o nome do país, depois de vírgula (8.4, 8.4.1). Vários locais: o primeiro ou o
  mais destacado (8.4.2). Local que não aparece no documento, mas é conhecido: entre
  colchetes (8.4.3). *Os dados.*
- **Editora:** como está no documento, sem as palavras que dizem a natureza jurídica ou
  comercial, como "Ltda." ou "S.A." (8.5). Duas editoras: as duas, cada uma com o seu
  local, separadas por ponto e vírgula, ou separadas por dois-pontos se o local é o mesmo;
  três ou mais, a primeira ou a mais destacada (8.5.2, 8.5.3). Editora que também é a
  autora pode ir abreviada ou pela sigla, se o documento a usa (8.5.4). *Os dados.*
- **Sem local ou sem editora:** local desconhecido vira [*S. l.*] (8.4.4); editora
  desconhecida, [*s. n.*] (8.5.5); os dois, [*S. l.*: *s. n.*] (8.5.6). Basta deixar o
  campo de fora dos dados. *O script.*

### Data

- Sempre há uma data (8.6), com o ano em algarismos (8.6.1). Sem ano de publicação, o de
  copyright, com um "c" colado: c2015 (8.6.1.1). Sem nenhum ano no documento, um ano
  entre colchetes: [2015?] provável, [ca. 2015] aproximado, [201-] década certa, [20--]
  século certo, [2014 ou 2015] um ou outro (8.6.1.3). *Os dados: escreva como a norma
  escreve, e o script mantém.*
- **Dia e mês:** nos dados, `AAAA-MM-DD` ou `AAAA-MM`; o script põe o dia antes do mês e o
  mês abreviado no idioma da publicação, pela tabela da norma (8.6.2, 8.6.3, Anexo A):
  "2020-09-04" sai "4 set. 2020" numa publicação em português e "4 Sept. 2020" numa em
  inglês. Por isso, quando a data tem mês, a fonte precisa do campo `idioma`. A tabela
  traz português, espanhol, italiano, francês, inglês e alemão; em outro idioma, escreva a
  data como está na publicação. Estação ou período, como "primavera 2020" ou "2. sem.
  2020", também vai escrito como está (8.6.2.1, 8.6.2.2). *Os dados e o script.*

### Partes, artigos e documentos online

- **Parte de uma obra** (um capítulo, por exemplo): autor e título da parte, *In*: em
  itálico, a referência da obra inteira e, no fim, as páginas da parte (7.3). *O script.*
- **Artigo de periódico:** autor, título do artigo, nome do periódico em negrito, local,
  volume, número, páginas e data (7.7.5). Nos exemplos da norma, quando o periódico não
  diz o local, ele simplesmente não aparece. *O script.*
- **Documento online:** por último, "Disponível em:" com o endereço e "Acesso em:" com o
  dia em que você o acessou (6.6, 8.13). O DOI, se houver, vem antes, como está no
  documento (7.2.2, 7.7.6). *O script, com `doi`, `url` e `acesso` nos dados.*
- Descrição física (número de páginas, "1 arquivo PDF"), série entre parênteses e notas
  vêm depois da data (8.7, 8.10, 8.11). *O script, com os campos nos dados.*

## Como preencher o `fontes.json`

O arquivo começa com o campo `et_al` e uma lista `fontes`, uma entrada por fonte. Os
campos de cada fonte:

| Campo | O que vai | Item da norma |
| --- | --- | --- |
| `chave` | Um código curto, sem espaço, o mesmo que o registro da transcrição usa | — |
| `tipo` | `monografia` (livro, guia, manual, página, material de aula), `parte` (capítulo), `artigo` (de periódico) ou `outro` | 6023: 7.1, 7.3, 7.7.5 |
| `idioma` | O idioma da publicação: `pt-BR`, `en`, `es`, `fr`, `it` ou `de`; obrigatório quando a data tem mês | 6023: 8.6.2 |
| `autores` | Uma lista. Pessoa: `sobrenome` e `prenomes`. Instituição: `entidade`, com um item por nível, e `qualificador`, se precisar | 6023: 8.1 |
| `participacao` | `org.`, `coord.`, `ed.` ou `comp.`, quando os autores organizaram a obra | 6023: 8.1.1.4 |
| `titulo`, `subtitulo` | Como estão no documento; sem autoria, o começo do título em maiúsculas | 6023: 8.2, 8.2.1 |
| `edicao` | Como está no documento, abreviada: `2. ed.` | 6023: 8.3 |
| `local`, `editora` | Como estão no documento; deixe de fora o que não souber | 6023: 8.4, 8.5 |
| `data` | `AAAA`, `AAAA-MM` ou `AAAA-MM-DD`; data incerta como a norma escreve: `[2015?]`, `c2015` | 6023: 8.6 |
| `paginas` | As páginas da parte ou do artigo: `15-28` | 6023: 7.3, 7.7.5 |
| `parte_de` | No tipo `parte`, a obra inteira, com os campos de uma monografia | 6023: 7.3 |
| `periodico`, `volume`, `numero` | No tipo `artigo` | 6023: 7.7.5 |
| `descricao_fisica`, `serie`, `notas`, `isbn` | Elementos complementares: se usar numa fonte, use em todas do mesmo tipo | 6023: 6.8, 8.7, 8.10, 8.11 |
| `doi`, `url`, `acesso` | Documento online; `acesso` como `AAAA-MM-DD` | 6023: 6.6, 8.13 |
| `referencia` | Só no tipo `outro`: a referência inteira, escrita à mão pela norma | — |

E, no topo do arquivo:

| Campo | O que vai | Item da norma |
| --- | --- | --- |
| `et_al` | `true` pra citar e referenciar só o primeiro de quatro autores ou mais, seguido de *et al.*; `false` pra pôr todos | 6023: 8.1.1.2; 10520: 6.1.2 |

Depois de preencher, rode `python scripts/validar_dados.py docs/fontes.json` pra conferir
a forma do arquivo, e `python scripts/referencias.py` pra gerar as referências e a
conferência (ver o [README dos scripts](scripts/README.md)).

## Referências

ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR 6023**: informação e documentação: referências: elaboração. 3. ed. Rio de Janeiro: ABNT, 2025.

ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR 10520**: informação e documentação: citações em documentos: apresentação. 2. ed. Rio de Janeiro: ABNT, 2023.

---

*Este documento está licenciado sob [CC BY-NC-SA 4.0](LICENSE-CONTENT.txt).*
