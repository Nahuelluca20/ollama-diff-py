from ollama_diff.internal.git.git_diff import get_git_diff
from ollama_diff.internal.ollama.chat import chat_ollama
from rich.console import Console
from rich.markdown import Markdown


def run_model():
    console = Console()
    console.print("[bold yellow]Selecciona las ramas para comparar:[/bold yellow]")
    diff = get_git_diff()

    if diff.startswith("Error:"):
        console.print(f"[bold red]{diff}[/bold red]")
        return

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
