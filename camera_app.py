import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

uploaded_image = st.file_uploader("Upload Image")

with st.expander('Start camera'):
    #Start camera
    camera_image = st.camera_input("Camera")


if camera_image:
    #Create a pillow image
    img = Image.open(camera_image)
