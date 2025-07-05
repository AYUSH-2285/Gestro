# utils/hand_tracker.py

import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, max_hands=1, detection_conf=0.7):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=max_hands,
                                         min_detection_confidence=detection_conf)
        self.mp_draw = mp.solutions.drawing_utils
        self.results = None

    def find_hands(self, frame, draw=True):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(rgb)

        if self.results.multi_hand_landmarks and draw:
            for hand in self.results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame, hand, self.mp_hands.HAND_CONNECTIONS)
        return frame

    def get_landmark_positions(self, frame, hand_no=0):
        lm_list = []
        h, w, _ = frame.shape

        if self.results and self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_no]
            for id, lm in enumerate(my_hand.landmark):
                px, py = int(lm.x * w), int(lm.y * h)
                lm_list.append((id, px, py))
        return lm_list
