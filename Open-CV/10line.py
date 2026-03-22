import cv2

img = cv2.imread("Open-CV\IMG.png")

if img is not None:
    pt1 = (50,500)
    #point = (X means left se, Y means upar se )
    pt2 = (500,500)
    #p1 se p2 tak ka distance
    color = (255,0,0)
    thickness = 4
    
    lineimg = cv2.line(img, pt1, pt2, color, thickness)
    cv2.imshow("line wali img", lineimg)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
