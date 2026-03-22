import cv2

img = cv2.imread("Open-CV\IMG.png")

if img is not None:
    flip_H = cv2.flip(img,1)
    flip_V = cv2.flip(img,0)
    flip_both = cv2.flip(img,-1)

    cv2.imshow("OG",img)
    cv2.imshow("Horizontal",flip_H)
    cv2.imshow("vertical",flip_V)
    cv2.imshow("both",flip_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()