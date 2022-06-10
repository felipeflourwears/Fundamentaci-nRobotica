from pickle import FRAME
import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('puzzlebot1.avi')
#############################Constantes#######################3
medianFilter = np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]],dtype=np.uint8)

###############################################################
frames = []
erotionIters=5
dilationIters=5
kernelC = np.ones((5,5), np.uint8)

def extractRedPixels(img):
    upperRed = np.array([15,255,255])
    lowerRed = np.array([0,88,88])
    upperRed2 = np.array([180,255,255])
    lowerRed2 = np.array([170,88,88])
    hsv = cv2.cvtColor(img.copy(),cv2.COLOR_BGR2HSV)
    filtered = cv2.inRange(hsv,lowerb=lowerRed,upperb=upperRed)
    filtered2 = cv2.inRange(hsv,lowerb=lowerRed2,upperb=upperRed2)
    masked = cv2.bitwise_and(img,img,mask=filtered+filtered2)
    return masked
def extractGreenPixels(img):
    upperRed = np.array([65,255,255])
    lowerRed = np.array([45,180,88])        
    hsv = cv2.cvtColor(img.copy(),cv2.COLOR_BGR2HSV)
    filtered = cv2.inRange(hsv,lowerb=lowerRed,upperb=upperRed)
    masked = cv2.bitwise_and(img,img,mask=filtered)
    return masked

#####################################################################################3
######SE UTILIZA####################
def extractRED(img):
    upperRed = np.array([15,255,255])
    lowerRed = np.array([0,88,88])
    upperRed2 = np.array([180,255,255])
    lowerRed2 = np.array([170,88,88])

    hsv = cv2.cvtColor(img.copy(),cv2.COLOR_BGR2HSV)
    filtered = cv2.inRange(hsv,lowerRed,upperRed)
    filtered2 = cv2.inRange(hsv,lowerRed2,upperRed2)
    maskRed=cv2.add(filtered,filtered2)
    masked = cv2.bitwise_and(img,img,mask=maskRed)
    return masked

######SE UTILIZA####################
def extractGREEN(img):
    upperRed = np.array([65,255,255])
    lowerRed = np.array([45,180,88])
    hsv = cv2.cvtColor(img.copy(),cv2.COLOR_BGR2HSV)
    filtered = cv2.inRange(hsv,lowerRed,upperRed)
    masked = cv2.bitwise_and(img,img,mask=filtered)
    return masked

def preprocessImage(img):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = cv2.rotate(img,cv2.ROTATE_180)
    #img =  img[:205,:,:]
    img =cv2.GaussianBlur(img,(7,7),0) 
    return img

def binarizeImage(masked,erotionIters=5,dilationIters = 5):
    gray = cv2.cvtColor(masked,cv2.COLOR_BGR2GRAY)
    threshold,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    erotion = cv2.erode(src=thresh,kernel=kernelC ,iterations=erotionIters)
    dilation = cv2.dilate(src=erotion,kernel=kernelC ,iterations=dilationIters)
    return dilation

def contorno(img):
    #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #threshold,thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    contornos1,hierarchy1 = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #contornos2,hierarchy2 = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    transform=cv2.drawContours(img, contornos1, -1, (255,0,0), 3)
    #print ('len(contornos1[2])=',len(contornos1[2]))
    #print ('len(contornos2[2])=',len(contornos2[2]))
    return transform

######SE UTILIZA####################
def circleRed(img):
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    gray_blurred = cv2.blur(gray,(3, 3)) 
    detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 1, maxRadius = 40) 
    found=False
    if detected_circles is not None:
        found=True 
        detected_circles = np.uint16(np.around(detected_circles)) 
        for pt in detected_circles[0, :]: 
            a, b, r = pt[0], pt[1], pt[2]
            #(B,G,R)
            #Contorno
            cv2.circle(imgRGB,(a, b), r,(0, 0, 255), 2) 
            #Circle de enmedio
            cv2.circle(imgRGB,(a, b), 1,(255, 0, 0), 3)
    return imgRGB

######SE UTILIZA####################
def circleGreen(img):
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    gray_blurred = cv2.blur(gray,(3, 3)) 
    detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 1, maxRadius = 40) 
    found=False
    if detected_circles is not None:
        found=True 
        detected_circles = np.uint16(np.around(detected_circles)) 
        for pt in detected_circles[0, :]: 
            a, b, r = pt[0], pt[1], pt[2] 
            cv2.circle(imgRGB,(a, b), r,(0, 255, 0), 2) 
            cv2.circle(imgRGB,(a, b), 1,(255, 0, 0), 3)
    return imgRGB

def extractBlobs(img, color):
    found = False
    params = cv2.SimpleBlobDetector_Params()
    params.filterByCircularity = True
    params.minCircularity = 0.6
    params.filterByArea = True
    params.minArea = 50
    params.maxArea = 5000
        
    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(img)
    m = np.zeros(img.shape,dtype = np.uint8)
    black = cv2.merge([m,m,m])
    blobs = cv2.drawKeypoints(black,keypoints,np.array([]),color,cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    found = False if len(keypoints)  == 0 else True
    return found, blobs


while(cap.isOpened()):
  ret, frame = cap.read()
  #red_pixel_image = extractRedPixels(dilation)
  preprocessed_image = preprocessImage(frame)
  red_pixel_image = extractRedPixels(preprocessed_image)
  red_pixel_binarized_image = binarizeImage(red_pixel_image,dilationIters=1,erotionIters=1)
  green_pixel_image = extractGreenPixels(preprocessed_image)
  green_pixel_binarized_image = binarizeImage(green_pixel_image,dilationIters=1,erotionIters=1)
  newImageRed=contorno(red_pixel_binarized_image)
  newImageGreen=contorno(green_pixel_binarized_image)
  found,blopRed=extractBlobs(newImageRed,(0, 0, 255))
  found,blopGreen=extractBlobs(newImageGreen,(0, 255, 0))
  
  #prueba=contourRed(preprocessed_image)
  prueba=extractRED(frame)
  prueba2=circleRed(prueba)
  prueba3=extractGREEN(frame)
  prueba4=circleGreen(prueba3)

  filtered_image= prueba2 | prueba4
  #filtered_image=prueba2
  #cv2.imshow('frame',red_pixel_image)

  cv2.imshow('frame', filtered_image)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()

