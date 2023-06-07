import argparse
import os

import uvicorn
from fastapi import FastAPI, UploadFile, Response
from src.prediction import predict_images
from src.read_image import read_image

__title__ = "API Model Coffee Detection"
__description__ = "This is API for Machine Learning"
__version__ = "0.0.1"


app: FastAPI = FastAPI(
    title=__title__, description=__description__, version=__version__
)


@app.get("/")
async def index():
    return {
        "message": "Detection Coffee Machine Learning API",
    }


@app.post("/api/predict")
async def predict(file: UploadFile, response: Response):
    extension = file.filename.split(".")[-1] in ("jpg", "JPG", "jpeg", "png")
    if not extension:
        response.status_code = 400
        return {"message": "Format gambar tidak sesuai"}
    try:
        content = file.file.read()
        image = await read_image(content)
        prediction = predict_images(image)
        return prediction

    except Exception as error:
        response.status_code = 500
        return {"message": str(error)}

__port__ = os.getenv("PORT", default=8001)
print(f"THIS IS PORT {__port__}")

uvicorn.run(app, host="0.0.0.0", port=8001)
