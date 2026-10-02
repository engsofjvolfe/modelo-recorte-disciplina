# Material de base (nunca versionado)

Esta pasta recebe o material de aula original da disciplina (PDFs de slides ou
equivalente) e, na subpasta `fontes-externas/`, as cópias do material de fora usado onde
a aula não cobre um eixo (ver seção 4 da metodologia). Regra permanente, não uma
pendência a resolver depois (ver seção 14 da
[metodologia de conteúdo](../../metodologia-de-conteudo.md)):

- **Nunca é versionada, publicada ou redistribuída** — o `.gitignore` da raiz já exclui
  `*.pdf` e as subpastas `gerados-ocr/` e `fontes-externas/` daqui.
- A referência de cada material — as aulas e o de fora — sai dos dados em
  `docs/fontes.json` e vai pro `docs/FONTES.md`, que são versionados: o que fica de fora
  é a cópia, não a referência.
- A transcrição literal do material de aula (OCR ou equivalente) e a base de trechos
  literais do material de fora vão em `gerados-ocr/` — são a base contra a qual se
  confere tudo o que se escreve, e também nunca são versionadas (ver as seções 2 e 4 da
  metodologia). Ali ficam também a base de cada item, `[item]-fontes-externas.md`; a
  prova dos cartões de cada planilha, na subpasta `provas/` (ver seção 9 da
  metodologia); e os quatro arquivos de conferência, com as imagens deles na subpasta
  `imagens/`: o das transcrições contra a imagem de cada página,
  `CONFERENCIA-COM-IMAGEM.md`, gerado por `scripts/conferencia.py`; o das referências
  contra a cópia de cada fonte, `CONFERENCIA-REFERENCIAS.md`, gerado por
  `scripts/referencias.py`; o das frases do material de fora, `CONFERENCIA-TRECHOS.md`,
  gerado por `scripts/base_externa.py`; e o dos cartões contra a prova deles,
  `CONFERENCIA-CARTOES.md`, gerado por `scripts/confere_cartoes.py`.
- Os caminhos daqui são os do modelo. Em cada projeto, quem diz onde fica cada coisa é o
  `projeto.json` da raiz (ver o [README dos scripts](../../scripts/README.md)).
- Antes de escrever qualquer coisa em `docs/material-gerado/`, leia este material
  inteiro, sem ferramenta que corte ou resuma automaticamente o texto (ver seção 2 da
  metodologia).

Este arquivo (`README.md`) é o único conteúdo desta pasta que deve ser versionado — ele
existe só para documentar a convenção, mesmo quando a pasta está vazia.
