from imread_from_url import imread_from_url

from .ImageAPI import ImageAPI
from .ImageData import ImageData


class Image():
    image_data: ImageData

    def __init__(self, image_id: str):
        raw_data = ImageAPI.get_image(image_id, fields=ImageData.fields())
        self.image_data = ImageData(raw_data)
