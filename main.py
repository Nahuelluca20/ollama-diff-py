from internal.git import git_diff
from internal.ollama import chat

# qwen2.5-coder:7b


def RunModel():
    diff = git_diff("main", "feat/git-proof")
    chat(diff, "What is the difference between these branches", "qwen2.5-coder:7b")


RunModel()
