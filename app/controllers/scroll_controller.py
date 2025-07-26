# app/controllers/scroll_controller.py

import pyautogui
import time
from app.config.settings import SCROLL_SENSITIVITY

class ScrollController:
    def __init__(self):
        self.last_scroll_time = time.time()

    def scroll(self, direction):
        """
        Scrolls the window based on direction.
        :param direction: 'up' or 'down'
        """
        current_time = time.time()
        if current_time - self.last_scroll_time < 0.2:
            return  # Cooldown to avoid rapid scroll

        scroll_amount = SCROLL_SENSITIVITY * 5

        if direction == 'up':
            pyautogui.scroll(scroll_amount)
        elif direction == 'down':
            pyautogui.scroll(-scroll_amount)

        self.last_scroll_time = current_time
