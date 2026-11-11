from src.graph.state import State
from src.graph.tools import TOOLS
from src.utils.llm_adapter import invocar_com_tools


def _extrair_texto(conteudo) -> str:
    if isinstance(conteudo, list):
        conteudo = "\n".join(
            item.get("text", "")
            for item in conteudo
            if isinstance(item, dict)
        )
    return str(conteudo).strip()


def analyze(state: State) -> dict:
    resposta = invocar_com_tools(state["messages"], TOOLS)

    # O modelo pediu ferramentas: o grafo segue para o nó "tools".
    if resposta.tool_calls:
        return {"messages": [resposta]}

    texto = _extrair_texto(resposta.content)
    if not texto:
        raise ValueError("O modelo retornou uma resposta vazia.")

    return {"messages": [resposta], "recomendacao": texto}
