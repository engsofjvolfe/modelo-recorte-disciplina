# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright do codigo sob GPL-3.0 -- ver LICENSE e NOTICE.md na raiz do projeto.

"""
Funcoes que os outros scripts usam: achar o projeto, o registro da fonte no topo de um
documento gerado, a impressao digital de um arquivo, os tiques de um arquivo de
conferencia e a imagem de uma pagina de PDF. Nao e para rodar sozinho.

Nenhum caminho fica no codigo. O projeto e achado pelo arquivo "projeto.json", subindo
de pasta em pasta a partir de onde o script e chamado (ou pelo arquivo indicado com
--projeto), e todo caminho sai dele, relativo a pasta onde ele esta. O nome
"projeto.json" e a unica coisa fixa: e por ele que o script reconhece o projeto.

Registro da fonte, no topo do documento gerado (uma linha por fonte; a chave e a mesma
da referencia da fonte em docs/fontes.json):
    ---
    fonte <CHAVE>: <caminho relativo a raiz do projeto> | sha256: <64 hexadecimais>
    ---

Tique, no arquivo de conferencia: uma marca com o grupo, a parte e a assinatura do que
foi conferido, seguida das caixas "IA" e "pessoa".
"""

import hashlib
import json
import os
import re
import subprocess
from pathlib import Path

ARQUIVO_PROJETO = "projeto.json"
LINHA_FONTE = re.compile(r"^fonte (?P<chave>\S+): (?P<caminho>.+?) \| sha256: (?P<hash>[0-9a-f]{64})$")
MARCA_PARTE = re.compile(r"^<!-- parte: ([^|]+)\|([^|]+)\|([0-9a-f]+) -->$")
TIQUE = re.compile(r"^- \[([ xX])\] (IA|pessoa)\s*$")


class Projeto:
    """Os caminhos do projeto, lidos do projeto.json, relativos a pasta dele."""

    def __init__(self, arquivo):
        self.arquivo = Path(arquivo).resolve()
        self.raiz = self.arquivo.parent
        self.dados = json.loads(self.arquivo.read_text(encoding="utf-8"))

    def caminho(self, nome):
        return self.raiz / self.dados["caminhos"][nome]

    def caminho_do_item(self, nome, item):
        """Caminho que o projeto.json da com "{item}" no lugar do id do item."""
        return self.raiz / self.dados["caminhos"][nome].replace("{item}", item)

    def todos_os_itens(self, nome):
        """Arquivos que existem para o modelo de caminho com "{item}" (qualquer item)."""
        modelo = self.dados["caminhos"][nome]
        return sorted(self.raiz.glob(modelo.replace("{item}", "*")))

    def valor(self, nome):
        return self.dados[nome]

    def pasta_de_imagens(self, conferencia):
        """Pasta das imagens de um arquivo de conferencia: dentro da pasta de imagens do
        projeto, uma subpasta com o nome do proprio arquivo de conferencia."""
        return self.caminho("imagens") / Path(conferencia).stem


def acha_projeto(arquivo=None):
    """O projeto.json indicado, ou o primeiro achado subindo a partir da pasta atual."""
    if arquivo is None:
        atual = Path.cwd().resolve()
        arquivo = next((d / ARQUIVO_PROJETO for d in (atual, *atual.parents) if (d / ARQUIVO_PROJETO).is_file()), None)
        if arquivo is None:
            raise SystemExit(f"nenhum {ARQUIVO_PROJETO} em {atual} nem nas pastas acima -- "
                             f"copie modelo-dados/{ARQUIVO_PROJETO} do modelo para a raiz do projeto")
    projeto = Projeto(arquivo)
    from validar_dados import PASTA_ESQUEMAS, erros_de
    schema = json.loads((PASTA_ESQUEMAS / ARQUIVO_PROJETO.replace(".json", ".schema.json")).read_text(encoding="utf-8"))
    erros = erros_de(projeto.dados, schema, schema)
    if erros:
        raise SystemExit("\n".join(f"ERRO em {projeto.arquivo}: {e}" for e in erros))
    return projeto


