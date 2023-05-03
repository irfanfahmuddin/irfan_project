from flask import Flask, request, jsonify
import pandas as pd 
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import cv2
app = Flask(__name__)

names = ["Cartoon", "Anime"]

# Process image and predict label
def processimg(IMG_PATH):
    # Read image
    model = load_model("bestmodel_jumat.hdf5")
    
    # Preprocess image
    image = cv2.imread(IMG_PATH)
    image = cv2.resize(image, (250, 250))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    res = model.predict(image)
    label = np.argmax(res)
    print("Label", label)
    labelName = names[label]
    print("Label name:", labelName)
    return labelName


@app.route("/")
def welcome():
    return "<h3>WELCOME</h3>"

@app.route("/predict", methods=["POST"])

def upl_img():
    data = request.files["img"]
    data.save("img.jpg")

    primg = processImg("img.jpg")


    return primg