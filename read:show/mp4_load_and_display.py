import cv2

# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture("/Users/RuneNisbeth/Documents/6semester/Fagprojekt/PiPyOpenCV/read:show/Paper.mp4")

while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    cv2.imshow('Frame',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
  else: 
    break
 
cap.release()
cv2.destroyAllWindows()
