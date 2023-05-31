from fastapi import FastAPI, File, UploadFile, Response

from application.prediction.serve_model import predict, read_image

app: FastAPI = FastAPI(title='API Model Coffee Detection',
                       description='This is API for Machine Learning',
                       version='0.0.1'
                       )


@app.post('/api/predict')
async def predict_image(file: UploadFile, response: Response):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Format gambar tidak sesuai"
    try:
        content = file.file.read()
        prediction = predict(await read_image(content))
        return {
            "result": str(prediction)
        }
    except Exception as error:
        response.status_code = 500
        return {
            "message": str(error)
        }
