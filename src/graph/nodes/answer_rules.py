from src.graph.prompts.answer_rules_prompt import RULES_PROMPT
from src.graph.state import State
from src.utils.llm_adapter import get_llm


def answer_rules(state: State) -> dict:
    chain = RULES_PROMPT | get_llm()
    resposta = chain.invoke({"pergunta": state["pergunta"]})

    return {"resultado": resposta.content}
