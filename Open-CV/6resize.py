import cv2

img = cv2.imread("Open-CV\IMG.png")

if img is None:
    print("img is not found")
else:
    print("img loaded")

    resize = cv2.resize(img, (300,300))
    # phele W fir H
    cv2.imshow("OG img", img)
    cv2.imshow("new img after resize", resize)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

