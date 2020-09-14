import pyautogui 
import schedule 
import time 
meetId = "Replace this with Meeting ID"
password = "Replace this with Password"
def attendZoom():
    time.sleep(0.2)
    pyautogui.press('esc',interval=0.1)
    time.sleep(0.3)
    pyautogui.press('win',interval=0.5)
    pyautogui.write('zoom')
    pyautogui.press('enter',interval=0.5)
    time.sleep(5)
    x,y = pyautogui.locateCenterOnScreen('join.png', confidence = 0.8)
    pyautogui.click(x,y)
    pyautogui.press('enter',interval=5)
    pyautogui.write(meetId)
    pyautogui.press('enter',interval=5)
    pyautogui.write(password)
    pyautogui.press('enter',interval = 10)
    pyautogui.hotkey('alt','f4')
    time.sleep(0.5)
    pyautogui.hotkey('alt','f4')
if __name__ == "__main__":
    attendZoom()
