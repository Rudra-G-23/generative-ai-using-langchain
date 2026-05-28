from transformers import pipeline

hf_pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-small",
)

chat_history = []

while True:
    user_input = input("<|YOU|> ").strip()
    chat_history.append(user_input)

    if user_input.lower() in {"exist", "stop"}:
        print("Existing chatbot...")
        break

    response = hf_pipe(user_input, max_new_tokens=20)
    response = response[0]["generated_text"]
    chat_history.append(response)
    print(f"<|ASST|> {response}\n")

print(chat_history)
