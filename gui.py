# gui
from tkinter import *
import logic

class Gui:
    def __init__(self, window):
        # Construct initial window
        self.window = window
        self.frame_shape = Frame(self.window)