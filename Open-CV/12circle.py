# isme na ek point liya jata h like 50,50 pe ek point aya to wha se ye point se ek 10 ya jitne ka redis doge utna 360 circle banadega 
import cv2

img = cv2.imread("Open-CV\IMG.png")

if img is not None:
    point = (460, 410)
    redius = 80
    color = (255,0,0)
    thickness = 3 

    circle_img = cv2.circle(img, point, redius , color, thickness)
    # circle_img = cv2.circle(img, (250, 280), 50 , (255,0,0), 5)
    cv2.imshow("circle img", circle_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()