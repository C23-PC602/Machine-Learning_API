
from io import BytesIO
import tensorflow as tf
import numpy as np
from keras.applications.imagenet_utils import decode_predictions

from PIL import Image


def predict(image: Image.Image):
    model = tf.keras.models.load_model("application/prediction/model.h5")
    image = np.asarray(image.resize((224,224)))[..., :3]
    image = np.expand_dims(image, 0)
    print(f"IMAGE : {image.shape}")
    image = image / 127.5 - 1.0
    prediction = model.predict(image)
    print(f"result prediction : {prediction[0]}")
    max_probability = max(prediction[0])
    max_index = 0
    for i in range(len(prediction[0])):
        if prediction[0][i] == max_probability:
            max_index = i

    print("Probabilitas tertinggi:", max_probability)
    print("Indeks probabilitas tertinggi:", max_index)
    if max_index == 0:
        result = "Matang"
    elif max_index == 1:
        result = "Mentah"
    else:
        result = "Setengah Matang"
    print(f"Result :  {result}")
    return result


async def read_image(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image
