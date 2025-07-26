# app/gestures/three_finger_gesture.py

from app.utils.helpers import count_fingers_up

class ThreeFingerControl:
    def __init__(self, minimize_callback):
        """
        minimize_callback: function to call when 3 fingers are detected.
        """
        self.minimize_callback = minimize_callback
        self.triggered = False  # Prevent repeated triggering in same gesture

    def is_three_finger(self, hand_landmarks):
        """Return True if exactly 3 fingers are up."""
        return count_fingers_up(hand_landmarks) == 3

    def detect(self, hand_landmarks):
        """Trigger minimize action once per 3-finger gesture."""
        if self.is_three_finger(hand_landmarks):
            if not self.triggered:
                self.minimize_callback()
                self.triggered = True
        else:
            self.triggered = False  # Reset when gesture is not active
