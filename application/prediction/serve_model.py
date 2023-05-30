from io import BytesIO
import tensorflow as tf
import numpy as np

from PIL import Image

model = None


def load_model():
    news_model = tf.saved_model.load("model.h5")
    print(news_model)
    return news_model


def predict(image: Image.Image):
    global model
    if model is None:
        model = load_model()
    image = np.asarray(image.resize((224, 224)))[..., :3]
    image = image / 127.5 - 1.0
    result = tf.keras.applications.imagenet_utils.decode_predictions(model.predict(image), 2)[0]
    print(result)


def read_image(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image
