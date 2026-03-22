#isme hm text add kar sakte h 

import cv2

img = cv2.imread("Open-CV\IMG.png")

if img is not None:
    #cv2.putText(img, text, org, font, fontscale, color, thikness)
    Textimg = cv2.putText(img, "This Is Face", (150, 270), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,255,255), 2)

    point1 = (150, 280)
    point2 = (850, 700)
    color = (255,0,0)
    thickness = 3 
    rectimg = cv2.rectangle(Textimg, point1, point2, color, thickness)
    cv2.imshow("Rectangle img", rectimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()