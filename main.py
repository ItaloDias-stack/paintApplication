from cv2 import cv2 as cv
import numpy as np
from Pincel import Pincel
from Cor import Cor

desenhando = False
cor = Cor(0, 0, 0)
pincel = Pincel(0, 0, cor, 0)

def nada(x):
    pass


def desenho(event, x, y, flags, param):
    global pincel,cor,desenhando
    pincel.x = x
    pincel.y = y
    if event == cv.EVENT_LBUTTONDOWN:
        desenhando = True
    elif event == cv.EVENT_MOUSEMOVE:
        if desenhando:
            cv.circle(img, (pincel.x, pincel.y), pincel.espessura, (pincel.cor.b, pincel.cor.g, pincel.cor.r), -1)
    elif event == cv.EVENT_LBUTTONUP:
        desenhando = False
        cv.circle(img, (pincel.x, pincel.y),  pincel.espessura, (pincel.cor.b, pincel.cor.g, pincel.cor.r), -1)


if __name__ == "__main__":

    img = np.zeros((400, 612, 3), np.uint8)
    cv.namedWindow("Paint")

    # Criando as trackBars par as cores
    cv.createTrackbar("R", "Paint", 0, 255, nada)
    cv.createTrackbar("G", "Paint", 0, 255, nada)
    cv.createTrackbar("B", "Paint", 0, 255, nada)
    cv.createTrackbar("Espessura", "Paint", 10, 50, nada)
    cv.setMouseCallback('Paint', desenho)

    while True:
        cv.imshow("Paint", img)
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break
        # Pega a posição atual do trackbar
        r = cv.getTrackbarPos('R', 'Paint')
        g = cv.getTrackbarPos('G', 'Paint')
        b = cv.getTrackbarPos('B', 'Paint')
        pincel.cor.r = r
        pincel.cor.g = g
        pincel.cor.b = b

        raio = cv.getTrackbarPos("Espessura", 'Paint')
        pincel.espessura = raio
        #img[:] = [b, g, r]
    cv.destroyAllWindows()
