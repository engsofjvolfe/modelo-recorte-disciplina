# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright do codigo sob GPL-3.0 -- ver LICENSE e NOTICE.md na raiz do projeto.

"""
Monta as referencias do projeto a partir dos dados. Le o arquivo de fontes, confere o
arquivo contra o schema dele, formata cada fonte pela ABNT NBR 6023 e grava:

  - o arquivo de referencias: so as referencias, em ordem alfabetica, como a lista de
    referencias do fim de um trabalho;
  - a conferencia das referencias: para cada fonte, a referencia como ficou, a copia
    registrada dela (com a imagem da primeira pagina, se for PDF, pra conferir contra a
    folha de rosto) e as caixas de tique "IA" e "pessoa". Se os dados da referencia ou a
    copia mudarem depois do tique, o tique e retirado.

Os caminhos vem do projeto.json: "fontes", "referencias", "conferencia_referencias",
"gerados", "licenca_conteudo" e "imagens", e a resolucao das imagens, de
"resolucao_imagens".

A copia de cada fonte e achada pelo registro no topo dos documentos gerados (ver
registrar_fonte.py), pela chave. O script lista no terminal as chaves registradas que
ainda nao tem referencia e as referencias que faltam conferir.

Tipos de fonte: "monografia" (livro, guia, manual, documento ou pagina online, material
de aula), "parte" (capitulo ou parte de uma monografia), "artigo" (de periodico) e
"outro" (a referencia vem pronta, no campo "referencia", e so passa pela conferencia).
Sem autoria, a entrada e pelo titulo, que vai nos dados ja com a primeira palavra em
maiusculas, como a norma pede, e sem destaque.

Uso (de qualquer pasta dentro do projeto):
    python scripts/referencias.py
    python scripts/referencias.py --projeto projeto.json
"""

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comum import (acha_projeto, ancora, assinatura, caixas, fontes_registradas, imagem, link, marca,  # noqa: E402
                   situacao_da_copia, tiques_anteriores, tiques_da_parte)
from validar_dados import PASTA_ESQUEMAS, erros_de  # noqa: E402

MESES = ["jan.", "fev.", "mar.", "abr.", "maio", "jun.", "jul.", "ago.", "set.", "out.", "nov.", "dez."]
SITUACAO = {"confere": "é a mesma do registro", "mudou": "mudou depois do registro", "nao-existe": "não existe"}


# ---------- formatacao pela NBR 6023 ----------

def data_abnt(valor):
    """"2024-09-04" -> "4 set. 2024"; "2024-09" -> "set. 2024"; outro valor fica como esta."""
    m = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", valor)
    if m:
        return f"{int(m.group(3))} {MESES[int(m.group(2)) - 1]} {m.group(1)}"
    m = re.fullmatch(r"(\d{4})-(\d{2})", valor)
    if m:
        return f"{MESES[int(m.group(2)) - 1]} {m.group(1)}"
    return valor


def ponto(texto):
    texto = texto.rstrip()
    return texto if texto.endswith((".", "?", "!")) else texto + "."


def autor(a):
    if "entidade" in a:
        texto = ". ".join([a["entidade"][0].upper()] + a["entidade"][1:])
        if a.get("qualificador"):
            texto += f" ({a['qualificador']})"
    else:
        texto = a["sobrenome"].upper() + (f", {a['prenomes']}" if a.get("prenomes") else "")
    return texto + (f" ({a['funcao']})" if a.get("funcao") else "")


def autoria(autores):
    return "; ".join(autor(a) for a in autores)


def titulo(obra, destaque):
    t = f"**{obra['titulo']}**" if destaque else obra["titulo"]
    return t + (f": {obra['subtitulo']}" if obra.get("subtitulo") else "")


def publicacao(obra):
    """Local: editora, data -- com [S. l.] e [s. n.] onde faltar."""
    local, editora = obra.get("local"), obra.get("editora")
    if local and editora:
        texto = f"{local}: {editora}"
    elif local:
        texto = f"{local}: [*s. n.*]"
    elif editora:
        texto = f"[*S. l.*]: {editora}"
    else:
        texto = "[*S. l.*: *s. n.*]"
    return f"{texto}, {data_abnt(obra['data'])}"


