# app/gestures/full_hand_gesture.py

import time
from collections import deque
from app.config.settings import FULL_HAND_SWIPE_THRESHOLD, SWIPE_COOLDOWN_TIME

class FullHandGesture:
    def __init__(self, switch_callback=None):
        """
        switch_callback: function to call on swipe gesture with argument 'left' or 'right'
        """
        self.hand_positions = deque(maxlen=10)
        self.switch_callback = switch_callback
        self.last_swipe_time = 0

    def is_full_hand(self, lm_list):
        """
        Check if all 5 fingers are up (basic check using landmarks).
        """
        if len(lm_list) < 21:
            return False

        fingers = [8, 12, 16, 20]
        base_joints = [6, 10, 14, 18]

        extended = [lm_list[f][1] < lm_list[b][1] for f, b in zip(fingers, base_joints)]
        thumb_extended = lm_list[4][0] > lm_list[3][0]  # Right hand

        return all(extended) and thumb_extended

    def track_swipe(self, lm_list):
        """
        Add wrist x-coord to buffer and detect swipe direction.
        """
        cx = lm_list[0][0]
        self.hand_positions.append(cx)

        if len(self.hand_positions) < self.hand_positions.maxlen:
            return None

        delta = self.hand_positions[-1] - self.hand_positions[0]

        if abs(delta) > FULL_HAND_SWIPE_THRESHOLD:
            now = time.time()
            if now - self.last_swipe_time > SWIPE_COOLDOWN_TIME:
                self.last_swipe_time = now
                return 'right' if delta > 0 else 'left'

        return None

    def detect(self, lm_list):
        """
        Detect full-hand swipe and invoke the switch callback.
        """
        if not self.is_full_hand(lm_list):
            self.hand_positions.clear()
            return None

        direction = self.track_swipe(lm_list)
        if direction and self.switch_callback:
            self.switch_callback(direction)
            return f'Switched {direction.capitalize()}'

        return None
