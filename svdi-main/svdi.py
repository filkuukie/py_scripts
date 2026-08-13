from pyvda import VirtualDesktop
from infi.systray import SysTrayIcon
from PIL import Image
import time

image= "null.ico"
systray = SysTrayIcon(image, "Systray")
systray.start()
while True:
    desk = VirtualDesktop.current()
    if desk.number==1:
        image= "one.ico"
        systray.update(icon=image)
    elif desk.number==2:
        image= "two.ico"
        systray.update(icon=image)
    elif desk.number==3:
        image= "three.ico"
        systray.update(icon=image)
    elif desk.number==4:
        image= "four.ico"
        systray.update(icon=image)
    elif desk.number==5:
        image= "five.ico"
        systray.update(icon=image)
    elif desk.number==6:
        image= "six.ico"
        systray.update(icon=image)
    elif desk.number==7:
        image= "seven.ico"
        systray.update(icon=image)
    elif desk.number==8:
        image= "eight.ico"
        systray.update(icon=image)
    elif desk.number==9:
        image= "nine.ico"
        systray.update(icon=image)
    else:
        image= "null.ico"
        systray.update(icon=image)
    time.sleep(1.5)
systray.shutdown()