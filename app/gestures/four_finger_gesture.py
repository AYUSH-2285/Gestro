
import time


class FourFingerGesture:
    def __init__(self, callback, cooldown=1.0):
        self.callback = callback
        self.cooldown = cooldown
        self.last_trigger = 0
        self.active = False

    def is_four_finger(self, hand_landmarks):
        lm = hand_landmarks.landmark

        # Count index, middle, ring and pinky fingers
        extended = sum(
            lm[tip].y < lm[tip - 2].y
            for tip in [8, 12, 16, 20]
        )

        # Thumb should be folded
        thumb_folded = abs(lm[4].x - lm[0].x) < 0.15

        return extended == 4 and thumb_folded

    def detect(self, hand_landmarks):
        now = time.time()

        if not self.is_four_finger(hand_landmarks):
            self.active = False
            return

        if not self.active and now - self.last_trigger >= self.cooldown:
            self.callback("next")
            self.last_trigger = now
            self.active = True
