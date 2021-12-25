import cv2
import numpy as np
import imutils
import os


Datos = '/home/carlos/Programing/ProyectoIA/data/Señales/SeñaleSocorroGenero/Fotos/'  #Cambiar al directorio necesario
if not os.path.exists(Datos):
    print('dir created:', Datos)
    os.makedirs(Datos)

capture = cv2.VideoCapture(0)
x1 , y1 = 100, 80
x2 , y2 = 300, 300

count = 3

while True:
    
    ret, frame = capture.read()
    if ret == False: break
    imgAux = frame.copy()
    cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)
#Es el objeto que se va a capturar
    objeto = imgAux[y1:y2,x1:x2]
    objeto = imutils.resize(objeto, width=40)

    k = cv2.waitKey(1)
    if k == 27:
        break
    if k == ord('s'):
        cv2.imwrite(Datos +'/SeñaleSocorroGenero_{}.jpg'.format(count),objeto)
        print('picture saved:','SeñaleSocorroGenero_{}.jpg'.format(count))
        count = count + 1

    cv2.imshow ('frame', frame)
    cv2.imshow ('objeto', objeto)

    capture.release()
    cv2.destroyAllWindows()

    



