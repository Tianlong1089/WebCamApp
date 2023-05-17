import streamlit as st
from PIL import Image

with st.expander('Start camera'):
    #Start camera
    camera_image = st.camera_input("Camera")


if camera_image:
    #Create a pillow image
    img = Image.open(camera_image)

    #Convert pillow image
    gray_img = img.convert("L")
    st.image(gray_img)