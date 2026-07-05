import cv2

img = cv2.imread("Open-CV/IMG.png")
gray = cv2.cvtColor(img,  cv2.COLOR_BGR2GRAY)
_, th_img = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

contours, heirarchy = cv2.findContours(th_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0,255,0),3)
# cv2.imshow("new img", th_img)
cv2.imshow("OG img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
