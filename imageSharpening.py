from PIL import Image, ImageFilter

def sharpen_image(image_path):
    original_image=Image.open(image_path)

    sharpened_image=original_image.filter(ImageFilter.SHARPEN)

    original_image.show(title='Original Image')
    sharpened_image.show(title='Sharpened Image')

image_path='slightBlur.jpg'

# sharpen_image(image_path)

import cv2

import numpy as np

image=cv2.imread('slightBlur.jpg')
kernel=np.array([[-1,-1,-1],
                 [-1,9,-1],
                 [-1,-1,-1]])
sharpened=cv2.filter2D(image,-1,kernel)
cv2.imshow('Image sharpening', sharpened)
cv2.imshow('Original Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()