import cv2
import requests
from PIL import Image
from matplotlib.pyplot import imshow, figure, subplot, show


def crop(img, x, y, ancho, alto):
    image = cv2.imread(f"static/processing/{img}")
    crop_image = image[y:y+alto, x:x+ancho]
    cv2.imwrite(f"static/processing/{img}", crop_image)
    return 0


def scale(img, porcentajeEscala):
    image = cv2.imread(f"static/processing/{img}")
    if porcentajeEscala < 100:
        scale_image = cv2.resize(
            image, None, fx=porcentajeEscala/100, fy=porcentajeEscala/100)
    else:
        scale_image = cv2.resize(
            image, None, fx=porcentajeEscala/100, fy=porcentajeEscala/100, interpolation=cv2.INTER_AREA)
    cv2.imwrite(f"static/processing/{img}", scale_image)
    return 0


def objectDetector(img):
    URL = 'http://localhost:32168/v1/vision/detection'

    print(img)
    image_data = open(f"static/processing/{img}", "rb").read()
    response = requests.post(URL, files={"image": image_data}).json()
    print(response['message'])
    return 0
