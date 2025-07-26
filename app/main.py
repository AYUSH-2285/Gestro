# main.py

import cv2
from app.gestures.hand_detector import HandDetector
from app.gestures.full_hand_gesture import FullHandGesture
from app.gestures.two_finger_scroll import TwoFingerScroll
from app.controllers.three_finger_actions import ThreeFingerActions  # ✅ NEW
from app.controllers.window_switcher import WindowSwitcher

# Create one instance of the controller
window_switcher = WindowSwitcher()

def switch_callback(direction: str) -> None:
    if direction == "left":
        window_switcher.switch_left()
    elif direction == "right":
        window_switcher.switch_right()

def scroll_callback(direction: str) -> None:
    """Callback to scroll windows based on gesture direction."""
    window_switcher.scroll_window(direction)

def initialize_gesture_handlers() -> tuple:
    """Initialize and return gesture handler instances."""
    full_hand = FullHandGesture(switch_callback=switch_callback)
    two_finger = TwoFingerScroll(scroll_callback=scroll_callback)
    three_finger = ThreeFingerActions()  # ✅ Use motion-based class
    return full_hand, two_finger, three_finger

def main():
    print("[INFO] Gestro is starting...")

    cap = cv2.VideoCapture(0)
    detector = HandDetector()

    full_hand, two_finger, three_finger = initialize_gesture_handlers()

    print("[INFO] Gestro is running. Perform hand gestures to control windows.")
    print("[INFO] Press 'q' or ESC to quit at any time.")

    try:
        while True:
            success, frame = cap.read()
            if not success:
                print("[WARNING] Failed to read from webcam.")
                break

            hand_landmarks_list = detector.detect(frame)

            for hand_landmarks in hand_landmarks_list:
                lm_list = detector.get_landmark_positions(hand_landmarks, frame.shape)

                if full_hand.is_full_hand(lm_list):
                    full_hand.detect(lm_list)

                elif two_finger.is_two_finger(hand_landmarks):
                    two_finger.detect(hand_landmarks)

                else:
                    three_finger.detect_and_act(hand_landmarks)  # ✅ Detect scroll only on vertical movement

            # Draw status message
            cv2.putText(
                frame,
                "Gestro running... Press 'q' or ESC to quit.",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

            cv2.imshow("Gestro", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == 27 or key == ord('q'):
                print("[INFO] 'q' or ESC key pressed. Exiting Gestro.")
                break

    except Exception as e:
        print(f"[ERROR] Unexpected error occurred: {e}")

    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("[INFO] Gestro shut down gracefully.")

if __name__ == "__main__":
    main()
