import simple_mapillary
from simple_mapillary import Client

token = ""
simple_mapillary.set_access_token(token)

print(Client.get("https://graph.mapillary.com/1933525276802129?fields=id"))


