import typing

from .api_utils import METADATA_URL
from .Client import Client

class ImageAPI:

    @staticmethod
    def get_image(image_id: str, fields: list) -> str:

        return f"{METADATA_URL}/{image_id}/?fields={','.join(fields)}"