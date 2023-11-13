import cv2
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
