from tkinter import *
from clock import Clock
from stopwatch import Stopwatch


def close():
    root.destroy()


def open_clock():
    clock_window = Clock(root)


def open_stopwatch():
    stopwatch_windows = Stopwatch(root)


root = Tk()
root.geometry("500x500")
root.resizable(1, 1)
root.title("Multi-function clock")

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

close_bt = Button(bottomFrame, text="Close", command=close)
close_bt.pack(pady=10)

clock_bt = Button(root, text="Clock", command=open_clock)
clock_bt.pack(pady=10)

stopwatch_bt = Button(root, text="Stopwatch", command=open_stopwatch)
stopwatch_bt.pack(pady=10)

mainloop()
