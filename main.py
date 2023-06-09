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
    extension = ["image/jpeg", "image/png", "image/jpg"]
    if file.content_type not in extension:
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

port = os.environ.get("PORT", 8080)
print(f"Listening to http://0.0.0.0:{port}")
uvicorn.run(app, host='0.0.0.0', port=port)
