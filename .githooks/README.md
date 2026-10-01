# Hook + template de commit

Este diretório contém dois arquivos que trabalham juntos:

- **`commit-template.txt`** — um esqueleto (título + descrição com marcadores
  `SUBSTITUA-...`) que o git carrega automaticamente no editor assim que você roda
  `git commit` (sem `-m`), antes de você escrever qualquer coisa.
- **`commit-msg`** — um hook que verifica, de forma mecânica, só a **estrutura** da
  mensagem final — nunca se ela é precisa, verdadeira ou bem escrita. Isso continua
  sendo julgamento de quem commita; o hook só barra a mensagem que:
  - não tem título (primeira linha vazia);
  - o título é, ele próprio, um bullet/item de lista (`- corrigido X`, `1. corrigido X`...);
  - não tem uma linha em branco separando título de descrição;
  - a descrição usa bullets/lista (`-`, `*`, `•`, `1.`, `2)`...) em vez de prosa corrida;
  - ainda contém algum marcador `SUBSTITUA-...` do template, ou seja, o título/descrição
    não foi de fato escrito por cima do esqueleto.

## Como ativar num projeto novo

Copie esta pasta (`.githooks/`) para a raiz do projeto da disciplina e rode, uma vez,
dentro dele:

    git config core.hooksPath .githooks
    git config commit.template .githooks/commit-template.txt

A partir daí, todo `git commit` (sem `-m`) já abre o editor com o esqueleto do template
pronto pra preencher, e todo commit — com ou sem `-m` — passa pela checagem estrutural
antes de ser aceito. Isso vale só localmente, por clone — git não versiona nenhuma dessas
duas configurações, então quem clonar o repositório precisa rodar os dois comandos de
novo na própria máquina.

## Por que existe

Um commit escrito como lista item-por-item (um bullet por arquivo alterado) parece
organizado num commit pequeno, mas não escala: à medida que o projeto cresce, cada
commit tem que decidir de novo "quanto detalhe cabe aqui", e isso não converge para um
padrão. O formato título + descrição em prosa corrida evita esse inventário.

O template resolve a parte de guiar quem escreve (mostra a forma esperada antes de
qualquer texto existir); o hook resolve a parte de barrar o que foge da forma depois de
escrito. Nenhum dos dois garante que o conteúdo é preciso ou coerente — uma frase cortada
ao meio entre "título" e "descrição" ainda passa, porque isso é sentido, não forma, e
sentido não é mecanizável por regex. O que o hook mecaniza é só o que é checável sem
julgamento: existe título, existe separador, não tem lista, o marcador do template foi
substituído.
