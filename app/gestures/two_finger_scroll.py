# app/gestures/two_finger_scroll.py

from app.utils.helpers import count_fingers_up, get_finger_positions
from app.config.settings import TWO_FINGER_IDS

class TwoFingerScroll:
    def __init__(self, scroll_callback, movement_threshold=20):
        """
        scroll_callback: function to call with 'up' or 'down'
        movement_threshold: minimum Y-axis movement to trigger scrolling
        """
        self.scroll_callback = scroll_callback
        self.prev_y_avg = None
        self.movement_threshold = movement_threshold

    def is_two_finger(self, hand_landmarks):
        return count_fingers_up(hand_landmarks) == 2

    def detect(self, hand_landmarks):
        """
        Detect vertical movement of two fingers and invoke scroll callback.
        Should be called every frame.
        """
        if not self.is_two_finger(hand_landmarks):
            self.prev_y_avg = None
            return None

        fingers = get_finger_positions(hand_landmarks, TWO_FINGER_IDS)
        if len(fingers) != 2:
            self.prev_y_avg = None
            return None

        # Calculate average Y of two fingers
        y_avg = sum(pos[1] for pos in fingers.values()) / 2

        if self.prev_y_avg is None:
            self.prev_y_avg = y_avg
            return None

        delta_y = y_avg - self.prev_y_avg

        if abs(delta_y) > self.movement_threshold:
            direction = "down" if delta_y > 0 else "up"
            self.scroll_callback(direction)

        self.prev_y_avg = y_avg
