# import cv2

# face_C = cv2.CascadeClassifier("Open-CV/haarcascade_frontalcatface_extended.xml")
# eye_C = cv2.CascadeClassifier("Open-CV/haarcascade_eye.xml")
# smile_C = cv2.CascadeClassifier("Open-CV/haarcascade_smile.xml")


# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()

#     # Convert the frame to grayscale for better detection
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Detect faces in the image
#     faces = face_C.detectMultiScale(gray, 1.1, 5)

#     # Draw rectangles around detected faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

#     roi_gray = gray[y:y+h, x:x+w]
#     roi_color = frame[y:y+h, x:x+w]

#     eye = eye_C.detectMultiScale(roi_gray, 1.1, 10)
#     if len(eye) > 0:
#         cv2.putText(frame, "Eye is ditc", (150, 270),cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 255), 2)
#     smile = smile_C.detectMultiScale(roi_gray, 1.7, 20)
#     if len(smile) > 0:
#         cv2.putText(frame, "smileing", (150, 270),cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 255), 2)

#     # Display the result in a window
#     cv2.imshow("smart face detc", frame)

#     # Exit the loop when 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the camera and close the window
# cap = cv2.VideoCapture(0)
# if not cap.isOpened():
#     print("Error: Could not access the webcam.")
#     exit()

# cv2.destroyAllWindows()


import cv2
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def load_classifier(filename):
    classifier_path = BASE_DIR / filename
    classifier = cv2.CascadeClassifier(str(classifier_path))
    if classifier.empty():
        raise FileNotFoundError(f"Could not load classifier: {classifier_path}")
    return classifier


# Load classifiers
face_C = load_classifier("haarcascade_frontalcatface_extended.xml")
eye_C = load_classifier("haarcascade_eye.xml")
smile_C = load_classifier("haarcascade_smile.xml")

# Start webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("Error: Could not access the webcam.")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_C.detectMultiScale(gray, 1.1, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            roi_gray = gray[y:y + h, x:x + w]

            # Detect eyes
            eyes = eye_C.detectMultiScale(roi_gray, 1.1, 10)
            if len(eyes) > 0:
                cv2.putText(frame, "Eye detected", (50, 50),
                            cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 255), 2)

            # Detect smile
            smiles = smile_C.detectMultiScale(roi_gray, 1.7, 20)
            if len(smiles) > 0:
                cv2.putText(frame, "Smiling", (50, 100),
                            cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 255), 2)

        cv2.imshow("Smart Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # Always release camera/window resources even on runtime errors.
    cap.release()
    cv2.destroyAllWindows()
