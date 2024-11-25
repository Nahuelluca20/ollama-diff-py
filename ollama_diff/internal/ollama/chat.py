import ollama


def chat_ollama(diff, question, model_name, llm_context):
    context = f"Based in this git diff info: {diff}"
    prompt_for_ollama = context + f" Provide a response to: {question}"
    generation_response = ollama.generate(
        model=model_name, prompt=prompt_for_ollama, context=llm_context
    )
    context = generation_response["context"]
    response_text = generation_response["response"].strip()

    return response_text, context
