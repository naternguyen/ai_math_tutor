import streamlit as st
from streamlit_chat import message
from pgconnect import init_connection, run_query
from message_func import get_initial_message, get_chatgpt_response, update_chat
import openai
from side_bar import create_side_bar
import pandas as pd
from utils import upload_img
from purposes import add_solve_problem

openai.api_key = "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"
st.title("AI MATH TUTOR: Improve your knowledge")
create_side_bar()

#pgconnect
conn = init_connection()
rows = run_query("SELECT * from mytable")
data=pd.DataFrame(rows)
data.columns=['name','pet']
# st.table(data)

model = "gpt-3.5-turbo"
st.write("Model: gpt-3.5-turbo")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

# first_message = message()
with st.form(key="sub_select"):
# SelectBox
# User information
    user_infor = st.container()
    user_id = user_infor.text_input("UserID: ", key="your name")
    user_age = user_infor.text_input("Age: ", key="your age")
    user_learning_style = user_infor.text_input("Learning-style", key="your learning style")
    subject_options = ["<select>", "Algebra", "Geometry", "Trigonometry", "Calculus", "Statistics and Probability", "Applied Mathematics"]
    subject_selection_ = st.selectbox(label="Hi, I am your Math Tutor, which topics do you want to learn today?",
                          options=subject_options)
    purpose_options = ["<select>", "Solve math problem", "Learn theoretical", "Show example"]
    purpose_selection_ = st.selectbox(label="Hi, I am your Math Tutor, which topics do you want to learn today?",
                          options=purpose_options)
    submit_chosen_sub = st.form_submit_button(label="Submit")

# Upload image
upload_img()

# Chatbot Message Manager
if 'messages' not in st.session_state:
    if submit_chosen_sub == True:
        st.session_state['messages'] = get_initial_message(subject_selection_, user_id, user_age)
        first_response = get_chatgpt_response(st.session_state['messages'], model)
        print(first_response)
        message(first_response)
    # Create First message

query = st.text_input("Your message: ", key="input")

if query:
    if purpose_selection_ == "<select>":
        with st.spinner("generating..."):
            messages = st.session_state['messages']
            messages = update_chat(messages, "user", query)
            response = get_chatgpt_response(messages, model)
            messages = update_chat(messages, "assistant", response)
            st.session_state.past.append(query)
            st.session_state.generated.append(response)
    elif purpose_selection_ == "Solve math problem":
        with st.spinner("generating..."):
            messages = st.session_state['messages']
            # messages = messages.append(add_solve_problem())
            messages = update_chat(messages, "user", query)
            response = get_chatgpt_response(messages, model)
            messages = update_chat(messages, "assistant", response)
            st.session_state.past.append(query)
            st.session_state.generated.append(response)
    elif purpose_selection_ == "Learn theoretical":
        with st.spinner("generating..."):
            messages = st.session_state['messages']
            messages = update_chat(messages, "user", query)
            response = get_chatgpt_response(messages, model)
            messages = update_chat(messages, "assistant", response)
            st.session_state.past.append(query)
            st.session_state.generated.append(response)
    elif purpose_selection_ == "Show example":
        with st.spinner("generating..."):
            messages = st.session_state['messages']
            messages = update_chat(messages, "user", query)
            response = get_chatgpt_response(messages, model)
            messages = update_chat(messages, "assistant", response)
            st.session_state.past.append(query)
            st.session_state.generated.append(response)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))
    # with st.expander("Show Messages"):
    #     st.write(messages)