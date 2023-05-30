import numpy as np
from fastapi import FastAPI, File, UploadFile
from application.prediction.serve_model import predict, read_image
import tensorflow as tf

app: FastAPI = FastAPI()


@app.post('/api/predict/image')
async def predict_image(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Format gambar tidak sesuai"
    prediction = predict(read_image(file))
    try:
        print("predictions")
        return {
            "result": prediction,
        }
    except:
        print("error")

