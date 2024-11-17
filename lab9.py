import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageFilter
ddepth = cv.CV_16S
scale = 1
delta = 0
img = Image.open('demo_image.jpg')
img = img.filter(ImageFilter.GaussianBlur)
# img.show()

fig, axs = plt.subplots(1,5,figsize=(15,15))
axs[0].imshow(img)
axs[0].set_title('Gaussian Filter')

src = cv.imread('demo_image.jpg', cv.IMREAD_COLOR)
 
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
src = cv.GaussianBlur(gray, (3, 3), 0)

grad_x = cv.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
 
# Gradient-Y
# grad_y = cv.Scharr(gray,ddepth,0,1)
grad_y = cv.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)

abs_grad_x = cv.convertScaleAbs(grad_x)
abs_grad_y = cv.convertScaleAbs(grad_y)

grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

axs[1].imshow(grad)
axs[1].set_title("Sobel Filter")

img2 = cv.imread('demo_image.jpg')
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv.filter2D(src, -1, kernelx)
img_prewitty = cv.filter2D(src, -1, kernely)

axs[2].imshow(img_prewittx)
axs[2].set_title("Prewitt Filter X")

axs[3].imshow(img_prewitty)
axs[3].set_title("Prewitt Filter Y")

dst = cv.Laplacian(gray, ddepth, ksize=3)
abs_dst = cv.convertScaleAbs(dst)

axs[4].imshow(abs_dst)
axs[4].set_title("Laplacian Filter")

plt.show()