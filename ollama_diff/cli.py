from ollama_diff.internal.git.git_diff import get_git_diff
from ollama_diff.internal.ollama.chat import chat_ollama, get_available_models
from rich.console import Console
from rich.markdown import Markdown
import questionary


def select_model():
    """
    Fetch and display available models, allowing the user to select one interactively.
    """
    console = Console()
    console.print("[bold yellow]Fetching available models...[/bold yellow]")

    # Fetch available models
    model_names = get_available_models()
    if not model_names:
        console.print("[bold red]No models available.[/bold red]")
        return None

    # Use questionary to create a selection prompt
    selected_model_name = questionary.select(
        "Select a model:",
        choices=model_names,
        qmark="👉",
    ).ask()

    if not selected_model_name:
        console.print("[bold red]No model selected. Exiting.[/bold red]")
        return None

    # Find and return the selected model object
    print(selected_model_name)
    return selected_model_name


def run_model():
    console = Console()
    console.print("[bold yellow]Select the branches to compare:[/bold yellow]")
    diff = get_git_diff()

    if diff.startswith("Error:"):
        console.print(f"[bold red]{diff}[/bold red]")
        return

    # Select model
    model = select_model()
    if not model:
        console.print("[bold red]No model selected. Exiting.[/bold red]")
        return

    console.print(f"[bold green]Selected model: {model}[/bold green]")
    console.print(
        "[bold green]Welcome to the interactive chat! Type your question or '/bye' to exit.[/bold green]"
    )
    llm_context = []

    while True:
        question = console.input("[bold blue]Ask your question: [/bold blue]")
        if question.lower() == "/bye":
            console.print("[bold red]Goodbye![/bold red]")
            break
        response_text, context = chat_ollama(diff, question, model, llm_context)
        llm_context = context
        console.print(Markdown(response_text))


if __name__ == "__main__":
    run_model()
