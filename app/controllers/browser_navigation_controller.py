import pyautogui


class BrowserNavigationController:
    def navigate(self, direction):
        if direction == "back":
            pyautogui.hotkey("alt", "left")
        elif direction == "forward":
            pyautogui.hotkey("alt", "right")