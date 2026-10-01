# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright do codigo sob GPL-3.0 -- ver LICENSE e NOTICE.md na raiz do projeto.

"""
Gera pacotes Anki (.apkg) a partir de QUALQUER CSV de perguntas encontrado direto na
pasta do material gerado (sem entrar em subpastas -- uma eventual subpasta de material
arquivado de outra disciplina nao e conteudo ativo e nao deve ser descoberta aqui). O
script e agnostico de disciplina, de nome de coluna e de caminho: nenhum nome de
disciplina, item, arquivo ou pasta fica fixado no codigo. As pastas e o prefixo das
planilhas vem do projeto.json ("material_gerado", "baralhos" e "prefixo_planilhas").
O contrato estavel e minimo:

  1. o nome do arquivo comeca com o prefixo das planilhas e termina em ".csv";
  2. existe uma coluna "pergunta" e uma coluna "resposta" -- os dois unicos nomes de
     coluna que o script realmente exige, porque sao intrinsecos a qualquer cartao de
     revisao, nao especificos de nenhuma disciplina.

Qualquer outra coluna (disciplina, tipo_pergunta, fonte, ordem, ou qualquer nome que a
disciplina preferir) e opcional e vira campo do cartao automaticamente, com o nome que
a propria coluna tiver -- nao exige nenhuma mudanca neste script. Uma coluna
"disciplina", se presente, organiza os cartoes em subdecks por valor distinto; se
ausente, todos os cartoes desse CSV vao para um unico deck. Uma coluna "fonte" (a
citacao da fonte do fato, que a metodologia pede em toda planilha), se presente,
aparece no verso, abaixo da resposta.

Cada arquivo processado vira seu proprio pacote .apkg (nomeado a partir do proprio nome
do arquivo). O modelo de nota (campos e template do cartao) e construido a partir do
cabecalho de cada CSV -- CSVs com conjuntos de coluna diferentes ganham modelos
diferentes automaticamente, cada um com ID deterministico a partir do proprio conjunto
de colunas.

Uso (de qualquer pasta dentro do projeto):
    python scripts/montar_deck.py              # gera um .apkg para cada CSV encontrado
    python scripts/montar_deck.py <trecho>     # gera so os .apkg cujo nome de arquivo contem <trecho>
    python scripts/montar_deck.py --listar     # so lista os CSVs que seriam processados, sem gerar nada
    python scripts/montar_deck.py --projeto projeto.json
"""

import argparse
import csv
import hashlib
import re
import sys
import unicodedata
from pathlib import Path

import genanki

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comum import acha_projeto  # noqa: E402

# Coluna com papel de bastidor: se existir, vira campo do cartao (pra nao perder a
# informacao), mas nao aparece na linha de metadados do cartao -- so pra nao poluir a
# tela com numero de ordem toda vez. Nao e exigida.
COLUNAS_SO_CAMPO = {"ordem"}

# Coluna com a citacao da fonte do fato: se existir, aparece no verso, abaixo da
# resposta, e nao na linha de metadados da frente.
COLUNA_FONTE = "fonte"


def normalizar(texto):
    sem_acento = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("ascii")
    return sem_acento.lower()


def campo_anki(nome_coluna):
    """Nome de coluna do CSV -> nome de campo do Anki (ex.: "tipo_pergunta" ->
    "TipoPergunta"). Sem espaco, pra nao arriscar problema de sintaxe no template do
    Anki. So formata para leitura -- nao muda o que a coluna significa, e nao presume
    nenhum nome especifico de coluna."""
    return "".join(p.capitalize() for p in re.split(r"[_\s]+", nome_coluna) if p) or "Campo"


def construir_modelo(colunas_extra, rotulo):
    """Monta um genanki.Model com campos Pergunta, Resposta, mais um campo pra cada
    coluna extra que o CSV realmente tiver -- nenhum nome de coluna e exigido pra isso
    funcionar. CSVs com conjuntos de coluna diferentes ganham modelos diferentes, cada
    um com ID deterministico a partir do proprio conjunto de colunas, entao o mesmo
    "formato" de CSV sempre reusa o mesmo modelo ao reimportar."""
    campos_extra = [campo_anki(c) for c in colunas_extra]
    campos_visiveis = [
        campo_anki(c)
        for c in colunas_extra
        if c.lower() not in COLUNAS_SO_CAMPO and c.lower() != COLUNA_FONTE
    ]
    campo_fonte = next(
        (campo_anki(c) for c in colunas_extra if c.lower() == COLUNA_FONTE), None
    )
    assinatura = ",".join(colunas_extra) or "minimo"
    model_id = id_estavel("modelo::" + assinatura)

    linha_meta = "".join(
        f"{{{{#{c}}}}}<span class=\"meta-item\">{{{{{c}}}}}</span>{{{{/{c}}}}}"
        for c in campos_visiveis
    )

    return genanki.Model(
        model_id,
        f"Nucleo Multidisciplina - {rotulo}",
        fields=[{"name": "Pergunta"}, {"name": "Resposta"}] + [{"name": c} for c in campos_extra],
        templates=[{
            "name": "Cartao Padrao",
            "qfmt": f'<div class="meta">{linha_meta}</div><div class="pergunta">{{{{Pergunta}}}}</div>',
            "afmt": (
                '{{FrontSide}}<hr id="answer">'
                '<div class="resposta">{{Resposta}}</div>'
                + (
                    f'{{{{#{campo_fonte}}}}}<div class="fonte">{{{{{campo_fonte}}}}}</div>{{{{/{campo_fonte}}}}}'
                    if campo_fonte
                    else ""
                )
            ),
        }],
        css="""
        .card { font-family: Arial, sans-serif; font-size: 18px; text-align: center; color: #1a1a1a; }
        .meta { color: #888; font-size: 13px; text-transform: uppercase; letter-spacing: .05em; margin-bottom: 8px; }
        .meta-item:not(:last-child)::after { content: " • "; }
        .pergunta { font-weight: 600; }
        .resposta { margin-top: 10px; }
        .fonte { color: #888; font-size: 13px; margin-top: 12px; }
        """,
    )


