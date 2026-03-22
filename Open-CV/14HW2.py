import cv2
# img ka input liya apne ne
# example of img (C:\Users\hp\OneDrive\Pictures\ChatGPT Image Feb 1, 2026, 06_48_04 PM.png)
input_img = input("enter your path: ")
img = cv2.imread(input_img)

# check img
if img is not None:
    print("succfulyyy img load")
print("""
      'press any number to do any task on your img'
press 1 for line,
press 2 for rectangle,
press 3 for circal,
press 4 for write a 'Text'...
""")

user_task_input = input("which is your task '1,2,3,4.': ")

if user_task_input == '1':
    print("For Line i want some inputs")
    Yinp_p1 = int(input("whar line Starts for Y-axis(left se) Ex.50 : "))
    Xinp_p1 = int(input("whar line Starts for X-axis(up se) Ex.50 : "))
    pt1 = (Yinp_p1, Xinp_p1)

    Yinp_p2 = int(input("whar line End for Y-axis(right tk) Ex.100 : "))
    Xinp_p2 = int(input("whar line End for X-axis(up tk) Ex.100 : "))
    pt2 = (Yinp_p2, Xinp_p2)

    color = (255, 0, 0)
    thickness = int(input("Thickness of Line Ex. 1,2,3 : "))
    lineimg = cv2.line(img, pt1, pt2, color, thickness)

    print("Do You want to save / open this img.")
    user_img_select = input("press 's' for save and 'o' for open: ")
    if user_img_select == 's':
        print("image saved !!!")
    elif user_img_select == 'o':
        cv2.imshow("line wali img", lineimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

elif user_task_input == '2':
    print("For rectangle we want to add some input")
    Yinp_p1 = int(input("whar line Starts for Y-axis(left se) Ex.50 : "))
    Xinp_p1 = int(input("whar line Starts for X-axis(up se) Ex.50 : "))
    pt1 = (Yinp_p1, Xinp_p1)

    Yinp_p2 = int(input("whar line End for Y-axis(right tk) Ex.100 : "))
    Xinp_p2 = int(input("whar line End for X-axis(up tk) Ex.100 : "))
    pt2 = (Yinp_p2, Xinp_p2)

    color = (255, 0, 0)
    thickness = int(input("Thickness of Line Ex. 1,2,3 : "))

    rectimg = cv2.rectangle(img, pt1, pt2, color, thickness)

    print("Do You want to save / open this img.")
    user_img_select = input("press 's' for save and 'o' for open: ")
    if user_img_select == 's':
        print("image saved !!!")
    elif user_img_select == 'o':
        cv2.imshow("line wali img", rectimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

elif user_task_input == '3':
    print("for circle we want to add some input")
    Yinp_p1 = int(input("whar line Starts for Y-axis(left se) Ex.50 : "))
    Xinp_p1 = int(input("whar line Starts for X-axis(up se) Ex.50 : "))
    point = (Yinp_p1, Xinp_p1)

    redius = int(input("entr the redius Ex.50,100: "))
    color = (255, 0, 0)
    thickness = int(input("Thickness of Line Ex. 1,2,3 : "))

    circle_img = cv2.circle(img, point, redius, color, thickness)

    print("Do You want to save / open this img.")
    user_img_select = input("press 's' for save and 'o' for open: ")
    if user_img_select == 's':
        print("image saved !!!")
    elif user_img_select == 'o':
        cv2.imshow("line wali img", circle_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
elif user_task_input == '4':
    print("For input text write a text")
    Yinp_p1 = int(input("whar text is show for Y-axis(left se) Ex.50 : "))
    Xinp_p1 = int(input("whar text is show for X-axis(up se) Ex.50 : "))
    point = (Yinp_p1, Xinp_p1)
    thickness = int(input("Thickness of Line Ex. 1,2,3 : "))
    user_text_input = input("entr your text here that show on img: ")
    Textimg = cv2.putText(img, user_text_input, point,
                          cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 255), thickness)

    print("Do You want to save / open this img.")
    user_img_select = input("press 's' for save and 'o' for open: ")
    if user_img_select == 's':
        print("image saved !!!")
    elif user_img_select == 'o':
        cv2.imshow("line wali img", Textimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
       print("invelid input")
else:
    print("Image is not found")
