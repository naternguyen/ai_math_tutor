import openai
def get_initial_message(selection, name, age):
    messages=[
            {"role": "system", "content": "You are a helpful AI Math Tutor. "
                                          f"User name is {name} and user age is {age}."
                                          f"You will be a tutor for {name} and you just only focus on the Math "
                                          f"knowledge for {age}-age person."
                                          f"After {name} choose the subject, you will provide a list of related topics "
                                          f"for {name} to choose."
             },
            {"role": "user", "content": "I want to learn Math"},
            {"role": "assistant", "content": "Hi, I am your Math Tutor, which subject do you want to learn today?"},
            {"role": "user", "content": f"I want to learn {selection}"},
        ]
    print(messages[0])
    return messages

def get_chatgpt_response(messages, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    return response['choices'][0]['message']['content']

def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages

