# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright do codigo sob GPL-3.0 -- ver LICENSE e NOTICE.md na raiz do projeto.

"""
Gera o arquivo de conferencia das transcricoes das fontes com imagem. O arquivo nasce do
que foi gerado da fonte, nao da fonte: cada transcricao e mostrada pagina por pagina, ao
lado da imagem da mesma pagina no PDF de onde ela veio, com o link para o original e
duas caixas de tique, "IA" e "pessoa".

O script nao julga o conteudo: so mostra. Quem confere e quem tica -- a IA pode ticar
primeiro, e nenhuma pagina vale como conferida sem o tique da pessoa. Pagina do PDF que
a transcricao nao tem aparece com a imagem e sem texto; secao que aponta para pagina que
o PDF nao tem aparece com o texto e sem imagem.

A transcricao e ligada ao PDF pelo registro no topo dela (ver registrar_fonte.py), nunca
pelo nome dos arquivos: uma transcricao registra uma fonte so. O arquivo gerado diz, para
cada transcricao, se o PDF registrado ainda e o mesmo, se mudou depois do registro ou se
nao existe.

Convencao da transcricao (secao 5 da metodologia): o registro da fonte no topo e uma
secao por pagina, com o titulo "## <como a citacao chama a pagina> (arquivo p. <posicao
no PDF>)" -- por exemplo, "## p. 12 (arquivo p. 14)" ou "## slide 3 (arquivo p. 3)".
Pagina sem texto nenhum fica com a secao e a marca "[sem texto]".

Os tiques ficam no proprio arquivo gerado, com a assinatura do que foi conferido (PDF,
pagina e transcricao). Ao gerar de novo, o tique volta se a assinatura e a mesma; se o
texto da pagina ou o PDF mudou, o tique e retirado, e a pagina diz isso.

As pastas e o arquivo gerado vem do projeto.json ("gerados", "conferencia_imagens" e
"material_base"). Precisa dos comandos pdfinfo e pdftoppm (pacote Poppler).

Uso (de qualquer pasta dentro do projeto):
    python scripts/conferencia.py
    python scripts/conferencia.py --projeto projeto.json
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comum import (acha_projeto, ancora, assinatura, caixas, fontes_registradas, imagem, impressao,  # noqa: E402
                   link, marca, numero_de_paginas, situacao_da_copia, tiques_anteriores, tiques_da_parte)

TITULO_PAGINA = re.compile(r"^## (.+?) \(arquivo p\. (\d+)\)\s*$")
CERCA = "````"  # cerca de 4 crases: a transcricao pode ter blocos de 3

SITUACAO = {
    "confere": "é o mesmo do registro",
    "mudou": "mudou depois do registro",
    "nao-existe": "não existe",
    "sem-registro": "a transcrição não registra de qual PDF veio",
    "varias": "a transcrição registra mais de uma fonte",
}


def secoes(texto):
    """[(rotulo, pagina, texto)] na ordem do arquivo."""
    out, atual = [], None
    for linha in texto.split("\n"):
        m = TITULO_PAGINA.match(linha)
        if m:
            atual = [m.group(1).strip(), int(m.group(2)), []]
            out.append(atual)
        elif linha.startswith("## "):
            atual = None
        elif atual is not None:
            atual[2].append(linha)
    return [(r, n, "\n".join(t).strip()) for r, n, t in out]


def transcricoes_da_pasta(pasta, saida):
    """Todo .md da pasta que tem pelo menos um titulo de pagina, menos o arquivo gerado."""
    out = []
    for arq in sorted(pasta.glob("*.md")):
        if arq.resolve() == saida.resolve():
            continue
        texto = arq.read_text(encoding="utf-8")
        if secoes(texto):
            out.append((arq, texto))
    return out


def fonte_da_transcricao(texto, raiz):
    """(chave ou None, caminho do PDF ou None, situacao do registro)."""
    registradas = fontes_registradas(texto)
    if not registradas:
        return None, None, "sem-registro"
    if len(registradas) > 1:
        return None, None, "varias"
    chave, (caminho, hash_registrado) = next(iter(registradas.items()))
    pdf, situacao = situacao_da_copia(raiz, caminho, hash_registrado)
    return chave, pdf, situacao


def partes(nome, texto, pdf, situacao, anteriores, pasta_img):
    com_pdf = situacao in ("confere", "mudou")
    hash_pdf = impressao(pdf) if com_pdf else ""
    total = numero_de_paginas(pdf) if com_pdf else 0
    por_pagina = {}
    for rotulo, n, conteudo in secoes(texto):
        por_pagina.setdefault(n, []).append((rotulo, conteudo))
    out = []
    for n in sorted(set(range(1, total + 1)) | set(por_pagina)):
        secs = por_pagina.get(n, [])
        rotulo = " / ".join(r for r, _ in secs) or f"arquivo p. {n}"
        sig = assinatura(hash_pdf, n, rotulo, "\n\n".join(c for _, c in secs))
        tiques, retirado = tiques_da_parte(anteriores, nome, n, sig)
        out.append({"n": n, "rotulo": rotulo, "secoes": secs, "sig": sig, "tiques": tiques, "retirado": retirado,
                    "imagem": imagem(pdf, n, pasta_img, nome) if com_pdf and n <= total else None})
    return out


def bloco(nome, pdf, parte, saida):
    n = parte["n"]
    out = ["", f"### {nome} — {parte['rotulo']} (arquivo p. {n})", "", marca(nome, n, parte["sig"]), ""]
    if parte["imagem"]:
        out += [f"[original, arquivo p. {n}]({link(pdf, saida)}#page={n})", "",
                f"![{nome}, arquivo p. {n}]({link(parte['imagem'], saida)})", ""]
    else:
        out += ["Imagem: nenhuma (o PDF não tem esta página ou não está disponível)", ""]
    if parte["secoes"]:
        for _, conteudo in parte["secoes"]:
            out += [CERCA, conteudo, CERCA, ""]
    else:
        out += ["Transcrição: nenhuma seção para esta página", ""]
    if parte["retirado"]:
        out += ["Tique retirado: o texto desta página ou o PDF mudou depois do tique", ""]
    return out + caixas(parte["tiques"])


def gera(transcricoes, saida, raiz):
    anteriores = tiques_anteriores(saida)
    pasta_img = saida.with_name(saida.stem + "-imagens")
    resumo, corpo, totais, problemas_de_registro, registrados = [], [], [0, 0, 0, 0], [], set()
    for arq, texto in transcricoes_da_pasta(transcricoes, saida):
        nome = arq.stem
        chave, pdf, situacao = fonte_da_transcricao(texto, raiz)
        if pdf is not None:
            registrados.add(pdf)
        if situacao != "confere":
            problemas_de_registro.append((arq, situacao))
        ps = partes(nome, texto, pdf, situacao, anteriores, pasta_img)
        cont = [len(ps), sum(p["tiques"]["IA"] for p in ps), sum(p["tiques"]["pessoa"] for p in ps)]
        cont.append(cont[0] - cont[2])
        totais = [a + b for a, b in zip(totais, cont)]
        resumo.append(f"| [{nome}](#{ancora(nome)}) | {chave or '—'} | {SITUACAO[situacao]} | "
                      + " | ".join(map(str, cont)) + " |")
        corpo += ["", "---", "", f"## {nome}", "", f"Transcrição: `{link(arq, saida)}`",
                  f"Fonte registrada: {chave or '—'}, `{link(pdf, saida) if pdf else '—'}` ({SITUACAO[situacao]})"]
        for parte in ps:
            corpo += bloco(nome, pdf, parte, saida)
    cabecalho = ["# Conferência das transcrições das fontes com imagem", "",
                 "| Transcrição | Chave da fonte | PDF registrado | Páginas | Tique da IA | Tique da pessoa | Sem tique da pessoa |",
                 "| :--- | :--- | :--- | ---: | ---: | ---: | ---: |"] + resumo
    cabecalho.append("| **Total** | | | " + " | ".join(f"**{x}**" for x in totais) + " |")
    saida.parent.mkdir(parents=True, exist_ok=True)
    saida.write_text("\n".join(cabecalho + corpo) + "\n", encoding="utf-8")
    return totais, problemas_de_registro, registrados


def main(argv=None):
    p = argparse.ArgumentParser(description="Gera o arquivo de conferência das transcrições das fontes com imagem.")
    p.add_argument("--projeto", type=Path, help="projeto.json (padrao: o primeiro achado subindo a partir daqui)")
    a = p.parse_args(argv)
    projeto = acha_projeto(a.projeto)
    transcricoes, saida = projeto.caminho("gerados"), projeto.caminho("conferencia_imagens")
    if not transcricoes_da_pasta(transcricoes, saida):
        raise SystemExit(f"nenhuma transcricao em {transcricoes}")
    (paginas, ia, pessoa, sem_pessoa), problemas_de_registro, registrados = gera(transcricoes, saida, projeto.raiz)
    for arq, situacao in problemas_de_registro:
        print(f"REGISTRO: {arq.name} -- PDF registrado: {SITUACAO[situacao]}")
    for pdf in sorted(projeto.caminho("material_base").glob("*.pdf")):
        if pdf.resolve() not in registrados:
            print(f"aviso: {pdf.name} nao e a fonte registrada de nenhuma transcricao")
    print(f"{paginas} páginas | tique da IA: {ia} | tique da pessoa: {pessoa} | sem tique da pessoa: {sem_pessoa}")
    print(f"arquivo: {saida}")
    return 1 if problemas_de_registro else 0


if __name__ == "__main__":
    sys.exit(main())
