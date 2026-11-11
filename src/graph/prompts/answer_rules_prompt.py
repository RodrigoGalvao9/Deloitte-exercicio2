
from langchain_core.prompts import ChatPromptTemplate


REGRAS = """
1. ETA:
   ETA em horas = distância em milhas náuticas /
   velocidade efetiva em nós.

2. TEMPESTADE:
   Navios em tempestade não podem ultrapassar 12 nós.
   Velocidade efetiva = min(velocidade original, 12).

3. RESERVA DE COMBUSTÍVEL:
   O combustível disponível deve ser maior ou igual
   à reserva mínima informada para o navio.
   Se combustível < reserva, o navio não pode zarpar.

4. SELEÇÃO:
   Somente navios aprovados na verificação de combustível
   participam da comparação de ETA.
"""


RULES_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Responda de forma clara e objetiva, usando "
            "somente as seguintes regras:\n" + REGRAS
        ),
        ("human", "{pergunta}")
    ]
)
