from imread_from_url import imread_from_url

from .ImageAPI import ImageAPI
from .ImageData import ImageData

class Image():

    def __init__(self, image_id: int):
        self.image_id = image_id
        self.raw_data = eval(ImageAPI.image_from_key(image_id, fields=ImageData.fields()))['features']
