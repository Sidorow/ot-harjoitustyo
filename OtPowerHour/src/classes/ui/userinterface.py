from tkinter import Tk, ttk
from tkinter.constants import BOTTOM
from ui.startwindow import StartWindow
from ui.gamewindow import GameWindow

class UI:
    def __init__(self):
        self.window = Tk()
        self.startwindow = StartWindow(self.window)
        self.gamewindow = GameWindow(self.window)
        
    def _show_start(self):
        self.startwindow.initialize_startwindow()
        
    def _show_game(self):
        self.gamewindow.initialize_gamewindow()
        
    def _hide_start(self):
        self.startwindow.hide()
        
    def _hide_game(self):
        self.gamewindow.hide()
    
    def _navigation_button(self):
        button = ttk.Button(self.window,
                            text= "Eteenpäin",
                            command= lambda: [self._hide_start(), self._show_game(), button.pack_forget(), button2.pack(side=BOTTOM,pady=15)])
        button.pack(side=BOTTOM,pady=15)
        
        button2 =ttk.Button(self.window,
                            text= "Takaisin",
                            command= lambda: [self._hide_game(), self._show_start(), button2.pack_forget(), button.pack(side=BOTTOM,pady=15)])    
    
    def initialize(self):
        self.window.geometry("600x750")
        self.window.title("PowerHour")
        self.window.resizable(False, False)
        self._navigation_button()
        self._show_start()
        self.window.mainloop()
        
    
        