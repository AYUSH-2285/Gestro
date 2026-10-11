import pyautogui


class BrowserTabController:
    def switch_tab(self, direction="next"):
        if direction == "next":
            pyautogui.hotkey("ctrl", "tab")
        else:
            pyautogui.hotkey("ctrl", "shift", "tab")