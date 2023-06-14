import openai
def get_initial_message():
    messages=[
            {"role": "system", "content": "You are a helpful AI Math Tutor. "},
            {"role": "user", "content": "I want to learn Math"},
            {"role": "assistant", "content": "Hi, I am your Math Tutor, which topics do you want to learn today?"}
        ]
    return messages

def get_chatgpt_response(messages, model="gpt-3.5-turbo"):
    print("model: ", model)
    response = openai.ChatCompletion.create(
    model=model,
    messages=messages
    )
    return  response['choices'][0]['message']['content']

def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages