import numpy as np
import cv2 as cv 
#Read an image using OpenCV
img = cv.imread('input_image.jpg')
blue,green,red=cv.split(img)
#Example : Increase Red Color
red_adjusted=cv.addWeighted(red,1.5,red,0,0)

#Merge the channels back together
adjusted_img=cv.merge((blue,green,red_adjusted))

cv.imshow('Color Balance Adjusted',adjusted_img)

