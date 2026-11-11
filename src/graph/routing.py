from src.graph.state import State


def route_by_intent(state: State) -> str:
    """Devolve a intenção classificada; o builder mapeia para o próximo nó."""
    return state["intent"]
