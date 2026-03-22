import cv2

img = cv2.imread("Open-CV\IMG.png")

if img is not None:
    (h, w) = img.shape[:2]

    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, 90, 1.0)
    #(khase rotated karna h, kitna karna h 90*, zoom)
    rotated = cv2.warpAffine(img, M, (w,h))

    cv2.imshow("rotated img", rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
