# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright do codigo sob GPL-3.0 -- ver LICENSE e NOTICE.md na raiz do projeto.

"""
Grava, no topo de um documento gerado, de qual arquivo ele veio: o caminho do arquivo
(relativo a raiz do projeto) e a impressao digital dele (sha256). E esse registro que
liga o documento gerado a sua fonte -- nunca o nome dos arquivos. Rodar de novo
atualiza a linha daquela fonte. Um documento que junta varias fontes tem uma linha por
fonte, cada uma com uma chave curta, que as partes do documento usam para dizer de onde
vieram.

Formato, no topo do documento:
    ---
    fonte: docs/material-base/AULA.pdf | sha256: <64 algarismos hexadecimais>
    ---
ou, com varias fontes:
    ---
    fonte BRASIL-2010: docs/material-base/fontes-externas/BRASIL_2010_guia.pdf | sha256: ...
    fonte OMS-2019: docs/material-base/fontes-externas/OMS_2019_manual.pdf | sha256: ...
    ---

Uso:
    python scripts/registrar_fonte.py DOCUMENTO.md FONTE
    python scripts/registrar_fonte.py DOCUMENTO.md FONTE --chave CHAVE
"""

import argparse
import hashlib
import os
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
LINHA_FONTE = re.compile(r"^fonte(?: (?P<chave>\S+))?: (?P<caminho>.+?) \| sha256: (?P<hash>[0-9a-f]{64})$")


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
    """{chave ("" quando a fonte e uma so): (caminho, sha256)}."""
    registro, _ = separa_registro(texto)
    out = {}
    for linha in registro:
        m = LINHA_FONTE.match(linha)
        if m:
            out[m.group("chave") or ""] = (m.group("caminho"), m.group("hash"))
    return out


def registra(documento, fonte, chave="", raiz=RAIZ):
    texto = documento.read_text(encoding="utf-8") if documento.exists() else ""
    registro, resto = separa_registro(texto)
    caminho = Path(os.path.relpath(Path(fonte).resolve(), Path(raiz).resolve())).as_posix()
    nova = f"fonte{' ' + chave if chave else ''}: {caminho} | sha256: {impressao(fonte)}"
    mantidas = [l for l in registro
                if not ((m := LINHA_FONTE.match(l)) and (m.group("chave") or "") == chave)]
    resto = resto.lstrip("\n")
    documento.write_text("\n".join(["---"] + mantidas + [nova, "---"]) + "\n" + ("\n" + resto if resto else ""),
                         encoding="utf-8")
    return nova


def main(argv=None):
    p = argparse.ArgumentParser(description="Grava no documento gerado de qual arquivo ele veio.")
    p.add_argument("documento", type=Path, help="documento gerado (.md)")
    p.add_argument("fonte", type=Path, help="arquivo de origem")
    p.add_argument("--chave", default="", help="chave curta da fonte, quando o documento junta varias")
    p.add_argument("--raiz", type=Path, default=RAIZ, help=f"raiz do projeto (padrao: {RAIZ})")
    a = p.parse_args(argv)
    if not a.fonte.exists():
        raise SystemExit(f"fonte nao encontrada: {a.fonte}")
    print(registra(a.documento, a.fonte, a.chave, a.raiz))
    return 0


if __name__ == "__main__":
    sys.exit(main())
