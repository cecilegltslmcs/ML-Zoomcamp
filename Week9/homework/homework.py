import tflite_runtime.interpreter as tflite

<<<<<<< HEAD
import os
=======
>>>>>>> 918ca45 (homework week9)
import numpy as np

from io import BytesIO
from urllib import request

from PIL import Image

<<<<<<< HEAD
MODEL_NAME = os.getenv('MODEL_NAME', 'bees-wasps-v2.tflite')
input_size = (150,150)
=======
input_size = (150, 150)
>>>>>>> 918ca45 (homework week9)

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img


def prepare_input(x):
    return x / 255.0


<<<<<<< HEAD
interpreter = tflite.Interpreter(model_path=MODEL_NAME)


=======
>>>>>>> 918ca45 (homework week9)
interpreter = tflite.Interpreter(model_path="bees-wasps-v2.tflite")
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]["index"]
output_index = interpreter.get_output_details()[0]["index"]

def predict(url):
    image = download_image(url)
    img = prepare_image(image, input_size)
    x = np.array(img, dtype='float32')
    X = np.array([x])
    X = prepare_input(X)
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()

    preds = interpreter.get_tensor(output_index)

    return float(preds[0, 0])

def lambda_handler(event, context):
    url = event["url"]
    pred = predict(url)
    result = {
        "prediction": pred
    }
    
<<<<<<< HEAD
    return result
=======
    return result
>>>>>>> 918ca45 (homework week9)
