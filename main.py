import time
import pyautogui
import datetime

def run():
    comments = open('comments.txt', "r", encoding="UTF8")
    commentLines = comments.readlines()

    for commentLine in commentLines:
        pyautogui.typewrite(commentLine)
        pyautogui.press("enter")
        print("Posted Comment " + commentLine
              )
        time.sleep(3)

run()
