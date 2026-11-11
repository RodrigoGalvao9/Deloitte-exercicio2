
from langgraph.types import interrupt

from src.graph.state import State


def human_review(state: State) -> dict:
    decisao = interrupt({
        "recomendacao": state["recomendacao"]
    })

    return {
        "aprovado": decisao["aprovado"],
        "nota_operador": decisao.get("nota", "")
    }
