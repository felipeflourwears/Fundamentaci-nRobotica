import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('puzzlebot_record.avi')
#############################Constantes#######################3
medianFilter = np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]],dtype=np.uint8)

###############################################################
frames = []
def createImageMask(image,lowerBound,upperBound):
    return  cv2.inRange(image, lowerBound, upperBound)

while(cap.isOpened()):
  ret, frame = cap.read()
  scale = 40
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  width = int(gray.shape[0]*scale/100)
  height = int(gray.shape[1]*scale/100)
  gray = cv2.resize(gray,(height,width))
  gray = cv2.rotate(gray,cv2.ROTATE_180)
  gray =cv2.GaussianBlur(gray,(11,11),0)    
  #ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
  ret, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
  print(type(binary))

  erotion = cv2.erode(src=binary,kernel=medianFilter ,iterations=1)
  dilation = cv2.dilate(src=binary,kernel=medianFilter ,iterations=1)
  binarized = createImageMask(binary,0,ret)
  
  print(type(binary))
  
  cv2.imshow('frame',binarized)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()

