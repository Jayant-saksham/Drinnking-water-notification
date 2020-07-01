from plyer import notification
import time

while True:
    notification.notify(
        title='Jayant bhai, Please drink water',
        message='Reminder message from Python\nPani pii lo Jayant bhai\nWater is very important for our body',
        app_icon='D:\Your_folder\your_icon.ico',  # e.g. 'C:\\icon_32x32.ico'
        timeout=10,  # seconds
    )
    time.sleep(60*60)
