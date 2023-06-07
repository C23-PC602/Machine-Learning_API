import numpy as np
from tensorflow.python.keras.models import load_model
from keras_preprocessing.image import img_to_array
from PIL import Image


def predict_images(image: Image.Image):
    model = load_model("model_DCoffee_Classification.h5", compile=False)

    image_to_array = img_to_array(image.resize((224, 224)))
    print(image_to_array.shape)
    image_preprocess = np.expand_dims(image_to_array, 0)
    image_preprocess /= 255.0
    print(f"Byte index 0 : {image_preprocess[-1, 0, 0]}")

    prediction: list = list(model.predict(image_preprocess, 10)[0])

    print(f"result prediction : {prediction}")
    max_index = prediction.index(max(prediction))

    label = ["Matang", "Mentah", "Setengah Matang"]
    result = label[max_index]

    print(f"Result :  {result}")

    return {"result": result}
