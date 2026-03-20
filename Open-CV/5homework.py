import cv2

user_img = input("enter the path to your image: ")
# Open-CV\IMG.png
img = cv2.imread(user_img)

if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print("img converted to gray")
else:
    print("failed to convert image")

choice = input("do you want to save the img or see the img? press 's' to save and 'p' to preview: ")

if choice == "s":
    name_img = input("enter the name of the image: ")
    cv2.imwrite(f"Open-CV/{name_img}.png", gray)
    print("image saved successfully")
elif choice == "p":
    cv2.imshow("gray", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("invalid choice")