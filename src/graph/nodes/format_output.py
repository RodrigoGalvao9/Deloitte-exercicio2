
from src.graph.state import State


def format_output(state: State) -> dict:
    recomendacao = state.get("recomendacao", "")
    aprovado = state.get("aprovado", False)
    nota = state.get("nota_operador", "")

    if aprovado:
        resultado = (
            "APROVADO pelo operador.\n\n"
            f"Recomendação:\n{recomendacao}"
        )
    else:
        resultado = (
            "REJEITADO pelo operador.\n\n"
            f"Recomendação:\n{recomendacao}"
        )

    if nota:
        resultado += f"\n\nNota do operador: {nota}"

    return {"resultado": resultado}
