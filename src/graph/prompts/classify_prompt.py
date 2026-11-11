from langchain_core.prompts import ChatPromptTemplate


CLASSIFY_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Você é um classificador de perguntas de um assistente
            de operações portuárias.

            Classifique a pergunta em apenas uma das intenções:

            - primeiro_a_chegar:
              Perguntas sobre qual navio chega primeiro ao porto.

            - regras:
              Perguntas sobre ETA, velocidade, tempestade,
              combustível e regras operacionais.

            - fora_escopo:
              Perguntas que não pertencem às operações portuárias.

            Não responda à pergunta.
            Apenas classifique a intenção.
            """
        ),
        ("human", "{pergunta}")
    ]
)
