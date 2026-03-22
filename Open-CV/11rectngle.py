    #in rectangle ham do cornr ko pakade ge means ham phele
    #"top left se" -> "down right tk"
    # |----
    # |   ithar se 
    # ithar tak  |
    #         ___|

import cv2

img = cv2.imread("Open-CV\IMG.png")

if img is not None:
    point1 = (150, 280)
    point2 = (850, 700)
    color = (255,0,0)
    thickness = 3 

    rectimg = cv2.rectangle(img, point1, point2, color, thickness)
    cv2.imshow("Rectangle img", rectimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()