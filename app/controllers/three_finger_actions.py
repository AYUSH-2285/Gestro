# app/controllers/three_finger_actions.py

import pyautogui
import time
from app.utils.helpers import count_fingers_up

# Suitable threshold for normalized MediaPipe Y coordinates
THREE_FINGER_THRESHOLD = 0.05  # 5% of screen height

class ThreeFingerActions:
    def __init__(self):
        self.prev_y = None
        self.last_action_time = time.time()
        self.gesture_in_progress = False

    def detect_and_act(self, hand_landmarks):
        """
        Detect vertical swipe using 3 fingers:
        - Swipe up: maximize
        - Swipe down: show desktop (minimize all windows)
        """
        current_time = time.time()

        # Only continue if exactly 3 fingers are up
        if count_fingers_up(hand_landmarks) != 3:
            self.prev_y = None
            self.gesture_in_progress = False
            return

        # Get average Y of 3 fingertips (index, middle, ring)
        tips = [hand_landmarks.landmark[i] for i in [8, 12, 16]]
        avg_y = sum(pt.y for pt in tips) / 3

        if self.prev_y is None:
            self.prev_y = avg_y
            return

        delta_y = self.prev_y - avg_y  # Positive = upward

        # Swipe up: maximize
        if delta_y > THREE_FINGER_THRESHOLD and not self.gesture_in_progress:
            pyautogui.hotkey('winleft', 'up')
            self.last_action_time = current_time
            self.gesture_in_progress = True

        # Swipe down: minimize all (show desktop)
        elif delta_y < -THREE_FINGER_THRESHOLD and not self.gesture_in_progress:
            pyautogui.hotkey('winleft', 'd')  # ✅ Win + D to show desktop
            self.last_action_time = current_time
            self.gesture_in_progress = True

        # Reset once hand stabilizes
        if abs(delta_y) < 0.01:
            self.gesture_in_progress = False

        self.prev_y = avg_y
