import numpy as np
from tensorflow.python.keras.models import load_model
from keras_preprocessing import image
from PIL import Image


def predict(target: Image.Image):
    model = load_model("model_DCoffee_Classification.h5", compile=False)
    print(model)

    target = image.img_to_array(target.resize((224, 224)))
    print(target.shape)
    target = np.expand_dims(target, 0)
    target_image = np.vstack([target])
    print(f"Bit index 0 : {target_image[-1, 0, 0]}")

    prediction: list = list(model.predict(target_image, 10)[0])

    print(f"result prediction : {prediction}")
    max_index = prediction.index(max(prediction))

    label = ["Matang", "Mentah", "Setengah Matang"]
    result = label[max_index]

    print(f"Result :  {result}")

    return {"result": result}
