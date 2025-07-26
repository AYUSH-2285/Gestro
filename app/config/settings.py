# config/settings.py

# Full-hand gesture thresholds
SWIPE_THRESHOLD = FULL_HAND_SWIPE_THRESHOLD  = 50   # Minimum X-axis movement (pixels) to register a swipe
SWIPE_COOLDOWN_TIME = 1.0  
SWIPE_DETECTION_BUFFER = 5 # Seconds to wait before accepting another swipe
WINDOW_SWITCH_COOLDOWN = 1.0 

# Two-finger scroll thresholds

TWO_FINGER_IDS = [8, 12]  # Index tip (8), Middle tip (12)
TWO_FINGER_MIN_DISTANCE = 40     # Minimum distance between two fingers to be valid
SCROLL_SENSITIVITY = 3           # Higher is slower; lower is more sensitive
THREE_FINGER_IDS = [8, 12, 16]  # Index, Middle, Ring finger tips


# Three-finger gesture thresholds (if used later)
THREE_FINGER_MIN_DISTANCE = 30
THREE_FINGER_MAX_DISTANCE = 80

# Frame processing
MAX_NUM_HANDS = 1                # Only track one hand for control
DETECTION_CONFIDENCE = 0.7
TRACKING_CONFIDENCE = 0.7

# Finger landmark indices (MediaPipe hand landmarks)
FINGER_TIPS = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
