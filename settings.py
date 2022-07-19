from tkinter import *


class Settings:

    def __init__(self, root):
        self.newWindow = Toplevel(root)
        self.newWindow.geometry("500x500")
        self.newWindow.resizable(1, 1)
        self.newWindow.title("Settings")
