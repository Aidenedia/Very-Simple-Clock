from datetime import datetime
import time
import os 

while True:
    os.system("cls")
    currenttime = datetime.now()
    print(currenttime.strftime("%H:%M:%S"))
    time.sleep(1)
