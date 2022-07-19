from tkinter import *
from time import strftime


class Clock:

    def __init__(self, root):
        self.newWindow = Toplevel(root)
        self.newWindow.geometry("500x500")
        self.newWindow.resizable(1, 1)
        self.newWindow.title("Digital clock")

        self.mark = Label(self.newWindow,
                          font=("calibri", 40, "bold"),
                          pady=150,
                          foreground="black")
        self.mark.pack(anchor="center")

        close_bt = Button(self.newWindow, text="Close", command=self.close)
        close_bt.pack(pady=10)
        self.time()

    def time(self):
        date_time = strftime("%A, %d %B %Y\n"
                             "%H:%M:%S")
        self.mark.config(text=date_time)
        self.mark.after(1000, self.time)  # calls "time" function after 1000ms (1s)

    def close(self):
        self.newWindow.destroy()
