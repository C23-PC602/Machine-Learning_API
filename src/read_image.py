from io import BytesIO
from PIL import Image


async def read_image(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image
