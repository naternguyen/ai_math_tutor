import streamlit as st
from streamlit_chat import message
from utils import get_initial_message, get_chatgpt_response, update_chat
import openai
from side_bar import create_side_bar

openai.api_key = "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"
st.title("AI MATH TUTOR: Improve your knowledge")
create_side_bar()
# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# st.subheader("AI Math Tutor:")
# model = st.selectbox(
#     "Select a model",
#     ("gpt-3.5-turbo", "gpt-4")
# )
model = "gpt-3.5-turbo"
# User information

# st.markdown(
#     """
# <style>
#     div[data-testid="stVerticalBlock"] div[style*="flex-direction: column;"] div[data-testid="stVerticalBlock"] {
#         border: 1px solid red;
#         padding: 5% 5% 5% 10%;
#     }
# </style>
# """,
#     unsafe_allow_html=True,
# )
st.write("Model: gpt-3.5-turbo")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

# first_message = message()
with st.form(key="sub_select"):
# SelectBox
    user_infor = st.container()
    user_id = user_infor.text_input("UserID: ", key="your name")
    user_age = user_infor.text_input("Age: ", key="your age")
    subject_options = ["<select>","Algebra", "Geometry", "Trigonometry", "Calculus", "Statistics and Probability", "Applied Mathematics"]
    selection_ = st.selectbox(label="Hi, I am your Math Tutor, which topics do you want to learn today?",
                          options=subject_options)
    submit_chosen_sub = st.form_submit_button(label="Submit")

if 'messages' not in st.session_state:
    if submit_chosen_sub == True:
        st.session_state['messages'] = get_initial_message(selection_, user_id, user_age)
        first_response = get_chatgpt_response(st.session_state['messages'], model)
        print(first_response)
        message(first_response)
    # Create First message

query = st.text_input("Your message: ", key="input")
if query:
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