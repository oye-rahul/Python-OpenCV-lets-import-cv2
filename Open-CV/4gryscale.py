import cv2

img = cv2.imread("Open-CV\IMG.png")

if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("failed to load image")