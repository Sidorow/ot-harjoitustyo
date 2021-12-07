from tkinter import Tk, ttk
from tkinter.constants import *
#from gamewindow import GameWindow
from app.gameservice import Service

class  StartWindow:
    def __init__(self, root):
        self.app = Service()
        self.root = root
    
    def widgets(self):
        self._title()
        self._initialize_player_entry()
        
    def _title(self):
        title = ttk.Label(master=self.root,
                          text="PowerHour",
                          font=("Arial", 85))
        title.pack(side=TOP)
        
    def _initialize_player_entry(self):
        self.player_entry = ttk.Entry(master=self.root,
                                      width= 30)

        self.player_entry_button = ttk.Button(master= self.root,
                                         text= "Lisää pelaaja",
                                         command= self._handle_player_entry)
        
        self.info_frame = ttk.Labelframe(master=self.root,
                                         width=200,
                                         height=100)
        self.player_entry.pack(pady=20)
        self.player_entry_button.pack(pady=20)
        self.info_frame.pack()

    def _handle_player_entry(self):
        player = self.player_entry.get()
        self.app.add_players(player)
        self.player_entry.delete(0, "end")
        
    def initialize_startwindow():
        window.geometry("600x650")
        #window.maxsize(600,650)
        #window.grid_propagate(0)
        ui.widgets()
        window.title("PowerHour")
        window.resizable(False,False)
        window.mainloop()
        
window = Tk()
ui = StartWindow(window)
StartWindow.initialize_startwindow()