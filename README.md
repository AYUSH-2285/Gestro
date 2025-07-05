# ✋ Gestro - Gesture-Based Virtual Mouse Control

Control your computer using just your hand gestures!  
**Gestro** is a Python-based virtual mouse controller that tracks your index finger using webcam and allows you to move the cursor, click by pinching, and toggle control on/off — all hands-free.

---

## 🔥 Features

- 👆 Cursor moves with index finger
- 🤏 Pinch (thumb + index) to left-click
- 🎥 Mini live preview window (300x300)
- 🟢 Toggle gesture control (`T` key)
- ❌ Quit with `Q` key or close window
- 🧠 Smoothing enabled for stable cursor
- 📦 Modular code (with `hand_tracker.py`)


## 🛠️ Tech Stack

- Python 3.10+
- OpenCV
- MediaPipe
- PyAutoGUI

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/Gestro.git
cd Gestro
```

### 2. Setup Virtual Environment (recommended)
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
python main.py
```


##🖥️ Controls

| Action           | How                               |
| ---------------- | --------------------------------- |
| 🖱️ Move Cursor  | Move your **index finger**        |
| 👆 Left Click    | Pinch with **index + thumb**      |
| 🔁 Toggle ON/OFF | Press `T` key                     |
| ❌ Quit           | Press `Q` or close preview window |



##🧠 Real-World Use Case

This project helps users control their system touch-free — useful for:
Accessibility (hands-free control)

Artists (gesture-based control)

Clean rooms / labs

Futuristic UI experiments
