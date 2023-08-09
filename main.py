from simple_mapillary import Image, set_access_token
from simple_mapillary.image import draw_detections
import cv2

# TODO: Set the token here
token = ''
set_access_token(token)

image_id = "279996174671586"
image = Image(image_id)

img = image.get_cvimage()

detections = image.get_detections()
segmentation_img = draw_detections(img, detections)

comb_img = cv2.addWeighted(img, 0.6, segmentation_img, 0.4, 0)

cv2.imshow('image', comb_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('doc/img/semantic_img.png', comb_img)