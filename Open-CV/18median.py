import cv2

img = cv2.imread("Open-CV/rahul.png")

blurimg = cv2.medianBlur(img, 3)

cv2.imshow("OG", img)
cv2.imshow("blurimg", blurimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