def id_estavel(nome, minimo=1_000_000_000, maximo=1_999_999_999):
    """ID deterministico de 10 digitos a partir do nome do deck: o mesmo nome sempre
    gera o mesmo ID, sem precisar cadastrar cada disciplina manualmente no codigo.
    Reimportar o mesmo .apkg atualiza os cartoes existentes no Anki em vez de duplicar
    o deck, desde que o nome do deck nao mude."""
    digest = hashlib.sha256(nome.encode("utf-8")).hexdigest()
    return minimo + (int(digest, 16) % (maximo - minimo))


def descobrir_csvs(pasta, prefixo, filtro=None):
    """Lista os CSVs de perguntas prontos para virar deck: qualquer <prefixo>*.csv
    direto dentro da pasta (nao entra em subpastas -- uma eventual subpasta de material
    arquivado de outra disciplina nao e ativa e nao deve ser descoberta aqui). `filtro`,
    se dado, mantem so arquivos cujo nome contenha o trecho (case-insensitive)."""
    candidatos = sorted(pasta.glob(f"{prefixo}*.csv"))
    if filtro:
        alvo = filtro.lower()
        candidatos = [c for c in candidatos if alvo in c.name.lower()]
    return candidatos


def nomes_a_partir_do_arquivo(caminho_csv: Path, prefixo: str):
    """"<prefixo>nucleo-dicionarios.csv" -> familia "Nucleo", nome de saida
    "Nucleo-Dicionarios". Tira o prefixo (se existir) e capitaliza cada palavra
    separada por hifen -- funciona pra qualquer nome de arquivo novo."""
    nome = caminho_csv.stem
    if prefixo and nome.startswith(prefixo):
        nome = nome[len(prefixo):]
    partes = [p for p in nome.split("-") if p] or [caminho_csv.stem]
    familia = partes[0].capitalize()
    nome_saida = "-".join(p.capitalize() for p in partes)
    return familia, nome_saida


def montar_pacote(caminho_csv: Path, pasta_saida: Path, prefixo: str):
    familia, nome_saida = nomes_a_partir_do_arquivo(caminho_csv, prefixo)

    decks = {}  # chave de deck normalizada -> genanki.Deck, criado sob demanda
    total_cartoes = 0

    with open(caminho_csv, encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        colunas = leitor.fieldnames or []
        if "pergunta" not in colunas or "resposta" not in colunas:
            raise ValueError(
                f'{caminho_csv.name}: precisa ter uma coluna "pergunta" e uma '
                f'"resposta" -- sao os dois unicos nomes de coluna exigidos '
                f"(colunas encontradas: {colunas})."
            )
        colunas_extra = [c for c in colunas if c not in ("pergunta", "resposta")]
        modelo = construir_modelo(colunas_extra, nome_saida)
        tem_disciplina = "disciplina" in colunas

        for linha in leitor:
            disciplina = linha.get("disciplina", "").strip()

            nota = genanki.Note(
                model=modelo,
                fields=[linha["pergunta"].strip(), linha["resposta"].strip()]
                + [linha[c].strip() for c in colunas_extra],
            )

            if tem_disciplina:
                chave_deck = normalizar(disciplina)
                nome_deck = f"{familia}::{disciplina.capitalize()}" if disciplina else familia
            else:
                chave_deck, nome_deck = "", familia
            if chave_deck not in decks:
                decks[chave_deck] = genanki.Deck(id_estavel(nome_deck), nome_deck)
            decks[chave_deck].add_note(nota)
            total_cartoes += 1

    caminho_saida = pasta_saida / f"{nome_saida}.apkg"
    pacote = genanki.Package(list(decks.values()))
    pasta_saida.mkdir(parents=True, exist_ok=True)
    pacote.write_to_file(caminho_saida)

    print(f"Deck gerado: {caminho_saida}")
    print(f"  Subdecks: {', '.join(d.name for d in decks.values())}")
    print(f"  Total de cartoes: {total_cartoes}")


def main(argv=None):
    p = argparse.ArgumentParser(description="Gera pacotes Anki (.apkg) a partir das planilhas de perguntas.")
    p.add_argument("filtro", nargs="?", help="gera so as planilhas cujo nome contem este trecho")
    p.add_argument("--listar", action="store_true", help="so lista as planilhas, sem gerar nada")
    p.add_argument("--projeto", type=Path, help="projeto.json (padrao: o primeiro achado subindo a partir daqui)")
    a = p.parse_args(argv)
    projeto = acha_projeto(a.projeto)
    pasta, prefixo = projeto.caminho("material_gerado"), projeto.valor("prefixo_planilhas")

    csvs = descobrir_csvs(pasta, prefixo, a.filtro)
    if not csvs:
        alvo_desc = f" com filtro {a.filtro!r}" if a.filtro else ""
        raise SystemExit(f"nenhum CSV '{prefixo}*.csv' encontrado em {pasta}{alvo_desc}")

    print(f"CSVs encontrados ({len(csvs)}): {', '.join(c.name for c in csvs)}")
    if a.listar:
        return 0
    for caminho in csvs:
        montar_pacote(caminho, projeto.caminho("baralhos"), prefixo)
    return 0


if __name__ == "__main__":
    sys.exit(main())
