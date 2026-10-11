import pyautogui


class MediaController:
    def toggle_play_pause(self):
        pyautogui.press("playpause")