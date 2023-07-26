import streamlit as st
from security_utils import check_password

if check_password():
    st.title('IdeaSpark DALL-E Image Editing')
    st.info(""" NOTE: You can download image by\
    right clicking on the image and select save image as option""")   