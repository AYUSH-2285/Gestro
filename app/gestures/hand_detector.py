# app/gestures/hand_detector.py

import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self, max_hands=2):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=max_hands)
        self.mp_draw = mp.solutions.drawing_utils

    def detect(self, frame):
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)

        if self.results.multi_hand_landmarks:
            return self.results.multi_hand_landmarks
        return []

    def get_landmark_positions(self, hand_landmarks, image_shape):
        h, w, _ = image_shape
        landmarks = []
        for lm in hand_landmarks.landmark:
            cx, cy = int(lm.x * w), int(lm.y * h)
            landmarks.append((cx, cy))
        return landmarks
