import streamlit as st

def upload_img():
    image_file = st.file_uploader("Choose an image", type=['jpg','jpeg','png'])
    if image_file is not None:
        st.write(type(image_file))

