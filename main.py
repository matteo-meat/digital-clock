from tkinter import *
from clock import Clock
from stopwatch import Stopwatch
from settings import Settings


def close():
    root.destroy()


def open_clock():
    Clock(root)


def open_stopwatch():
    Stopwatch(root)


def open_settings():
    Settings(root)


root = Tk()
root.geometry("500x500")
root.resizable(1, 1)
root.title("Multi-function clock")

topFrame = Frame(root)
topFrame.pack(side=TOP)
clock_bt = Button(topFrame, text="Clock", command=open_clock)
clock_bt.pack(side=LEFT, padx=5, pady=10)
stopwatch_bt = Button(topFrame, text="Stopwatch", command=open_stopwatch)
stopwatch_bt.pack(side=LEFT, padx=5, pady=10)

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
settings_bt = Button(bottomFrame, text="Settings", command=open_settings)
settings_bt.pack(pady=10)
close_bt = Button(bottomFrame, text="Close", command=close)
close_bt.pack(pady=10)

mainloop()
