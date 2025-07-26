Gestro/
│
├── app/                            # Core application logic
│   ├── gestures/                   # Gesture recognition modules
│   │   ├── hand_detector.py        # MediaPipe hand detection logic
│   │   ├── full_hand_gesture.py    # Detect full-hand swipe (left/right)
│   │   ├── two_finger_scroll.py    # Detect two-finger scroll (up/down)
│   │   └── three_finger_gesture.py # Detect 3-finger gestures (e.g., minimize, maximize)
│   │
│   ├── controllers/                # Trigger OS actions from gestures
│   │   ├── window_switcher.py      # Switch window left/right
│   │   ├── scroll_controller.py    # Scroll window up/down
│   │   └── three_finger_actions.py # Control window state (minimize, maximize)
│   │
│   └── main.py                     # Main control loop
│
├── config/                         # Configuration values
│   └── settings.py                 # Gesture thresholds, finger ID config
│
├── utils/                          # Helper functions (optional but useful)
│   └── helpers.py
│
├── requirements.txt                # Python dependencies
├── README.md                       # Project overview and instructions
├── .gitignore                      # Ignore venv, __pycache__, etc.
└── run.py                          # Entry point to start the system




# Gestro 🎯 - Gesture-Based Window Control System

**Gestro** is a real-time hand gesture recognition system built with Python, OpenCV, and MediaPipe. It allows users to control windows using hand gestures like:

- 🖐️ Full-hand swipes to switch between windows
- ✌️ Two-finger gestures for scrolling
- 🤟 Three-finger gestures to minimize all windows

---

## 🚀 Features

- Full-hand gesture → Switch window (left/right)
- Two-finger gesture → Scroll (up/down)
- Three-finger gesture → Minimize all windows
- Modular gesture detection design
- Callback-based architecture for flexibility

---

## 🛠️ Technologies Used

- Python
- OpenCV
- MediaPipe
- PyAutoGUI
- Modular OOP architecture

---

## 🔧 Installation

```bash
git clone https://github.com/AYUSH-2285/Gestro.git
cd Gestro
python -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
