from simple_mapillary import Image
import cv2

# TODO: You can either set the token here or in the __token__.py file
# token = ""
# simple_mapillary.set_access_token(token)

image_id = "1200479493800436"
image = Image(image_id)

img = image.get_cvimage()

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
