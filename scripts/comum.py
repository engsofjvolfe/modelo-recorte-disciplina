# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright do codigo sob GPL-3.0 -- ver LICENSE e NOTICE.md na raiz do projeto.

"""
Funcoes que os outros scripts usam: achar o projeto e as planilhas de pergunta, o
registro da fonte no topo de um documento gerado, a impressao digital de um arquivo, os
tiques de um arquivo de conferencia e a imagem de uma pagina de PDF. Nao e para rodar
sozinho.

Nenhum caminho fica no codigo. O projeto e achado pelo arquivo "projeto.json", subindo
de pasta em pasta a partir de onde o script e chamado (ou pelo arquivo indicado com
--projeto), e todo caminho sai dele, relativo a pasta onde ele esta. O nome
"projeto.json" e fixo: e por ele que o script reconhece o projeto. A pasta do material de
base tambem: o schema do projeto.json so aceita o lugar dela e poe dentro dela tudo o que
tem texto de terceiros, e e ela que o .gitignore deixa de fora.

Registro da fonte, no topo do documento gerado (uma linha por fonte; a chave e a mesma
da referencia da fonte no arquivo de fontes do projeto):
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
import shutil
import subprocess
from pathlib import Path

ARQUIVO_PROJETO = "projeto.json"
LINHA_FONTE = re.compile(r"^fonte (?P<chave>\S+): (?P<caminho>.+?) \| sha256: (?P<hash>[0-9a-f]{64})$")
MARCA_PARTE = re.compile(r"^<!-- parte: ([^|]+)\|([^|]+)\|([0-9a-f]+) -->$")
TIQUE = re.compile(r"^- \[([ xX])\] (IA|pessoa)\s*$")
VARIAVEL = re.compile(r"\{[^{}]+\}")


class Projeto:
    """Os caminhos do projeto, lidos do projeto.json, relativos a pasta dele."""

    def __init__(self, arquivo):
        self.arquivo = Path(arquivo).resolve()
        self.raiz = self.arquivo.parent
        self.dados = json.loads(self.arquivo.read_text(encoding="utf-8"))

    def caminho(self, nome):
        return self.raiz / self.dados["caminhos"][nome]

    def caminho_com(self, nome, valor):
        """Caminho que o projeto.json da com uma variavel entre chaves, como "{item}" ou
        "{planilha}", com o valor no lugar dela."""
        return self.raiz / VARIAVEL.sub(lambda _: valor, self.dados["caminhos"][nome])

    def todos_com(self, nome):
        """Arquivos que existem para o modelo de caminho com variavel (qualquer valor)."""
        return sorted(self.raiz.glob(VARIAVEL.sub("*", self.dados["caminhos"][nome])))

    def valor(self, nome):
        return self.dados[nome]

    def pasta_de_imagens(self, conferencia):
        """Pasta das imagens de um arquivo de conferencia: dentro da pasta de imagens do
        projeto, uma subpasta com o nome do proprio arquivo de conferencia."""
        return self.caminho("imagens") / Path(conferencia).stem


def procura_projeto():
    """O primeiro projeto.json achado subindo a partir da pasta atual, ou None."""
    atual = Path.cwd().resolve()
    return next((d / ARQUIVO_PROJETO for d in (atual, *atual.parents) if (d / ARQUIVO_PROJETO).is_file()), None)


def acha_projeto(arquivo=None):
    """O projeto.json indicado, ou o primeiro achado subindo a partir da pasta atual."""
    if arquivo is None:
        arquivo = procura_projeto()
        if arquivo is None:
            raise SystemExit(f"nenhum {ARQUIVO_PROJETO} em {Path.cwd().resolve()} nem nas pastas acima -- "
                             f"copie modelo-dados/{ARQUIVO_PROJETO} do modelo para a raiz do projeto")
    projeto = Projeto(arquivo)
    from validar_dados import PASTA_ESQUEMAS, erros_de
    schema = json.loads((PASTA_ESQUEMAS / ARQUIVO_PROJETO.replace(".json", ".schema.json")).read_text(encoding="utf-8"))
    erros = erros_de(projeto.dados, schema, schema)
    if erros:
        raise SystemExit("\n".join(f"ERRO em {projeto.arquivo}: {e}" for e in erros))
    return projeto


def planilhas(projeto, filtro=None):
    """As planilhas de pergunta: os CSVs direto na pasta do material gerado (sem entrar em
    subpastas) cujo nome comeca com o prefixo do projeto; com filtro, so as que tem o
    trecho no nome, sem diferenca entre maiuscula e minuscula."""
    pasta, prefixo = projeto.caminho("material_gerado"), projeto.valor("prefixo_planilhas")
    todas = sorted(pasta.glob(f"{prefixo}*.csv"))
    return [c for c in todas if filtro.lower() in c.name.lower()] if filtro else todas


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


def dentro(caminho, pasta):
    """Se o caminho fica dentro da pasta (ou e a propria pasta)."""
    try:
        Path(caminho).resolve().relative_to(Path(pasta).resolve())
        return True
    except ValueError:
        return False


def ignorados_pelo_git(raiz, arquivos):
    """O conjunto dos arquivos que a lista do que nao vai ao GitHub (o .gitignore) deixa de
    fora, numa pergunta so ao git; None se o projeto nao usa o git ou se o git nao esta
    instalado."""
    arquivos = [Path(a).resolve() for a in arquivos]
    try:
        r = subprocess.run(["git", "-C", str(raiz), "check-ignore", "--no-index", "--stdin", "-z"],
                           input="\0".join(map(str, arquivos)).encode("utf-8"), capture_output=True)
    except FileNotFoundError:
        return None
    if r.returncode not in (0, 1):
        return None
    return {Path(p).resolve() for p in r.stdout.decode("utf-8").split("\0") if p}


def ignorado_pelo_git(raiz, caminho):
    """True ou False pra um arquivo so; None como em ignorados_pelo_git."""
    ignorados = ignorados_pelo_git(raiz, [caminho])
    return None if ignorados is None else Path(caminho).resolve() in ignorados


def registros(projeto):
    """[(documento, chave, caminho do arquivo da fonte, sha256)] de todos os documentos
    gerados que registram fonte: as transcricoes e as bases do material de fora."""
    documentos = sorted(set(projeto.caminho("gerados").glob("*.md")) | set(projeto.todos_com("base_externa")))
    return [(doc, chave, projeto.raiz / caminho, h) for doc in documentos
            for chave, (caminho, h) in fontes_registradas(doc.read_text(encoding="utf-8")).items()]


def impressoes_das_fontes(projeto):
    """{sha256: arquivo}: cada arquivo da pasta do material de base que a lista do que nao
    vai ao GitHub deixa de fora (todos, se o projeto nao usa o git) e cada fonte
    registrada, onde quer que esteja."""
    arquivos = [a for a in sorted(projeto.caminho("material_base").rglob("*")) if a.is_file()]
    ignorados = ignorados_pelo_git(projeto.raiz, arquivos)
    out = {impressao(a): a for a in arquivos if ignorados is None or a.resolve() in ignorados}
    for _, _, arquivo, h in registros(projeto):
        out.setdefault(h, arquivo)
    return out


def leva_para(arquivo, pasta, sem_perguntar=False):
    """Move o arquivo pra pasta, depois de mostrar de onde pra onde e a pessoa confirmar
    (ou direto, com sem_perguntar). Devolve o caminho novo, ou None se nao moveu."""
    arquivo, destino = Path(arquivo), Path(pasta) / Path(arquivo).name
    if destino.exists():
        if impressao(destino) != impressao(arquivo):
            print(f"ERRO: já existe outro arquivo com o nome {destino.name} em {pasta}; renomeie um dos dois")
            return None
        print(f"Já existe uma cópia igual em {destino}; ela é que vale. A cópia em {arquivo} pode ser apagada.")
        return destino
    print(f"A fonte {arquivo} está fora da pasta protegida, onde poderia acabar publicada.")
    print(f"Ela pode ir para {destino}.")
    if not sem_perguntar:
        try:
            resposta = input("Digite s pra mover ou n pra deixar onde está: ")
        except EOFError:
            resposta = ""
        if resposta.strip().lower() not in ("s", "sim"):
            print("Nada foi movido.")
            return None
    destino.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(arquivo), str(destino))
    print(f"Movida para {destino}.")
    return destino


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
