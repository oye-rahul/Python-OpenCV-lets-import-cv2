import cv2

img = cv2.imread("Open-CV\IMG.png")

if img is not None:
    success = cv2.imwrite("Open-CV\saved.png", img)
    if success:
        print("image saved successfully")
    else:
        print("failed to save image")
else:
    print("failed to load image")