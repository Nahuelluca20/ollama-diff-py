from ollama import ChatResponse
import ollama


def chat_ollama(diff, question, model_name):
    messages = [
        {
            "role": "system",
            "content": f"Analyze the following git diff and summarize the differences between the branches. Git diff content:\n{diff}",
        },
        {"role": "user", "content": question},
    ]
    context = f"Based in this git diff info: {diff}"
    prompt_for_ollama = context + f" Provide a response to: {question}"
    generation_response = ollama.generate(
        model=model_name,
        prompt=prompt_for_ollama,
    )

    response_text = generation_response["response"].strip()
    print(response_text)
