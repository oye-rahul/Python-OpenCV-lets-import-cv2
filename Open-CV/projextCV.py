import cv2
import numpy as np
import mediapipe as mp
import pyautogui
import math
from collections import deque
import time

# Initialize MediaPipe Hands
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path='hand_landmarker.task'),
    running_mode=VisionRunningMode.VIDEO,
    num_hands=1,
    min_hand_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    min_hand_presence_confidence=0.7
)
hands = HandLandmarker.create_from_options(options)

# Screen settings
screen_width, screen_height = pyautogui.size()
pyautogui.FAILSAFE = False

# Smoothing parameters
SMOOTHING_WINDOW = 5
position_history = deque(maxlen=SMOOTHING_WINDOW)

# Click cooldown to prevent multiple clicks
last_click_time = 0
CLICK_COOLDOWN = 0.3  # seconds

# Sensitivity for finger movement
MOVEMENT_SENSITIVITY = 1.5

# Gesture detection thresholds
INDEX_TIP = 8
MIDDLE_TIP = 12
RING_TIP = 16
PINKY_TIP = 20
THUMB_TIP = 4
INDEX_MCP = 5
MIDDLE_MCP = 9
RING_MCP = 13
PINKY_MCP = 17


class HandGestureMouse:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.cap.set(cv2.CAP_PROP_FPS, 30)

        self.prev_x, self.prev_y = screen_width // 2, screen_height // 2
        self.smooth_x, self.smooth_y = self.prev_x, self.prev_y
        self.is_dragging = False
        self.right_click_pending = False

        # FPS calculation
        self.fps_start_time = time.time()
        self.fps_frame_count = 0
        self.fps = 0

    def calculate_distance(self, point1, point2):
        """Calculate Euclidean distance between two points"""
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    def smooth_position(self, new_x, new_y):
        """Apply moving average smoothing to cursor position"""
        position_history.append((new_x, new_y))

        if len(position_history) > 0:
            avg_x = sum(p[0] for p in position_history) / len(position_history)
            avg_y = sum(p[1] for p in position_history) / len(position_history)

            # Exponential smoothing for even smoother movement
            self.smooth_x = self.smooth_x * 0.7 + avg_x * 0.3
            self.smooth_y = self.smooth_y * 0.7 + avg_y * 0.3

            return int(self.smooth_x), int(self.smooth_y)
        return new_x, new_y

    def detect_gestures(self, landmarks, frame_shape):
        """Detect hand gestures for clicks and dragging"""
        h, w, _ = frame_shape

        # Get relevant landmarks
        index_tip = (int(landmarks[INDEX_TIP].x * w), int(landmarks[INDEX_TIP].y * h))
        middle_tip = (int(landmarks[MIDDLE_TIP].x * w), int(landmarks[MIDDLE_TIP].y * h))
        thumb_tip = (int(landmarks[THUMB_TIP].x * w), int(landmarks[THUMB_TIP].y * h))
        index_mcp = (int(landmarks[INDEX_MCP].x * w), int(landmarks[INDEX_MCP].y * h))
        middle_mcp = (int(landmarks[MIDDLE_MCP].x * w), int(landmarks[MIDDLE_MCP].y * h))
        wrist = (int(landmarks[0].x * w), int(landmarks[0].y * h))

        # Calculate a dynamic scale for distance thresholds based on hand size
        # Distance between index mcp and wrist usually stays stable
        hand_size = self.calculate_distance(index_mcp, wrist)

        # Dynamic thresholds
        pinch_threshold = max(hand_size * 0.3, 20) # ensure it is at least 20 pixels
        drag_threshold = hand_size * 0.4

        # Calculate finger distances
        index_thumb_distance = self.calculate_distance(index_tip, thumb_tip)
        middle_thumb_distance = self.calculate_distance(middle_tip, thumb_tip)

        # Check if fingers are extended (simplified method)
        index_extended = index_tip[1] < index_mcp[1] - (hand_size * 0.1)  # Tip above MCP
        middle_extended = middle_tip[1] < middle_mcp[1] - (hand_size * 0.1)

        # Gesture detection
        is_click = False
        is_right_click = False
        is_drag = False

        # Left click: Index and thumb touching
        if index_thumb_distance < pinch_threshold:
            is_click = True
        # Right click: Middle finger and thumb touching
        elif middle_thumb_distance < pinch_threshold:
            is_right_click = True
        # Dragging: Index and middle extended, and thumb touching middle finger
        elif index_extended and middle_extended and middle_thumb_distance < pinch_threshold:
            is_drag = True

        return is_click, is_right_click, is_drag

    def move_mouse(self, landmarks, frame_shape):
        """Move mouse cursor based on index finger position"""
        h, w, _ = frame_shape

        # Use index finger tip for cursor control
        index_tip = landmarks[INDEX_TIP]

        # Map coordinates to screen
        cursor_x = np.interp(index_tip.x, [0.1, 0.9], [0, screen_width])
        cursor_y = np.interp(index_tip.y, [0.1, 0.9], [0, screen_height])

        # Apply sensitivity
        cursor_x = self.prev_x + \
            (cursor_x - self.prev_x) * MOVEMENT_SENSITIVITY
        cursor_y = self.prev_y + \
            (cursor_y - self.prev_y) * MOVEMENT_SENSITIVITY

        # Clamp to screen bounds
        cursor_x = max(0, min(screen_width, cursor_x))
        cursor_y = max(0, min(screen_height, cursor_y))

        # Apply smoothing
        smooth_x, smooth_y = self.smooth_position(cursor_x, cursor_y)

        # Move mouse
        pyautogui.moveTo(smooth_x, smooth_y)

        self.prev_x, self.prev_y = smooth_x, smooth_y
        return smooth_x, smooth_y

    def handle_clicks(self, is_click, is_right_click, is_drag):
        """Handle mouse clicks and dragging"""
        global last_click_time
        current_time = time.time()

        # Handle dragging
        if is_drag:
            if not self.is_dragging:
                pyautogui.mouseDown()
                self.is_dragging = True
        else:
            if self.is_dragging:
                pyautogui.mouseUp()
                self.is_dragging = False

        # Handle left click with cooldown
        if is_click and not self.is_dragging:
            if current_time - last_click_time > CLICK_COOLDOWN:
                pyautogui.click()
                last_click_time = current_time
                return "Left Click"

        # Handle right click
        if is_right_click and not self.is_dragging:
            if current_time - last_click_time > CLICK_COOLDOWN:
                pyautogui.rightClick()
                last_click_time = current_time
                return "Right Click"

        return "None"

    def draw_hand_landmarks(self, frame, landmarks_list, gesture_status):
        """Draw hand landmarks and gesture information"""
        connections = [
            (0, 1), (1, 2), (2, 3), (3, 4), (0, 5), (5, 6), (6, 7), (7, 8),
            (5, 9), (9, 10), (10, 11), (11, 12), (9, 13), (13, 14), (14, 15),
            (15, 16), (13, 17), (17, 18), (18, 19), (19, 20), (0, 17)
        ]
        h, w, _ = frame.shape
        for conn in connections:
            p1 = landmarks_list[conn[0]]
            p2 = landmarks_list[conn[1]]
            x1, y1 = int(p1.x * w), int(p1.y * h)
            x2, y2 = int(p2.x * w), int(p2.y * h)
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        for lm in landmarks_list:
            x, y = int(lm.x * w), int(lm.y * h)
            cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)

        # Draw gesture info on frame
        cv2.putText(frame, f"Gesture: {gesture_status}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, f"FPS: {self.fps:.0f}", (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Draw cursor position on frame
        cv2.putText(frame, f"Cursor: ({self.smooth_x:.0f}, {self.smooth_y:.0f})", (10, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Draw instructions
        instructions = [
            "Instructions:",
            "Index finger tip -> Move cursor",
            "Pinch index + thumb -> Left click",
            "Pinch middle + thumb -> Right click",
            "Index + middle fingers extended -> Drag",
            "Press 'q' to quit"
        ]

        y_offset = frame.shape[0] - 120
        for instruction in instructions:
            cv2.putText(frame, instruction, (10, y_offset),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4, (200, 200, 200), 1)
            y_offset += 20

    def run(self):
        """Main loop for hand gesture mouse control"""
        print("Hand Gesture Mouse Started!")
        print("Press 'q' to quit")

        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            # Flip frame horizontally for mirror effect
            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process hand landmarks using Tasks API
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
            timestamp_ms = int(time.time() * 1000)
            results = hands.detect_for_video(mp_image, timestamp_ms)

            gesture_status = "None"

            if results.hand_landmarks:
                for hand_landmarks in results.hand_landmarks:
                    # Move mouse cursor
                    cursor_x, cursor_y = self.move_mouse(
                        hand_landmarks, frame.shape)

                    # Detect gestures
                    is_click, is_right_click, is_drag = self.detect_gestures(
                        hand_landmarks, frame.shape
                    )

                    # Handle mouse actions
                    gesture_status = self.handle_clicks(
                        is_click, is_right_click, is_drag)

                    # Draw landmarks
                    self.draw_hand_landmarks(
                        frame, hand_landmarks, gesture_status)

                    # Visual feedback for gestures
                    h, w, _ = frame.shape
                    index_tip = hand_landmarks[INDEX_TIP]
                    index_pos = (int(index_tip.x * w), int(index_tip.y * h))

                    # Draw cursor circle at index tip position
                    cv2.circle(frame, index_pos, 15, (0, 255, 0), 2)

                    # Visual feedback for clicks
                    if gesture_status != "None":
                        cv2.circle(frame, index_pos, 20, (0, 0, 255), -1)

            # Calculate FPS
            self.fps_frame_count += 1
            if time.time() - self.fps_start_time >= 1:
                self.fps = self.fps_frame_count
                self.fps_frame_count = 0
                self.fps_start_time = time.time()

            # Display frame
            cv2.imshow("Hand Gesture Mouse Controller", frame)

            # Quit on 'q' press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Cleanup
        self.cap.release()
        cv2.destroyAllWindows()


# Install required packages if not already installed

if __name__ == "__main__":
    # Optional: Adjust pyautogui settings for better performance
    pyautogui.PAUSE = 0  # Remove delay between actions
    pyautogui.MINIMUM_DURATION = 0  # Remove minimum duration

    hand_mouse = HandGestureMouse()
    hand_mouse.run()
