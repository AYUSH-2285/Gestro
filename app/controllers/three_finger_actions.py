# app/controllers/three_finger_actions.py

import pyautogui
import time
from app.config.settings import THREE_FINGER_THRESHOLD

class ThreeFingerActions:
    def __init__(self):
        self.prev_y = None
        self.last_action_time = time.time()

    def detect_and_act(self, hand_landmarks):
        """
        Detects 3-finger vertical movement and triggers window snapping.
        :param hand_landmarks: List of hand landmarks from MediaPipe
        """
        current_time = time.time()
        if current_time - self.last_action_time < 0.5:
            return  # Cooldown

        # Finger tip landmarks: Index (8), Middle (12), Ring (16)
        tips = [hand_landmarks[8], hand_landmarks[12], hand_landmarks[16]]
        avg_y = sum([pt.y for pt in tips]) / 3

        if self.prev_y is None:
            self.prev_y = avg_y
            return

        delta_y = self.prev_y - avg_y

        if delta_y > THREE_FINGER_THRESHOLD:
            self.window_snap_up()
            self.last_action_time = current_time
        elif delta_y < -THREE_FINGER_THRESHOLD:
            self.window_snap_down()
            self.last_action_time = current_time

        self.prev_y = avg_y

    def window_snap_up(self):
        # Windows shortcut: Win + Up Arrow
        pyautogui.hotkey('winleft', 'up')

    def window_snap_down(self):
        # Windows shortcut: Win + Down Arrow
        pyautogui.hotkey('winleft', 'down')
