# app/controllers/window_switcher.py

import pyautogui
import time
from app.config.settings import WINDOW_SWITCH_COOLDOWN

class WindowSwitcher:
    def __init__(self):
        self.last_switch_time = time.time()
        
    def switch_window(self, direction):
        if direction == 'left':
            self.switch_left()
        elif direction == 'right':
            self.switch_right()

    def switch_left(self):
        """Simulate Win + Ctrl + Left Arrow to move to the desktop on the left."""
        current_time = time.time()
        if current_time - self.last_switch_time > WINDOW_SWITCH_COOLDOWN:
            pyautogui.hotkey('winleft', 'ctrlleft', 'left')
            self.last_switch_time = current_time

    def switch_right(self):
        """Simulate Win + Ctrl + Right Arrow to move to the desktop on the right."""
        current_time = time.time()
        if current_time - self.last_switch_time > WINDOW_SWITCH_COOLDOWN:
            pyautogui.hotkey('winleft', 'ctrlleft', 'right')
            self.last_switch_time = current_time
            
    # inside class WindowSwitcher
    def scroll_window(self, direction):
        if direction == 'up':
            pyautogui.scroll(500)
        elif direction == 'down':
            pyautogui.scroll(-500)
            
    def minimize_all_windows(self):
        """Simulate Win + D to show desktop (minimize all windows)."""
        pyautogui.hotkey('winleft', 'd')


