from tkinter import ttk
from tkinter.constants import *
from app.gameservice import Service

class  StartWindow:
    def __init__(self, window):
        self.app = Service()
        self.frame = ttk.LabelFrame(window,
                                    width=600,
                                    height=650)
    
    def _widgets(self):
        self._title()
        self._initialize_player_entry()
        
    def _title(self):
        title = ttk.Label(self.frame,
                          text="PowerHour",
                          font=("Arial", 85))
        title.pack(side=TOP)
        
    def _initialize_player_entry(self):
        self.player_entry_button = ttk.Button(master= self.frame,
                                         text= "Lisää pelaajia",
                                         command= self._add_players_window)
        
        self.player_entry_button.pack()
        
    def _add_players_window(self):
        self.player_entry = ttk.Entry(master=self.frame,
                                      width= 30)
        
        player_entry_button = ttk.Button(master= self.frame,
                                         text= "Lisää pelaaja",
                                         command= self._handle_player_entry)
        
        self.player_entry.pack(pady=20)
        player_entry_button.pack(pady=10)
        
    def _handle_player_entry(self):
        player = self.player_entry.get()
        self.app.add_players(player)
        self.player_entry.delete(0, "end")
        player_added = ttk.Label(self.frame,
                                 text= f"{player} lisätty!")
        player_added.pack()
        self.frame.after(2000,player_added.pack_forget)
        
    def initialize_startwindow(self):
        self.frame.pack()
        self._widgets()
        
    def hide(self):
        self.frame.pack_forget()
