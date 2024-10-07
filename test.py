import cv2
import numpy as np
 
""""
# Load the image
image = cv2.imread("GreenPen.JPG")
 
# Display the original image
cv2.imshow('Original Image', image)
cv2.waitKey(0)
 
# Define the color range for the green color in HSV
# Adjust the range to cover more shades of green if necessary
lower_green = np.array([35, 40, 40])
upper_green = np.array([85, 255, 255])
 
# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
 
# Create a mask for the green color
mask_green = cv2.inRange(hsv_image, lower_green, upper_green)
 
# Define the purple color in BGR
purple = np.array([128, 0, 128])
 
# Apply the mask to change the green color to purple
# Use np.where to change the color
image[np.where(mask_green == 255)] = purple
 
# Display the modified image
cv2.imshow('Modified Image', image)
cv2.waitKey(0)
 
# Close all OpenCV windows
cv2.destroyAllWindows()
"""
 
# Load the image
image = cv2.imread("C:\\Users\\Eric\\Desktop\\degree\\level2sem2\\Imaging\\Codes\\image.png")
print(image)
# Display the original image
cv2.imshow('Original Image', image)
cv2.waitKey(0)
 
# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
 
# Define the lower and upper bounds for yellow hues in HSV
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([40, 255, 255])  # Adjust the upper bound for yellow hues as needed
 
# Create a mask for all shades of yellow
yellow_mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
 
# Replace yellow pixels with red
image[np.where(yellow_mask == 255)] = (0, 0, 255)  # BGR value for red
 
# Display the modified image
cv2.imshow('Modified Image', image)
cv2.waitKey(0)
 
 
# Load the image
image = cv2.imread("C:\\Users\\Eric\\Desktop\\degree\\level2sem2\\Imaging\\Codes\\image.png")
 
# Display the original image
cv2.imshow('Original Image', image)
cv2.waitKey(0)
 
# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
 
# Define the lower and upper bounds for red hues in HSV
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])  # Adjust the upper bound for red hues as needed
 
# Create a mask for all shades of red
red_mask = cv2.inRange(hsv_image, lower_red, upper_red)
 
# Replace red pixels with blue
image[np.where(red_mask == 255)] = (255, 0, 0)  # BGR value for blue
 
# Display the modified image
cv2.imshow('Modified Image (Red to Blue)', image)
cv2.waitKey(0)
 
# Define the lower and upper bounds for blue hues in HSV
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])  # Adjust the upper bound for blue hues as needed
 
# Create a mask for all shades of blue
blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
 
# Replace blue pixels with red
image[np.where(blue_mask == 255)] = (0, 0, 255)  # BGR value for red
 
# Display the modified image
cv2.imshow('Modified Image (Blue to Red)', image)
cv2.waitKey(0)
 
# Close all OpenCV windows
cv2.destroyAllWindows()