def obra_inteira(obra):
    """Elementos de uma monografia: titulo (com destaque se ha autoria), edicao e publicacao."""
    tem_autoria = bool(obra.get("autores"))
    els = ([autoria(obra["autores"])] if tem_autoria else []) + [titulo(obra, tem_autoria)]
    if obra.get("edicao"):
        els.append(obra["edicao"])
    return els + [publicacao(obra)]


def referencia(f):
    if f["tipo"] == "outro":
        return f["referencia"]
    if f["tipo"] == "monografia":
        els = obra_inteira(f)
    elif f["tipo"] == "parte":
        els = ([autoria(f["autores"])] if f.get("autores") else []) + [titulo(f, False)]
        livro = obra_inteira(f["parte_de"])
        els += ["In: " + livro[0]] + livro[1:] + [f"p. {f['paginas']}"]
    else:  # artigo
        els = ([autoria(f["autores"])] if f.get("autores") else []) + [titulo(f, False)]
        pub = [f"**{f['periodico']}**"] + [f[c] for c in ("local",) if f.get(c)]
        pub += [f"{p} {f[c]}" for c, p in (("volume", "v."), ("numero", "n."), ("paginas", "p.")) if f.get(c)]
        els.append(", ".join(pub + [data_abnt(f["data"])]))
    if f.get("descricao_fisica"):
        els.append(f["descricao_fisica"])
    if f.get("serie"):
        els.append(f"({f['serie']})")
    els += f.get("notas", [])
    if f.get("isbn"):
        els.append(f"ISBN {f['isbn']}")
    if f.get("doi"):
        els.append(f"DOI: {f['doi']}")
    if f.get("url"):
        els.append(f"Disponível em: {f['url']}")
    if f.get("acesso"):
        els.append(f"Acesso em: {data_abnt(f['acesso'])}")
    return " ".join(ponto(e) for e in els)


def ordem(texto):
    """Chave de ordem alfabetica: sem destaque, sem colchetes, sem acento, em maiusculas."""
    simples = unicodedata.normalize("NFKD", re.sub(r"[*\[\]]", "", texto))
    return "".join(c for c in simples if not unicodedata.combining(c)).upper()


# ---------- arquivos ----------

def copias_registradas(transcricoes, raiz):
    """{chave: [(documento, arquivo, situacao, hash registrado)]} dos registros dos documentos gerados."""
    out = {}
    for doc in sorted(transcricoes.glob("*.md")):
        for chave, (caminho, hash_registrado) in fontes_registradas(doc.read_text(encoding="utf-8")).items():
            arquivo, situacao = situacao_da_copia(raiz, caminho, hash_registrado)
            out.setdefault(chave, []).append((doc, arquivo, situacao, hash_registrado))
    return out


def grava_fontes_md(refs, saida, licenca):
    corpo = ["# Referências", ""] + [linha for _, r in refs for linha in (r, "")]
    corpo += ["---", "", f"*Este documento está licenciado sob [CC BY-NC-SA 4.0]({link(licenca, saida)}).*"]
    saida.parent.mkdir(parents=True, exist_ok=True)
    saida.write_text("\n".join(corpo) + "\n", encoding="utf-8")


