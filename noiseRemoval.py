import cv2 
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('imagewithnoise.jpg')

plt.subplot(1,4,1)
plt.title("Original")
plt.imshow(image)
filtered_image=cv2.medianBlur(image,11)
size = (5,5)
shape=cv2.MORPH_RECT
kernel=cv2.getStructuringElement(shape,size)
# kernel=np.ones((5,5),np.uint8)
maxFilter_image=cv2.dilate(image,kernel)
minFilter_image=cv2.erode(image,kernel)
cv2.imwrite('Median Blur.jpg',filtered_image)
plt.subplot(1,4,2)
plt.title("Median Blur")
plt.imshow(filtered_image)
cv2.imwrite('Max Blur.jpg',maxFilter_image)
plt.subplot(1,4,3)
plt.title("Max Blur")
plt.imshow(maxFilter_image)
cv2.imwrite('Min Blur.jpg',minFilter_image)
cv2.imwrite('Original Image.jpg',image)
plt.subplot(1,4,4)
plt.title("Min Blur")
plt.imshow(minFilter_image)
plt.show()