import cv2
import pyautogui
import math
from utils.hand_tracker import HandTracker

# Init
cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

tracker = HandTracker()
screen_w, screen_h = pyautogui.size()

control_enabled = True
prev_x, prev_y = 0, 0
smoothening = 7  # Smoothness level

cv2.namedWindow("Gestro Cam", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Gestro Cam", 300, 300)

print("🖐️ Gestro running (modular). Press T to toggle, Q to quit.")

while True:
    ret, frame = cam.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame = tracker.find_hands(frame)
    landmarks = tracker.get_landmark_positions(frame)

    if landmarks:
        # Index & Thumb
        ix, iy = landmarks[8][1], landmarks[8][2]
        tx, ty = landmarks[4][1], landmarks[4][2]

        # Cursor position
        screen_x = int(ix * screen_w / 640)
        screen_y = int(iy * screen_h / 480)

        curr_x = prev_x + (screen_x - prev_x) / smoothening
        curr_y = prev_y + (screen_y - prev_y) / smoothening
        prev_x, prev_y = curr_x, curr_y

        if control_enabled:
            pyautogui.moveTo(curr_x, curr_y)
            if math.hypot(tx - ix, ty - iy) < 30:
                pyautogui.click()
                cv2.circle(frame, (ix, iy), 15, (0, 255, 255), 3)

        # Visual
        cv2.circle(frame, (ix, iy), 8, (255, 0, 0), -1)
        cv2.circle(frame, (tx, ty), 8, (0, 255, 0), -1)

    cv2.imshow("Gestro Cam", frame)

    # Check for key or window close
    key = cv2.waitKey(1) & 0xFF
    if key == ord('t'):
        control_enabled = not control_enabled
        print(f"[Toggle] Control {'enabled' if control_enabled else 'disabled'}")
    elif key == ord('q'):
        print("[Quit] Exiting Gestro")
        break

    # 💥 Detect if user closed the preview window directly
    if cv2.getWindowProperty("Gestro Cam", cv2.WND_PROP_VISIBLE) < 1:
        print("[Window Closed] Exiting Gestro")
        break

cam.release()
cv2.destroyAllWindows()
