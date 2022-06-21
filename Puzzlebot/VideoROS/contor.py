import numpy as np
import cv2
import matplotlib.pyplot as plt



img = cv2.imread('circleBInary.png')

def contorno(img):
    #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #threshold,thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    contornos1,hierarchy1 = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #contornos2,hierarchy2 = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    transform=cv2.drawContours(img, contornos1, -1, (255,0,0), 3)
    #print ('len(contornos1[2])=',len(contornos1[2]))
    #print ('len(contornos2[2])=',len(contornos2[2]))
    return transform

contorno(img)
