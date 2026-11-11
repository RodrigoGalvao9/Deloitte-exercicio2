import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

# Alguns modelos (ex.: gpt-oss no Groq) às vezes geram uma tool call inválida
# e a API responde 400 "output_parse_failed". Com temperatura 0 a repetição
# daria o mesmo resultado, então o retry varia a temperatura.
TEMPERATURAS_RETRY = [0, 0.3, 0.6]


def get_llm(temperature: float = 0):
    return init_chat_model(
        model=os.environ["LLM_MODEL"],
        model_provider=os.environ["LLM_PROVIDER"],
        temperature=temperature,
    )


def invocar_com_tools(mensagens, tools):
    """Chama o modelo com ferramentas, repetindo se a saída não for parseável."""
    for temperatura in TEMPERATURAS_RETRY:
        llm = get_llm(temperatura).bind_tools(tools)
        try:
            return llm.invoke(mensagens)
        except Exception as erro:
            if "output_parse_failed" not in str(erro):
                raise
            ultimo_erro = erro

    raise ultimo_erro