def grava_conferencia(refs, fontes, copias, saida, pasta_img, resolucao):
    anteriores = tiques_anteriores(saida)
    por_chave = {f["chave"]: f for f in fontes}
    resumo, corpo, sem_pessoa = [], [], []
    for chave, ref in refs:
        cs = copias.get(chave, [])
        sig = assinatura(json.dumps(por_chave[chave], ensure_ascii=False, sort_keys=True),
                         *sorted(f"{a}|{h}" for _, a, _, h in cs))
        tiques, retirado = tiques_da_parte(anteriores, "referencias", chave, sig)
        if not tiques["pessoa"]:
            sem_pessoa.append(chave)
        situacoes = ", ".join(dict.fromkeys(SITUACAO[s] for _, _, s, _ in cs)) or "nenhuma"
        resumo.append(f"| [{chave}](#{ancora(chave)}) | {situacoes} | "
                      f"{'sim' if tiques['IA'] else 'não'} | {'sim' if tiques['pessoa'] else 'não'} |")
        corpo += ["", "---", "", f"## {chave}", "", marca("referencias", chave, sig), "", f"> {ref}", ""]
        if not cs:
            corpo += ["Cópia registrada: nenhuma", ""]
        for doc, arquivo, situacao, _ in cs:
            corpo += [f"Cópia registrada: `{link(arquivo, saida)}` ({SITUACAO[situacao]}), no registro de "
                      f"`{link(doc, saida)}`", ""]
            if arquivo.suffix.lower() == ".pdf" and situacao != "nao-existe":
                nome = re.sub(r"[^\w.-]", "_", chave)
                corpo += [f"[original, primeira página]({link(arquivo, saida)}#page=1)", "",
                          f"![{chave}, primeira página]({link(imagem(arquivo, 1, pasta_img, nome, resolucao), saida)})", ""]
        if retirado:
            corpo += ["Tique retirado: os dados da referência ou a cópia mudaram depois do tique", ""]
        corpo += caixas(tiques)
    cabecalho = ["# Conferência das referências", "",
                 "| Chave | Cópia registrada | Tique da IA | Tique da pessoa |",
                 "| :--- | :--- | :---: | :---: |"] + resumo
    saida.parent.mkdir(parents=True, exist_ok=True)
    saida.write_text("\n".join(cabecalho + corpo) + "\n", encoding="utf-8")
    return sem_pessoa


def roda(projeto, chave_nova=None):
    fontes, saida = projeto.caminho("fontes"), projeto.caminho("referencias")
    conferencia, transcricoes = projeto.caminho("conferencia_referencias"), projeto.caminho("gerados")
    if not fontes.exists():
        print(f"FALTA REFERÊNCIA: {fontes} não existe -- crie a partir de modelo-dados/fontes.json do modelo"
              + (f" e acrescente a chave {chave_nova}" if chave_nova else ""))
        return 1
    dados = json.loads(fontes.read_text(encoding="utf-8"))
    schema = json.loads((PASTA_ESQUEMAS / "fontes.schema.json").read_text(encoding="utf-8"))
    erros = erros_de(dados, schema, schema)
    if erros:
        for e in erros:
            print(f"ERRO em {fontes.name}: {e}")
        return 1
    lista = dados["fontes"]
    refs = sorted(((f["chave"], referencia(f)) for f in lista), key=lambda x: ordem(x[1]))
    grava_fontes_md(refs, saida, projeto.caminho("licenca_conteudo"))
    copias = copias_registradas(transcricoes, projeto.raiz) if transcricoes.exists() else {}
    sem_pessoa = grava_conferencia(refs, lista, copias, conferencia, projeto.pasta_de_imagens(conferencia),
                                   projeto.valor("resolucao_imagens"))
    chaves = {f["chave"] for f in lista}
    faltam = sorted(set(copias) - chaves)
    print(f"{len(refs)} referência(s) gravadas em {saida}")
    print(f"conferência: {conferencia}")
    if chave_nova and chave_nova not in chaves and chave_nova not in faltam:
        faltam.append(chave_nova)
    for chave in faltam:
        print(f"FALTA REFERÊNCIA: a chave {chave} está registrada, mas não está em {fontes.name}")
    if sem_pessoa:
        print(f"CONFERIR: {len(sem_pessoa)} referência(s) sem o tique da pessoa: {', '.join(sem_pessoa)}")
    return 1 if faltam else 0


def main(argv=None):
    a = argparse.ArgumentParser(description="Monta as referências do projeto a partir do arquivo de fontes.")
    a.add_argument("--projeto", type=Path, help="projeto.json (padrao: o primeiro achado subindo a partir daqui)")
    args = a.parse_args(argv)
    return roda(acha_projeto(args.projeto))


if __name__ == "__main__":
    sys.exit(main())
