# app/gestures/two_finger_scroll.py

from app.utils.helpers import count_fingers_up, get_finger_positions
from app.config.settings import TWO_FINGER_IDS
import time

class TwoFingerScroll:
    def __init__(self, scroll_callback, movement_threshold=15, debounce_time=0.1):
        """
        scroll_callback: function to call with 'up' or 'down'
        movement_threshold: min Y movement to scroll
        debounce_time: min time between scrolls
        """
        self.scroll_callback = scroll_callback
        self.prev_y_avg = None
        self.movement_threshold = movement_threshold
        self.debounce_time = debounce_time
        self.last_scroll_time = time.time()
        self.scroll_in_progress = False

    def is_two_finger(self, hand_landmarks):
        return count_fingers_up(hand_landmarks) == 2

    def detect(self, hand_landmarks):
        if not self.is_two_finger(hand_landmarks):
            self.prev_y_avg = None
            self.scroll_in_progress = False
            return

        fingers = get_finger_positions(hand_landmarks, TWO_FINGER_IDS)
        if len(fingers) != 2:
            self.prev_y_avg = None
            self.scroll_in_progress = False
            return

        y_avg = sum(pos[1] for pos in fingers.values()) / 2

        if self.prev_y_avg is None:
            self.prev_y_avg = y_avg
            return

        delta_y = y_avg - self.prev_y_avg
        current_time = time.time()

        if abs(delta_y) > self.movement_threshold and (current_time - self.last_scroll_time) > self.debounce_time:
            direction = "down" if delta_y > 0 else "up"
            self.scroll_callback(direction)
            self.last_scroll_time = current_time
            self.scroll_in_progress = True
        elif abs(delta_y) < 3:  # finger is stabilized
            self.scroll_in_progress = False

        self.prev_y_avg = y_avg
