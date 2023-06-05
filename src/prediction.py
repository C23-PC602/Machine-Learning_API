
import numpy as np
from tensorflow.python.keras.models import load_model
from PIL import Image


def predict(image: Image.Image):
    model = load_model('model_DCoffee_Classification.h5', compile=False)

    image = np.asarray( image.resize((224,224)) )[..., :3]
    image = np.expand_dims(image, 0)
    print(f"IMAGE SHAPE : {image.shape}")

    image = image / 127.5 - 1.0

    prediction = model.predict(image)
    print(f"result prediction : {prediction[0]}")
    max_probability = max(prediction[0])
    max_index = 0

    for i, pred in enumerate(prediction[0]):
        if pred == max_probability:
            max_index = i

    max_probability = max_probability * 100

    label = ['Matang', 'Mentah', 'Setengah Matang']
    result = label[max_index]

    print("Probabilitas tertinggi: {:.0f}%".format(max_probability))
    print("Indeks probabilitas tertinggi:", max_index)
    print(f"Result :  {result}")

    return {
        "probability": max_probability,
        "result": result
    }
