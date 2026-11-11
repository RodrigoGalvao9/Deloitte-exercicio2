import json

from src.graph.prompts.analyze_prompt import ANALYZE_PROMPT
from src.graph.state import State


def prepare(state: State) -> dict:
    """Monta as mensagens iniciais (prompt + frota) para o nó analyze."""
    mensagens = ANALYZE_PROMPT.format_messages(
        frota=json.dumps(state["frota"], ensure_ascii=False, indent=2),
        pergunta=state["pergunta"],
    )

    return {"messages": mensagens}
