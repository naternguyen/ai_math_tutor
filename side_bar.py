import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from hugchat import hugchat

def create_side_bar():
    with st.sidebar:
        st.title('🤗💬 MATH TUTOR')
        st.markdown('''
        ## About
        This app is an AI Math Tutor built using:
        - [Streamlit](<https://streamlit.io/>)
        - [HugChat](<https://github.com/Soulter/hugging-chat-api>)
    
        💡 Note: No API key required!
        ''')
        add_vertical_space(5)
        st.write('Made with ❤️ by [Chubby Nate](<https://www.linkedin.com/in/nate-nguyen/>)')