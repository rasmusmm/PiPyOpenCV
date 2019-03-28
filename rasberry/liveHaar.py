import cv2
face_cascade = cv2.CascadeClassifier("/Users/RuneNisbeth/Documents/6semester/Fagprojekt/PiPyOpenCV/haar/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("/Users/RuneNisbeth/Documents/6semester/Fagprojekt/PiPyOpenCV/haar/haarcascade_eye.xml")

# If the input is the camera, pass 0 instead of the video file name
#cap = cv2.VideoCapture("/Users/RuneNisbeth/Documents/6semester/Fagprojekt/PiPyOpenCV/read:show/Paper.mp4")
cap = cv2.VideoCapture("/Users/RuneNisbeth/Desktop/face.mp4")

while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
      
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('Frame',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
  else: 
    break
 
cap.release()
cv2.destroyAllWindows()
