# Material de base (nunca versionado)

Esta pasta recebe o material de aula original da disciplina (PDFs de slides ou
equivalente) e, na subpasta `fontes-externas/`, as cópias do material de fora usado onde
a aula não cobre um eixo (ver seção 5 da metodologia). Regra permanente, não uma
pendência a resolver depois (ver seção 10 da
[metodologia de conteúdo](../../metodologia-de-conteudo.md)):

- **Nunca é versionada, publicada ou redistribuída** — o `.gitignore` da raiz já exclui
  `*.pdf` e as subpastas `gerados-ocr/` e `fontes-externas/` daqui.
- A referência de cada material — as aulas e o de fora — vai em `docs/FONTES.md`, que é
  versionado: o que fica de fora é a cópia, não a referência.
- A transcrição literal do material de aula (OCR ou equivalente) e a base de trechos
  literais do material de fora vão em `gerados-ocr/` — são a base contra a qual se
  confere tudo o que se escreve, e também nunca são versionadas (ver seção 5 da
  metodologia).
- Antes de escrever qualquer coisa em `docs/material-gerado/`, leia este material
  inteiro, sem ferramenta que corte ou resuma automaticamente o texto (ver seção 5 da
  metodologia).

Este arquivo (`README.md`) é o único conteúdo desta pasta que deve ser versionado — ele
existe só para documentar a convenção, mesmo quando a pasta está vazia.
