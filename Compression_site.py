import numpy as np
import cv2
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image

def compress_img(color_img,k):
    B, G, R = cv2.split(color_img)
    U_R, S_R, Vt_R = np.linalg.svd(R, full_matrices=False)
    U_G, S_G, Vt_G = np.linalg.svd(G, full_matrices=False)
    U_B, S_B, Vt_B = np.linalg.svd(B, full_matrices=False)

    n = k
    R_compressed = np.matrix(U_R[:, :n]) * np.diag(S_R[:n]) * np.matrix(Vt_R[:n, :])
    G_compressed = np.matrix(U_G[:, :n]) * np.diag(S_G[:n]) * np.matrix(Vt_G[:n, :])
    B_compressed = np.matrix(U_B[:, :n]) * np.diag(S_B[:n]) * np.matrix(Vt_B[:n, :])

    
    compressed_image = cv2.merge([np.clip(R_compressed, 1, 255), np.clip(G_compressed, 1, 255), np.clip(B_compressed, 1, 255)])
    compressed_image = compressed_image.astype(np.uint8)
    compressed_image2 = cv2.cvtColor(compressed_image, cv2.COLOR_BGR2RGB)
    return compressed_image2


st.title("Image Compression")
st.subheader("Upload your image and pick a number using the slider")

uploaded_file = st.file_uploader("Upload Image:")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()

    # Show the image filename and image.
    st.write(f'filename: {uploaded_file.name}')
    st.image(bytes_data)

    original_image = Image.open(uploaded_file)
    original_image = np.array(original_image)


    compress_rate = st.slider("Compression Parameter", min_value=0, max_value=original_image.shape[0])

    compressed_img = compress_img(original_image,compress_rate)

    st.image(compressed_img)
    

