from typing import Literal

from pydantic import BaseModel, Field

from src.graph.prompts.classify_prompt import CLASSIFY_PROMPT
from src.graph.state import State
from src.utils.llm_adapter import get_llm


class Intencao(BaseModel):
    intent: Literal[
        "primeiro_a_chegar",
        "regras",
        "fora_escopo",
    ] = Field(description="Intenção identificada na pergunta")


def classify(state: State) -> dict:
    chain = CLASSIFY_PROMPT | get_llm().with_structured_output(Intencao)
    resposta = chain.invoke({"pergunta": state["pergunta"]})

    return {"intent": resposta.intent}
