
import json
import os
from pathlib import Path

from src.graph.state import State

FROTA_PADRAO = "frota_tempestade.json"


def receive(state: State) -> dict:
    caminho = (
        Path(__file__).resolve().parents[3]
        / "dados"
        / os.getenv("FROTA_ARQUIVO", FROTA_PADRAO)
    )

    with open(caminho, "r", encoding="utf-8") as arquivo:
        frota = json.load(arquivo)

    return {"frota": frota}
