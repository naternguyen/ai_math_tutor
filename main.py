import streamlit as st
from streamlit_chat import message
from utils import get_initial_message, get_chatgpt_response, update_chat
import openai

openai.api_key = "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"

st.title("AI MATH TUTOR: Improve your knowledge")
# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# st.subheader("AI Math Tutor:")
# model = st.selectbox(
#     "Select a model",
#     ("gpt-3.5-turbo", "gpt-4")
# )
model = "gpt-3.5-turbo"
# User information

user_infor = st.container()
user_id = user_infor.text_input("UserID: ", key="your name")
user_age = user_infor.text_input("Age: ", key="your age")
st.markdown(
    """
<style>
    div[data-testid="stVerticalBlock"] div[style*="flex-direction: column;"] div[data-testid="stVerticalBlock"] {
        border: 1px solid red;
        padding: 5% 5% 5% 10%;
    }
</style>
""",
    unsafe_allow_html=True,
)
st.write("Model: gpt-3.5-turbo")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []


query = st.text_input("Your message: ", key="input")

if 'messages' not in st.session_state:
    st.session_state['messages'] = get_initial_message()
    # first_message = "Hi, I am your Math Tutor, which topics do you want to learn today?"
    # st.session_state.generated.append(first_message)
    first_message = message("Hi, I am your Math Tutor, which topics do you want to learn today?")

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
        message(st.session_state['past'][i+1], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))
    with st.expander("Show Messages"):
        st.write(messages)