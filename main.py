
from simple_mapillary import Image, set_access_token
import cv2

# TODO: Set the token here
token = ""
set_access_token(token)

image_id = "1200479493800436"
image = Image(image_id)

img = image.get_cvimage()

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
