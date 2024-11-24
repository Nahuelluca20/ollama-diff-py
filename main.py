from internal.git.git_diff import get_git_diff
from internal.ollama.chat import chat_ollama
from rich.console import Console
from rich.markdown import Markdown


def run_model():
    console = Console()
    diff = get_git_diff("main", "feat/git-proof")

    console.print(
        "[bold green]Welcome to the interactive chat! Type your question or '/bye' to exit.[/bold green]"
    )
    llm_context = []

    while True:
        question = console.input("[bold blue]Ask your question: [/bold blue]")
        if question.lower() == "/bye":
            console.print("[bold red]Goodbye![/bold red]")
            break
        response_text, context = chat_ollama(
            diff, question, "qwen2.5-coder:7b", llm_context
        )
        llm_context = context
        console.print(Markdown(response_text))


if __name__ == "__main__":
    run_model()
