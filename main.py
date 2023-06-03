from fastapi import FastAPI, UploadFile, Response
from src.prediction import predict
from src.read_image import read_image
import uvicorn
import sys

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
async def predict_image(file: UploadFile, response: Response):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        response.status_code = 400
        return {"message": "Format gambar tidak sesuai"}
    try:
        content = file.file.read()
        image = await read_image(content)
        prediction = predict(image)
        return prediction

    except Exception as error:
        response.status_code = 500
        return {"message": str(error)}

PORT = int(sys.argv[1])
HOST = "0.0.0.0"
uvicorn.run(app, host=HOST, port=PORT)
print(f"listening {HOST}:{PORT} ...")
