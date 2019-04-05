import numpy as np
import cv2 as cv
face_cascade = cv.CascadeClassifier("/Users/RuneNisbeth/Documents/6semester/Fagprojekt/PiPyOpenCV/haar/haarcascade_frontalface_default.xml")

a = 101
b = -60
while a <= 180 :
    c = -90
    while c < 91 : 
#        /Users/RuneNisbeth/Documents/6semester/Fagprojekt/PiPyOpenCV/HeadPoseImageDatabase/Person01/
        imageFileName = ("/Users/RuneNisbeth/Documents/6semester/Fagprojekt/PiPyOpenCV/HeadPoseImageDatabase/Person01/person01%d%+d%+d.jpg" %(a,b,c))
#        print(imageFileName)
        img = cv.imread(imageFileName)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
        imageOutputName = ("/Users/RuneNisbeth/Documents/6semester/Fagprojekt/PiPyOpenCV/HaarClassifiedV1/person01person01%d%+d%+d.jpg" %(a,b,c))
        cv.imwrite(imageOutputName, img )

        c += 15
        a += 1
    if b == 90 : b = -90
    if b == -90 or b == -60 or b == 30 or b == 60 : b += 30
    else : b += 15



