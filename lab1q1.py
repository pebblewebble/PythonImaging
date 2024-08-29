import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage.io import imshow, imread
from skimage.color import rgb2hsv
from skimage.color import rgb2gray
import cv2
array_1=np.array([[255,0],
                 [0,255]], dtype=np.uint8)

cv2.imshow("Test",array_1 );
cv2.waitKey(0)
cv2.destroyAllWindows()





