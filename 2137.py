import datetime
import time
from winotify import Notification, audio
dt = datetime.datetime.now()
check=True

while check:
    if dt.strftime("%H:%M") == "21:37":
        app = Notification(app_id="Papież Notifier",
                     title="Uwaga!",
                     msg="Nastała godzina 21:37",
                     duration="long")

        app.set_audio(audio.Default, loop=False)

        app.add_actions(label="JP2GMD", launch="https://www.youtube.com/watch?v=0qzLRlQFFQ4")

        app.show()
        check= False
    time.sleep(2)