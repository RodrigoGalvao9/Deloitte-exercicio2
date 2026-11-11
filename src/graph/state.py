from typing import TypedDict, Annotated

from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages


class State(TypedDict, total=False):
    pergunta: str
    intent: str
    frota: dict
    messages: Annotated[list[AnyMessage], add_messages]

    recomendacao: str
    aprovado: bool
    nota_operador: str

    resultado: str
