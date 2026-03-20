import cv2

img = cv2.imread("Open-CV\IMG.png")

if img is not None:
    h, w, c = img.shape
    print(f"this image has \n {h} height, \n {w} width, \n and {c} channels.")
else:
    print("failed to load image")