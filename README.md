# simple-mapillary-python-sdk
 Simplified Python library for accessing the Mapillary API.

## Installation
```bash
pip install simple-mapillary
```

Or clone the repository and install it manually:
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

Then, you can either modify the [__token__py file](https://github.com/ibaiGorordo/simple-mapillary-python-sdk/blob/main/simple_mapillary/__token__.py) 
with your token or pass it as an argument to the `simple_mapillary.set_access_token()` function.

## Example (Read image)
```python
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
```

![! Mapillary image example](https://github.com/ibaiGorordo/simple-mapillary-python-sdk/blob/main/doc/img/retrieve_img.png)