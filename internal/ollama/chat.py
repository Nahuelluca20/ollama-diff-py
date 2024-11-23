from ollama import ChatResponse, chat


def chat_ollama(diff, question, model_name):
    messages = [
        {
            "role": "system",
            "content": f"Analyze the following git diff and summarize the differences between the branches. Git diff content:\n{diff}",
        },
        {"role": "user", "content": question},
    ]

    response: ChatResponse = chat(model=model_name, messages=messages)

    print(response)
    print(response["message"]["content"])
