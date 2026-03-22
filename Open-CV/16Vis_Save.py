import cv2

camera =  cv2.VideoCapture(0)

frame_W = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_H = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'mp4v')
recoded = cv2.VideoWriter("my_vid.mp4",codec, 20, (frame_W, frame_H))

while True:
    success, img = camera.read()

    if not success:
        break

    recoded.write(img)
    cv2.imshow("this is recoded", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
recoded.release()
cv2.destroyAllWindows()