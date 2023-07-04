import openai
import streamlit as st
from streamlit_chat import message

def add_solve_problem(selection, name, age):
    addition_messages=[
            {"role": "assistant", "content": "What types of learning do you want to learn"},
            {"role": "user", "content": "I want to solve a math problem."},
            {"role": "assistant", "content": "Could you show me the problem you want to solve?"},
        ]
    for i in range(len(addition_messages)-1):
        if addition_messages["role"] == "assistant":
            message(addition_messages["content"])
        else:
            message(addition_messages, is_user=True)
    return addition_messages