def impressao(arquivo):
    return hashlib.sha256(Path(arquivo).read_bytes()).hexdigest()


def separa_registro(texto):
    """(linhas do registro, resto do texto). O registro e o bloco entre "---" no topo."""
    linhas = texto.split("\n")
    if linhas and linhas[0] == "---" and "---" in linhas[1:]:
        fim = linhas.index("---", 1)
        return linhas[1:fim], "\n".join(linhas[fim + 1:])
    return [], texto


def fontes_registradas(texto):
    """{chave: (caminho, sha256)} do registro no topo do texto."""
    registro, _ = separa_registro(texto)
    out = {}
    for linha in registro:
        m = LINHA_FONTE.match(linha)
        if m:
            out[m.group("chave")] = (m.group("caminho"), m.group("hash"))
    return out


def situacao_da_copia(raiz, caminho, hash_registrado):
    """(arquivo, "confere" | "mudou" | "nao-existe")."""
    arquivo = (Path(raiz) / caminho).resolve()
    if not arquivo.exists():
        return arquivo, "nao-existe"
    return arquivo, "confere" if impressao(arquivo) == hash_registrado else "mudou"


def assinatura(*partes):
    junto = re.sub(r"\s+", " ", "|".join(str(p) for p in partes)).strip()
    return hashlib.sha256(junto.encode("utf-8")).hexdigest()[:12]


def tiques_anteriores(arquivo):
    """{(grupo, parte): (assinatura, {"IA": bool, "pessoa": bool})} de um arquivo de conferencia."""
    arquivo = Path(arquivo)
    if not arquivo.exists():
        return {}
    out, chave = {}, None
    for linha in arquivo.read_text(encoding="utf-8").split("\n"):
        m = MARCA_PARTE.match(linha)
        if m:
            chave = (m.group(1), m.group(2))
            out[chave] = (m.group(3), {"IA": False, "pessoa": False})
            continue
        m = TIQUE.match(linha)
        if m and chave in out:
            out[chave][1][m.group(2)] = m.group(1) != " "
    return out


def tiques_da_parte(anteriores, grupo, parte, sig):
    """(tiques, retirado): os tiques voltam se a assinatura e a mesma; se mudou, saem."""
    anterior = anteriores.get((grupo, str(parte)))
    if not anterior:
        return {"IA": False, "pessoa": False}, False
    if anterior[0] == sig:
        return anterior[1], False
    return {"IA": False, "pessoa": False}, any(anterior[1].values())


def marca(grupo, parte, sig):
    return f"<!-- parte: {grupo}|{parte}|{sig} -->"


def caixas(tiques):
    return [f"- [{'x' if tiques['IA'] else ' '}] IA", f"- [{'x' if tiques['pessoa'] else ' '}] pessoa"]


def comando(args):
    return subprocess.run(args, capture_output=True, text=True, check=True).stdout


def numero_de_paginas(pdf):
    m = re.search(r"^Pages:\s+(\d+)", comando(["pdfinfo", str(pdf)]), re.M)
    return int(m.group(1)) if m else 0


def imagem(pdf, n, pasta, nome, resolucao):
    """PNG da pagina, na resolucao dada (dpi), gerado de novo so se nao existe ou se o
    PDF e mais novo que ele."""
    pasta.mkdir(parents=True, exist_ok=True)
    base = pasta / f"{nome}-p{n:03d}"
    png = base.with_suffix(".png")
    if not png.exists() or png.stat().st_mtime < Path(pdf).stat().st_mtime:
        comando(["pdftoppm", "-f", str(n), "-l", str(n), "-r", str(resolucao), "-png", "-singlefile",
                 str(pdf), str(base)])
    return png


def link(alvo, saida):
    return Path(os.path.relpath(alvo, Path(saida).parent)).as_posix()


def ancora(texto):
    return re.sub(r"[^\w-]", "", texto.lower().replace(" ", "-"))
