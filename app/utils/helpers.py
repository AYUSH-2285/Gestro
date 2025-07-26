import math
from app.config import settings

def calculate_distance(p1, p2):
    """Calculate Euclidean distance between two (x, y) points."""
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

def fingers_up(hand_landmarks):
    """
    Determine which fingers are up.
    Returns a dictionary with finger tip indices as keys and boolean values.
    """
    tips = settings.FINGER_TIPS
    fingers = {}

    # Hand landmark indices for finger base joints
    base_ids = [2, 6, 10, 14, 18]

    for i, tip in enumerate(tips):
        base = base_ids[i]
        fingers[tip] = hand_landmarks.landmark[tip].y < hand_landmarks.landmark[base].y

    return fingers

def count_fingers_up(hand_landmarks):
    """
    Count how many fingers are up based on hand landmark positions.
    Ignores the thumb and starts from index finger to pinky.
    """
    fingers = [0] * 5
    tip_ids = [4, 8, 12, 16, 20]

    if not hand_landmarks or len(hand_landmarks.landmark) < 21:
        return 0

    for i in range(1, 5):  # Index to Pinky (skip thumb)
        tip = hand_landmarks.landmark[tip_ids[i]]
        pip = hand_landmarks.landmark[tip_ids[i] - 2]
        fingers[i] = 1 if tip.y < pip.y else 0  # y is inverted

    return sum(fingers)

def get_finger_positions(hand_landmarks, finger_ids):
    """
    Returns a dictionary of (x, y) positions for given finger IDs.
    """
    return {
        fid: (hand_landmarks.landmark[fid].x, hand_landmarks.landmark[fid].y)
        for fid in finger_ids if fid < len(hand_landmarks.landmark)
    }

def all_fingers_extended(hand_landmarks, finger_ids):
    """
    Returns True if all specified finger IDs are extended (pointing up).
    """
    fingers = fingers_up(hand_landmarks)
    return all(fingers.get(f, False) for f in finger_ids)
