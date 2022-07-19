from tkinter import *


class Stopwatch:

    t = "00:00:00"
    count = 0

    def __init__(self, root):

        self.newWindow = Toplevel(root)
        self.newWindow.geometry("500x500")
        self.newWindow.resizable(1, 1)
        self.newWindow.title("Stopwatch")

        self.mark = Label(self.newWindow,
                     font=("calibri", 40, "bold"),
                     pady=50,
                     foreground="black")
        self.mark.pack(anchor="center")
        self.mark.config(text=self.t)

        buttons_frame = Frame(self.newWindow)
        buttons_frame.pack(side=TOP)
        start_bt = Button(buttons_frame, text="Start", command=self.start)
        start_bt.pack(side=LEFT, padx=50)
        stop_bt = Button(buttons_frame, text="Stop", command=self.stop)
        stop_bt.pack(side=LEFT, padx=50)
        reset_bt = Button(buttons_frame, text="Reset", command=self.reset)
        reset_bt.pack(side=LEFT, padx=50)

        bottom_frame = Frame(self.newWindow)
        bottom_frame.pack(side=BOTTOM)
        close_bt = Button(bottom_frame, text="Close", command=self.close)
        close_bt.pack(side=BOTTOM, pady=2)

    def reset(self):
        self.count = 1
        self.t = "00:00:00"
        self.mark.config(text=self.t)

    def start(self):
        self.count = 0
        self.timer()

    def stop(self):
        self.count = 1

    def close(self):
        self.newWindow.destroy()

    def timer(self):

        if self.count == 0:
            h, m, s = map(int, self.t.split(":"))
            h = int(h)
            m = int(m)
            s = int(s)

            if s < 59:
                s += 1
            elif s == 59:
                s = 0
                if m < 59:
                    m += 1
                elif m == 59:
                    m = 0
                    h += 1

            if h < 10:
                h = str(0) + str(h)
            else:
                h = str(h)

            if m < 10:
                m = str(0) + str(m)
            else:
                m = str(m)

            if s < 10:
                s = str(0) + str(s)
            else:
                s = str(s)

            elapsed = h + ":" + m + ":" + s
            self.t = elapsed
            self.mark.config(text=elapsed)
            self.mark.after(1000, self.timer)
