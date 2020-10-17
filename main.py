import pyautogui 
#import schedule
from datetime import datetime 
import time 
import pandas as pd
# meetId = "Replace this with Meeting ID"
# password = "Replace this with Password"

df = pd.read_csv('class_schedule.csv')
pd_df = pd.DataFrame()


def attendZoom():
    while(True):
        time_str = datetime.now().strftime("%H:%M")

        if time_str in df.Time.values:
            pd_df = df[df['Time'].astype(str).str.contains(time_str)]

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
            pyautogui.write(pd_df.iloc[0,1])

            pyautogui.press('enter',interval=5)
            pyautogui.write(str(int(pd_df.iloc[0,2])))

            pyautogui.press('enter',interval = 10)
            pyautogui.hotkey('alt','f4')

            time.sleep(0.5)
            pyautogui.hotkey('alt','f4')




if __name__ == "__main__":
    attendZoom()

    # time.sleep(0.2)

    # pyautogui.press('esc',interval=0.1)
    # time.sleep(0.3)

    # pyautogui.press('win',interval=0.5)
    # pyautogui.write('zoom')

    # pyautogui.press('enter',interval=0.5)
    # time.sleep(5)

    # x,y = pyautogui.locateCenterOnScreen('join.png', confidence = 0.8)
    # pyautogui.click(x,y)

    # pyautogui.press('enter',interval=5)
    # pyautogui.write(meetId)

    # pyautogui.press('enter',interval=5)
    # pyautogui.write(password)

    # pyautogui.press('enter',interval = 10)
    # pyautogui.hotkey('alt','f4')

    # time.sleep(0.5)
    # pyautogui.hotkey('alt','f4')