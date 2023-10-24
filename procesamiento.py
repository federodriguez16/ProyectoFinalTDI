import cv2

camera = cv2.VideoCapture(0)

ret, image = camera.read()
cv2.imwrite("captura0.png", image)
del (camera)
option = 0

height, width, rgb = image.shape
print(image.shape)
w = 200
h = 200
match(option):
    case 1:
        if w >= width & h >= height:
            y = 0
            x = 0
            crop_image = image[x:h, y:w]
        elif w >= width:
            y = 0
            x = int((height/2)-(h/2))
            crop_image = image[x:x+h, 0:w]
        elif h >= height:
            y = int((width/2)-(w/2))
            x = 0
            crop_image = image[0:h, y:y+w]
        else:
            y = int((width/2)-(w/2))
            x = int((height/2)-(h/2))
            crop_image = image[x:x+h, y:y+w]
    case 2:
        y = 0
        x = height
        crop_image = image[(height-h):x, y:w]
    case 3:
        y = width
        x = 0
        crop_image = image[x:h, (width-w):y]
    case 4:
        y = width
        x = height
        crop_image = image[(height-h):x, (width-w):y]
    case _:
        y = 0
        x = 0
        crop_image = image[x:h, y:w]


cv2.imwrite('captura1.png', crop_image)
