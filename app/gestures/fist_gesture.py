
import time


class FistGesture:
    def __init__(self, callback, cooldown=1.0):
        self.callback = callback
        self.cooldown = cooldown
        self.last_trigger = 0
        self.active = False

    def is_fist(self, hand_landmarks):
        lm = hand_landmarks.landmark

        # All four fingers should be folded
        fingers_folded = all(
            lm[tip].y > lm[tip - 2].y
            for tip in [8, 12, 16, 20]
        )

        # Thumb should also be folded toward the palm
        thumb_folded = (
            abs(lm[4].x - lm[5].x) < 0.12
        )

        return fingers_folded and thumb_folded

    def detect(self, hand_landmarks):
        now = time.time()

        if not self.is_fist(hand_landmarks):
            self.active = False
            return

        if not self.active and now - self.last_trigger >= self.cooldown:
            self.callback()
            self.last_trigger = now
            self.active = True
