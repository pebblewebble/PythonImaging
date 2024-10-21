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

fig, axs = plt.subplots(2,3,figsize=(15,10))
axs[0,0].imshow(img)
axs[0,0].set_title('Gaussian Filter')

src = cv.imread('demo_image.jpg', cv.IMREAD_COLOR)
src = cv.GaussianBlur(src, (3, 3), 0)
 
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
 
grad_x = cv.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
 
# Gradient-Y
# grad_y = cv.Scharr(gray,ddepth,0,1)
grad_y = cv.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)

abs_grad_x = cv.convertScaleAbs(grad_x)
abs_grad_y = cv.convertScaleAbs(grad_y)

grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

axs[0,1].imshow(grad)
axs[0,1].set_title("Sobel Filter")

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

# Apply Gaussian smoothing
blur = cv.GaussianBlur(gray, (3, 3), 0)

# Define the Prewitt kernel for the x and y directions
prewittx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
prewitty = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

# Calculate the Prewitt gradient in the x and y directions
sobelx = cv.filter2D(blur, -1, prewittx)
sobely = cv.filter2D(blur, -1, prewitty)

# Compute the gradient magnitude and direction
mag, angle = cv.cartToPolar(sobelx, sobely, angleInDegrees=True)

# Threshold the magnitude to obtain the edges
edges = cv.threshold(mag, 50, 255, cv.THRESH_BINARY)[1]

axs[0,2].imshow(edges)
axs[0,2].set_title("Prewitt Filter")

plt.show()