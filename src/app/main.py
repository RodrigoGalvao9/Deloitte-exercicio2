import sys
import uuid

from langgraph.types import Command

from src.graph.builder import build_graph
from src.utils.langfuse_client import flush, run_config

# Cada ciclo do agente (analyze + tools) gasta 2 passos; o padrão (25) é curto
# para uma frota de 4 navios.
LIMITE_PASSOS = 60


def pedir_aprovacao(recomendacao: str) -> dict:
    """Mostra a recomendação e coleta a decisão do operador."""
    print("\nRecomendação do agente:")
    print(recomendacao)

    aprovado = input("\nAprovar? (s/n): ").strip().lower() == "s"
    nota = input("Nota (opcional): ").strip()

    return {"aprovado": aprovado, "nota": nota}


def responder(graph, pergunta: str) -> str:
    """Executa o grafo para uma pergunta e devolve o texto final."""
    # Um thread_id novo por pergunta evita vazar estado entre perguntas.
    config = run_config(
        configurable={"thread_id": str(uuid.uuid4())},
        recursion_limit=LIMITE_PASSOS,
    )

    saida = graph.invoke({"pergunta": pergunta}, config)

    if "__interrupt__" in saida:
        pedido = saida["__interrupt__"][0].value
        decisao = pedir_aprovacao(pedido["recomendacao"])
        saida = graph.invoke(Command(resume=decisao), config)

    return saida.get("resultado", "Nenhuma resposta gerada.")


def main() -> None:
    # O modelo pode devolver caracteres fora do cp1252 (ex.: '‑'); sem UTF-8 o print falha no Windows.
    sys.stdout.reconfigure(encoding="utf-8")
    graph = build_graph()

    print("=" * 55)
    print("       ASSISTENTE DE OPERAÇÕES PORTUÁRIAS")
    print("=" * 55)
    print("Digite 'sair' para encerrar.")

    try:
        while True:
            pergunta = input("\nPergunta: ").strip()

            if not pergunta:
                print("Digite uma pergunta válida.")
                continue

            if pergunta.lower() in ["sair", "exit", "quit"]:
                print("\nEncerrando o assistente. Até logo!")
                break

            try:
                print(f"\nResposta: {responder(graph, pergunta)}")
            except Exception as erro:
                print(f"\nErro ao processar a pergunta: {erro}")

    except KeyboardInterrupt:
        print("\n\nFluxo interrompido pelo usuário (Ctrl + C).")

    finally:
        flush()


if __name__ == "__main__":
    main()
