from tkinter import Tk, ttk
from tkinter.constants import BOTTOM
from ui.startwindow import StartWindow
from ui.gamewindow import GameWindow
from app.gameservice import Service

class UI:
    def __init__(self):
        self.app = Service()
        self.window = Tk()
        self.startwindow = StartWindow(self.window, self.app)
        self.gamewindow = GameWindow(self.window, self.app)
        
    def _initialize_start(self):
        self.startwindow.initialize_startwindow()
        
    def _initialize_game(self):
        self.gamewindow.initialize_gamewindow()
        
    def _show_start(self):
        self.startwindow.show_frame()
        
    def _show_game(self):
        self.gamewindow.show_frame()
    
    def _navigation_button(self):
        button = ttk.Button(self.window,
                            text= "Eteenpäin",
                            command= lambda: [self._show_game(), button.grid_forget(), button2.grid()])
        button.grid(row=1)
        
        button2 =ttk.Button(self.window,
                            text= "Takaisin",
                            command= lambda: [self._show_start(), button2.grid_forget(), button.grid()])    
    
    def initialize(self):
        self.window.geometry("600x750")
        self.window.title("PowerHour")
        self.window.resizable(False, False)
        self._navigation_button()
        self._initialize_start()
        self._initialize_game()
        self._show_start()
        self.app.spread_task_times()
        self.app.spread_curse_times()
        self.window.mainloop()
        
    
        