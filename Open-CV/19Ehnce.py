import cv2
import numpy as np

img = cv2.imread("Open-CV/blur.png")

#high level of sharpnnes
sharping_K1 = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

# veryy high level of sharpnnes
sharping_K2 = np.array([
    [-1, -1, -1],
    [-1, 9, -1],
    [-1, -1, -1]
])

# ultra high level of sharpnnes
sharping_K3 = np.array([
    [-2, -3, -2],
    [-3, 21, -3],
    [-2, -3, -2]
])

sharpImg = cv2.filter2D(img, -1, sharping_K3)

cv2.imshow("OG IMG", img)
cv2.imshow("SHARP IMG", sharpImg)
cv2.waitKey(0)
cv2.destroyAllWindows()