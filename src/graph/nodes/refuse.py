
from src.graph.state import State


def refuse(state: State):
    """
    Retorna uma resposta fixa quando a solicitação não pode ser atendida.
    """

    return {
        "resultado": (
            "Pergunta fora do escopo. Este assistente responde apenas "
            "sobre frota e operações portuárias. Reformule sua pergunta."
        )
    }
