import cv2

img = cv2.imread("Open-CV/cat.png", cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(img, 50, 150)

cv2.imshow("new img", edges)
cv2.imshow("OG img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()