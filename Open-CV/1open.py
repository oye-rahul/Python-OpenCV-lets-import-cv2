import cv2

img = cv2.imread("Open-CV\IMG.png")

if img is not None:
    cv2.imshow("img od dino", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("faill to open img") 