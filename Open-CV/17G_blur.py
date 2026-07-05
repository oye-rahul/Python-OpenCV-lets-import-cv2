import cv2

img = cv2.imread("Open-CV/rahul.png")

blurimg = cv2.GaussianBlur(img, (5,5), 0)

cv2.imshow("blurimg", blurimg)
cv2.imwrite("blur.png", blurimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
