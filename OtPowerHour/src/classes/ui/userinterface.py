from startwindow import StartWindow
from gamewindow import GameWindow
from app import gameservice
from tkinter import Tk

class UI:
    def __init__(self):
        self.window = Tk
        self.start = StartWindow()
        self.game = GameWindow()
        
    def initialize_start(self):
        self.start.initialize_startwindow(self.window)
        
ui = UI()
ui.initialize_start()
        