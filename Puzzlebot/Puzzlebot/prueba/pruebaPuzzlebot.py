import cv2
import numpy as np
import matplotlib.pyplot as plt

LOWER_RED  = [0,88,179]
UPPER_RED = [33, 255, 255]
LOWER_GREEN = [98,255,255]
UPPER_GREEN = [49, 39, 130]

# Erode Delay Kernel:
MATT = [[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]]

image = cv2.imread("lf.jpg")

def preprocessImage(img):
    # Your code here...
    width = int(img.shape[0])
    height = int(img.shape[1])
    img = cv2.resize(img,(height,width))
    img =cv2.GaussianBlur(img,(7,7),0)
