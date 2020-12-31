import pyautogui

spam = pyautogui.prompt('Print Spam content here XD') 
f_o_r = 1
longitude = int(pyautogui.prompt("You have been spammedEnter the number of times to be repeated")) 

while f_o_r < longitude: 
    f_o_r += 1
    pyautogui.typewrite(spam)
    pyautogui.press("enter")

