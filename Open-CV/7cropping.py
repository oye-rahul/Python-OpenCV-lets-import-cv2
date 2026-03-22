import cv2

img = cv2.imread("Open-CV\IMG.png")

if img is not None:
    cropped = img[250:550, 500:1000]
    # img[StartY : endY, StartX : endX, ]
    cv2.imshow("cropped img", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()