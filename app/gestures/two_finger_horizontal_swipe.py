
import time


class TwoFingerHorizontalSwipe:
    def __init__(self, callback, threshold=0.12, cooldown=1.0):
        self.callback = callback
        self.threshold = threshold
        self.cooldown = cooldown
        self.previous_x = None
        self.last_trigger = 0

    def detect(self, hand_landmarks):
        lm = hand_landmarks.landmark

        extended = sum(
            lm[tip].y < lm[tip - 2].y
            for tip in [8, 12, 16, 20]
        )

        if extended != 2:
            self.previous_x = None
            return

        current_x = (lm[8].x + lm[12].x) / 2

        if self.previous_x is None:
            self.previous_x = current_x
            return

        delta = current_x - self.previous_x
        now = time.time()

        if abs(delta) >= self.threshold and now - self.last_trigger >= self.cooldown:
            self.callback("forward" if delta > 0 else "back")
            self.last_trigger = now
            self.previous_x = None
            return

        self.previous_x = current_x
