from internal.git.git_diff import get_git_diff
from internal.ollama.chat import chat_ollama

# qwen2.5-coder:7b


# def RunModel():
#     diff = git_diff("main", "feat/git-proof")
#     chat(diff, "What is the difference between these branches", "qwen2.5-coder:7b")


# RunModel()


def run_model():
    diff = get_git_diff("main", "feat/git-proof")
    chat_ollama(diff, "Are there repeated functions? How many?", "qwen2.5-coder:7b")


if __name__ == "__main__":
    run_model()
