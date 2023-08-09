# simple-mapillary-python-sdk [![PyPI](https://img.shields.io/pypi/v/simple_mapillary?color=2BAF2B)](https://pypi.org/project/simple_mapillary/)
 Simplified Python library for accessing the Mapillary API. 
 For a more complete library, check out the official [mapillary-python-sdk](https://github.com/mapillary/mapillary-python-sdk).

## Installation
```bash
pip install simple-mapillary
```

Or clone the repository and install it manually (If you want to modify the code):
```bash
git clone https://github.com/ibaiGorordo/simple-mapillary-python-sdk
cd simple-mapillary-python-sdk
pip install .
```

## Setup
First, you need to get an access token. To get one:
- Visit https://www.mapillary.com/dashboard/developer, go to 'developers',
- Then, click 'register application', register a new application (read access is enough),
- Finally, copy the 'Client Token'

Then, pass the token as an argument to the `set_access_token()` function.

## Example (Read image)
```python
from simple_mapillary import Image, set_access_token
import cv2

token = ""
set_access_token(token)

image_id = "1200479493800436"
image = Image(image_id)

img = image.get_cvimage()

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

<p align="center">
  <img src="https://raw.githubusercontent.com/ibaiGorordo/simple-mapillary-python-sdk/main/doc/img/retrieve_img.png" />
</p>

## Example (Read image with semantic map)
```python
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
```
<p align="center">
  <img src="https://raw.githubusercontent.com/ibaiGorordo/simple-mapillary-python-sdk/main/doc/img/semantic_img.png" />
</p>
