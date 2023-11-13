import cv2
from PIL import Image
import requests
from matplotlib.pyplot import imshow, figure, subplot, show


def crop(img, x, y, ancho, alto):
    image = cv2.imread(f"static/uploads/{img}")
    crop_image = image[y:y+alto, x:x+ancho]
    cv2.imwrite(f"static/downloads/{img}", crop_image)
    return 0


def scale(img, porcentajeEscala):
    scale_image = cv2.resize(
        f"static/uploads/{img}", None, fx=porcentajeEscala/100, fy=porcentajeEscala/100)
    cv2.imwrite(f"downloads/{img}", scale_image)
    return 0
