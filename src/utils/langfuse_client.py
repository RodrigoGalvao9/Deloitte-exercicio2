import os


def get_langfuse_handler():
    if not (os.getenv("LANGFUSE_PUBLIC_KEY") and os.getenv("LANGFUSE_SECRET_KEY")):
        return None
    from langfuse.langchain import CallbackHandler

    return CallbackHandler()


def run_config(**extra) -> dict:
    handler = get_langfuse_handler()
    config = {"callbacks": [handler]} if handler else {}
    config.update(extra)
    return config


def flush() -> None:
    if os.getenv("LANGFUSE_PUBLIC_KEY") and os.getenv("LANGFUSE_SECRET_KEY"):
        from langfuse import get_client

        get_client().flush()