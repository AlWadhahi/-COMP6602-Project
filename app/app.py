import streamlit as st 
from PIL import Image
from classify import predict

st.title("COMP6602 Project Demo")

st.markdown("""This is a demo of COMP6602 Project, 
the purpose of this project is to build a classifier that
is able to classify car images into two labels:

- Damage: For cars that were damaged in accident as an example
- Non-damage: For cars that are clean and without visible damage

#### [Checkout the code in the repo here](https://github.com/AlWadhahi/COMP6602-Project)

and feel free to try out the project by uploading an image of a car 👇""")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg"])


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.header("Results")
    with st.spinner('Classifying...'):
        label = predict(uploaded_file)
    
    st.write(label)