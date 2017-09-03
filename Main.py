import os
from datetime import datetime
import time
import threading

#Pylapse v1.0

Time_sleep=2
Number_str=1
def startup():
    print("-----------------------------------------------------")
    print("Pylapse OSX v0.1 https://github.com/Acollie/Py-lapse")
    print("You are responsle for any damage done by this program")
    print("-----------------------------------------------------")
    try:
        os.mkdir("Screenshots")

    except:
        print("Screenhots file already exists")

    os.chdir("Screenshots")

    Start=input("Start program yes/no \n")


    if Start=="yes" or Start=="y":
        print("ok boss thread started")
        print("Thread start ="+ datetime.now().strftime('%H:%M:%S'))
        threads = []
        Number_str = 0

        t = threading.Thread(target=sceencapfuc(),args=())
        t.start()
        kill = input("press q to quit")
        if kill == 'q':
            quit()


    else:

        print("exiting program \n")
        print("Thread end ="+ datetime.now().strftime('%H:%M:%S'))



def sceencapfuc():
    Time_sleep = input("Please select number interval in seconds \n")



    Time_sleep=int(Time_sleep)
    Number_str=1

    i=10
    while i==10:

        time.sleep(Time_sleep)
        Number_str = str(Number_str)
        os.system("screencapture -x test"+Number_str+ ".png")
        Number_str=int(Number_str)
        Number_str+=1

    sceencapfuc()



startup()

