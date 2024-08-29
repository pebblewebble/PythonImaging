import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = cv2.imread('input_image.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,70,255,0)
cv2.imshow("binary image",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
# imgplot=plt.imshow(img)
# plt.show()
# plt.imshow(cv2.cvtColor(thresh, cv2.COLOR_BGR2RGB))
# cv2.waitKey(0)
# cv2.destroyAllWindows()
