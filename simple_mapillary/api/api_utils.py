from .Client import Client
from . import __token__

METADATA_URL = "https://graph.mapillary.com"


def init_client(access_token: str):
    if Client.initialised:
        return

    if type(access_token) != str or type(__token__.token) != str:
        raise Exception("\n\nThe access token must be a string.\n")

    if len(access_token) == 0:
        if len(__token__.token) == 0:
            raise Exception("\n\nNo access token was provided. Please pass a token to the set_access_token"
                            " function or set the token in the __token__.py file. Check the README for more"
                            " information.\n")
        else:
            access_token = __token__.token

    Client.init_static(access_token)
