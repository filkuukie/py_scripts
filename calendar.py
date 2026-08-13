import calendar 
import keyboard
import os
from datetime import datetime

yy = int(datetime.now().strftime('%Y'))
mm = int(datetime.now().strftime('%m'))
print(calendar.month(yy, mm))
today = datetime.today().strftime('%Y-%m-%d')
print(f"Today is: {today}")

while True:
    if keyboard.read_key() == "a":
        yy +=1
        os.system('cls')
        print(calendar.month(yy, mm))
        print(f"Today is: {today}")
    elif keyboard.read_key() == "d":
        yy -=1
        os.system('cls')
        print(calendar.month(yy, mm))
        print(f"Today is: {today}")
    elif keyboard.read_key() == "w":
        if mm == 12:
            os.system('cls')
            print(calendar.month(yy, mm))
            print(f"Today is: {today}")
        if mm != 12:
            mm += 1   
            os.system('cls')
            print(calendar.month(yy, mm))   
            print(f"Today is: {today}")   
    elif keyboard.read_key() == "s":
        if mm == 1:
            mm = 1
            os.system('cls')
            print(calendar.month(yy, mm))   
            print(f"Today is: {today}")
        if mm != 1:
            mm -= 1
            os.system('cls')
            print(calendar.month(yy, mm))
            print(f"Today is: {today}")