from simple_mapillary import Image,Client

# TODO: You can either set the token here or in the __token__.py file
# token = ""
# simple_mapillary.set_access_token(token)

image_id = "1933525276802129"
image = Image(image_id)

print(image.image_data.id)


