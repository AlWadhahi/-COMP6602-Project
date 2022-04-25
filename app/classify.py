import pickle
import streamlit as st
import numpy as np
from PIL import Image

model = pickle.load(open('saved-models/final_model.p','rb'))
pca = pickle.load(open('saved-models/pca.pkl','rb'))

def process_image(img):
    
    w = 256
    h = 256
    channels = 3

    X = np.empty(shape= (1, w*h*channels))

    image_vector = Image.open(img) 
    
    # Resize to 256 x 256
    resized_image_vector = np.array(image_vector.resize((256, 256)))

    # Scale to [0,1]
    norm_image_vector = resized_image_vector / 255

    flattened_image_vector = norm_image_vector.flatten()

    X[0] = np.pad(flattened_image_vector, (0, (w*h*channels) - len(flattened_image_vector) ))

    X=pca.transform(X)

    return X

def predict(uploaded_image):

    processed_image = process_image(uploaded_image)

    # Class 0: Damage   
    if model.predict(processed_image.reshape(1, -1))[0] == 0:
        return "Damage"

    # Class 1: Non-damage
    else:
        return "Non-Damage"