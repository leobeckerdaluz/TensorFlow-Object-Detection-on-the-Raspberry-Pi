import cv2
import numpy as np

# filepath = '/home/pi/grazi.png'
captura = cv2.VideoCapture(0)
 
ret, frame = captura.read()
# cv2.imshow("Video", frame)
 
captura.release()
# cv2.destroyAllWindows()

# image = cv2.imread('grazi.png')
# image = cv2.imread(filepath, 0)
# print("abriu a imagem e converteu pra cinza!!")
 
# cv2.imshow('image', img)

cv2.imwrite('grazi_feito_aeee.png', frame)
# cv2.imwrite('grazi_feito_aeee.png', image)
# cv2.imwrite('grazi_feito_aeee.png', image_gray)

print("salvou frame!")