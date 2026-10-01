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
pelo nome dos arquivos. O arquivo gerado diz, para cada transcricao, se o PDF registrado
ainda e o mesmo, se mudou depois do registro ou se nao existe.

Convencao da transcricao (secao 5 da metodologia): o registro da fonte no topo e uma
secao por pagina, com o titulo "## <como a citacao chama a pagina> (arquivo p. <posicao
no PDF>)" -- por exemplo, "## p. 12 (arquivo p. 14)" ou "## slide 3 (arquivo p. 3)".
Pagina sem texto nenhum fica com a secao e a marca "[sem texto]".

Os tiques ficam no proprio arquivo gerado, com a assinatura do que foi conferido (PDF,
pagina e transcricao). Ao gerar de novo, o tique volta se a assinatura e a mesma; se o
texto da pagina ou o PDF mudou, o tique e retirado, e a pagina diz isso.

Precisa dos comandos pdfinfo e pdftoppm (pacote Poppler).

Uso:
    python scripts/conferencia.py
    python scripts/conferencia.py --transcricoes DIR --saida ARQUIVO.md --base DIR --raiz DIR
"""

import argparse
import hashlib
import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from registrar_fonte import RAIZ, fontes_registradas, impressao  # noqa: E402

BASE_PADRAO = RAIZ / "docs" / "material-base"
TRANSCRICOES_PADRAO = BASE_PADRAO / "gerados-ocr"
SAIDA_PADRAO = TRANSCRICOES_PADRAO / "CONFERENCIA-COM-IMAGEM.md"
RESOLUCAO = "80"  # dpi da imagem da pagina

TITULO_PAGINA = re.compile(r"^## (.+?) \(arquivo p\. (\d+)\)\s*$")
MARCA_PARTE = re.compile(r"^<!-- parte: (.+)\|(\d+)\|([0-9a-f]+) -->$")
TIQUE = re.compile(r"^- \[([ xX])\] (IA|pessoa)\s*$")
CERCA = "````"  # cerca de 4 crases: a transcricao pode ter blocos de 3

SITUACAO = {
    "confere": "é o mesmo do registro",
    "mudou": "mudou depois do registro",
    "nao-existe": "não existe",
    "sem-registro": "a transcrição não registra de qual PDF veio",
}


def comando(args):
    return subprocess.run(args, capture_output=True, text=True, check=True).stdout


def numero_de_paginas(pdf):
    m = re.search(r"^Pages:\s+(\d+)", comando(["pdfinfo", str(pdf)]), re.M)
    return int(m.group(1)) if m else 0


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
    """(caminho do PDF ou None, situacao do registro)."""
    registradas = fontes_registradas(texto)
    if "" not in registradas:
        return None, "sem-registro"
    caminho, hash_registrado = registradas[""]
    pdf = (raiz / caminho).resolve()
    if not pdf.exists():
        return pdf, "nao-existe"
    return pdf, "confere" if impressao(pdf) == hash_registrado else "mudou"


def assinatura(hash_pdf, n, rotulo, texto):
    junto = re.sub(r"\s+", " ", f"{hash_pdf}|{n}|{rotulo}|{texto}").strip()
    return hashlib.sha256(junto.encode("utf-8")).hexdigest()[:12]


def tiques_anteriores(saida):
    """{(transcricao, pagina): (assinatura, {"IA": bool, "pessoa": bool})} do arquivo ja gerado."""
    if not saida.exists():
        return {}
    out, chave = {}, None
    for linha in saida.read_text(encoding="utf-8").split("\n"):
        m = MARCA_PARTE.match(linha)
        if m:
            chave = (m.group(1), int(m.group(2)))
            out[chave] = (m.group(3), {"IA": False, "pessoa": False})
            continue
        m = TIQUE.match(linha)
        if m and chave in out:
            out[chave][1][m.group(2)] = m.group(1) != " "
    return out


def imagem(pdf, n, pasta, nome):
    """PNG da pagina, gerado de novo so se nao existe ou se o PDF e mais novo que ele."""
    pasta.mkdir(parents=True, exist_ok=True)
    base = pasta / f"{nome}-p{n:03d}"
    png = base.with_suffix(".png")
    if not png.exists() or png.stat().st_mtime < pdf.stat().st_mtime:
        comando(["pdftoppm", "-f", str(n), "-l", str(n), "-r", RESOLUCAO, "-png", "-singlefile", str(pdf), str(base)])
    return png


def link(alvo, saida):
    return Path(os.path.relpath(alvo, saida.parent)).as_posix()


def ancora(texto):
    return re.sub(r"[^\w-]", "", texto.lower().replace(" ", "-"))


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
        conteudo = "\n\n".join(c for _, c in secs)
        sig = assinatura(hash_pdf, n, rotulo, conteudo)
        tiques, retirado = {"IA": False, "pessoa": False}, False
        anterior = anteriores.get((nome, n))
        if anterior:
            if anterior[0] == sig:
                tiques = anterior[1]
            else:
                retirado = any(anterior[1].values())
        out.append({"n": n, "rotulo": rotulo, "secoes": secs, "sig": sig, "tiques": tiques, "retirado": retirado,
                    "imagem": imagem(pdf, n, pasta_img, nome) if com_pdf and n <= total else None})
    return out


def bloco(nome, pdf, parte, saida):
    n = parte["n"]
    out = ["", f"### {nome} — {parte['rotulo']} (arquivo p. {n})", "", f"<!-- parte: {nome}|{n}|{parte['sig']} -->", ""]
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
    out += [f"- [{'x' if parte['tiques']['IA'] else ' '}] IA",
            f"- [{'x' if parte['tiques']['pessoa'] else ' '}] pessoa"]
    return out


def gera(transcricoes, saida, raiz):
    anteriores = tiques_anteriores(saida)
    pasta_img = saida.with_name(saida.stem + "-imagens")
    resumo, corpo, totais, problemas_de_registro, registrados = [], [], [0, 0, 0, 0], [], set()
    for arq, texto in transcricoes_da_pasta(transcricoes, saida):
        nome = arq.stem
        pdf, situacao = fonte_da_transcricao(texto, raiz)
        if pdf is not None:
            registrados.add(pdf)
        if situacao != "confere":
            problemas_de_registro.append((arq, situacao))
        ps = partes(nome, texto, pdf, situacao, anteriores, pasta_img)
        cont = [len(ps), sum(p["tiques"]["IA"] for p in ps), sum(p["tiques"]["pessoa"] for p in ps)]
        cont.append(cont[0] - cont[2])
        totais = [a + b for a, b in zip(totais, cont)]
        resumo.append(f"| [{nome}](#{ancora(nome)}) | {SITUACAO[situacao]} | " + " | ".join(map(str, cont)) + " |")
        corpo += ["", "---", "", f"## {nome}", "", f"Transcrição: `{link(arq, saida)}`",
                  f"PDF registrado: `{link(pdf, saida) if pdf else '—'}` ({SITUACAO[situacao]})"]
        for parte in ps:
            corpo += bloco(nome, pdf, parte, saida)
    cabecalho = ["# Conferência das transcrições das fontes com imagem", "",
                 "| Transcrição | PDF registrado | Páginas | Tique da IA | Tique da pessoa | Sem tique da pessoa |",
                 "| :--- | :--- | ---: | ---: | ---: | ---: |"] + resumo
    cabecalho.append("| **Total** | | " + " | ".join(f"**{x}**" for x in totais) + " |")
    saida.parent.mkdir(parents=True, exist_ok=True)
    saida.write_text("\n".join(cabecalho + corpo) + "\n", encoding="utf-8")
    return totais, problemas_de_registro, registrados


def main(argv=None):
    p = argparse.ArgumentParser(description="Gera o arquivo de conferência das transcrições das fontes com imagem.")
    p.add_argument("--transcricoes", type=Path, default=TRANSCRICOES_PADRAO,
                   help=f"pasta das transcricoes (padrao: {TRANSCRICOES_PADRAO})")
    p.add_argument("--saida", type=Path, default=SAIDA_PADRAO, help=f"arquivo gerado (padrao: {SAIDA_PADRAO})")
    p.add_argument("--base", type=Path, default=BASE_PADRAO,
                   help=f"pasta dos PDFs, so para listar os que nenhuma transcricao registra (padrao: {BASE_PADRAO})")
    p.add_argument("--raiz", type=Path, default=RAIZ, help=f"raiz do projeto (padrao: {RAIZ})")
    a = p.parse_args(argv)
    if not transcricoes_da_pasta(a.transcricoes, a.saida):
        raise SystemExit(f"nenhuma transcricao em {a.transcricoes}")
    (paginas, ia, pessoa, sem_pessoa), problemas_de_registro, registrados = gera(a.transcricoes, a.saida, a.raiz.resolve())
    for arq, situacao in problemas_de_registro:
        print(f"REGISTRO: {arq.name} -- PDF registrado: {SITUACAO[situacao]}")
    for pdf in sorted(a.base.glob("*.pdf")):
        if pdf.resolve() not in registrados:
            print(f"aviso: {pdf.name} nao e a fonte registrada de nenhuma transcricao")
    print(f"{paginas} páginas | tique da IA: {ia} | tique da pessoa: {pessoa} | sem tique da pessoa: {sem_pessoa}")
    print(f"arquivo: {a.saida}")
    return 1 if problemas_de_registro else 0


if __name__ == "__main__":
    sys.exit(main())
