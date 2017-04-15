import os
import time
import threading
import _thread

from tkinter import Tk, Label, Button

Sc_Number = 0
Start = 0



class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Py-Lapse")

        self.label = Label(master, text="Click for screen shots")
        self.label.pack()

        self.greet_button = Button(master, text="Screenshot", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Start Thread", command=self.Thread())
        self.close_button.pack()
    def greet(self):
        global Start
        Number_increase=1
        Start += Number_increase


        Number_str=str(Start)
        os.system("screencapture test"+Number_str+ ".png")
        print("Screenshot taken "+Number_str)

    def Screenshot(self):
        global Start
        Number_increase=1
        Start += Number_increase


        Number_str=str(Start)
        os.system("screencapture test"+Number_str+ ".png")
        print("Screenshot taken "+Number_str)
        return
    def Thread(self):
        print("test")



root = Tk()
my_gui = GUI(root)
root.mainloop()