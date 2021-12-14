from tkinter import ttk
from tkinter.constants import *
from app.gameservice import Service

class  StartWindow:
    def __init__(self, window, app):
        self.app = app
        self.frame = ttk.LabelFrame(window,
                                    width=600,
                                    height=650,
                                    borderwidth=0)
    
    def _widgets(self):
        self._title()
        self._initialize_player_entry()
        self._initialize_options()
        
    def _title(self):
        title = ttk.Label(self.frame,
                          text="PowerHour",
                          font=("Helvetica", 80),
                          padding=20)
        title.pack(side=TOP, fill=BOTH)
        title.pack_propagate(0)
        
    def _initialize_player_entry(self):
        self.entry_frame = ttk.Labelframe(self.frame,
                                     height=200,
                                     width=300,
                                     text="Lisää vähintään 3 pelaajaa",
                                     padding=10)
        self.player_entry = ttk.Entry(self.entry_frame,
                                      width= 30)

        player_entry_button = ttk.Button(self.entry_frame,
                                         text= "Lisää pelaaja",
                                         command= lambda: self._handle_player_entry())
        self.entry_frame.pack(pady=75)
        self.entry_frame.pack_propagate(0)
        self.player_entry.pack(pady=20)
        player_entry_button.pack(pady=10,side=BOTTOM)
        
    def _handle_player_entry(self):
        player = self.player_entry.get()
        self.app.add_players(player)
        self.player_entry.delete(0, "end")
        player_added = ttk.Label(self.entry_frame,
                                 text= f"{player} lisätty!")
        player_added.pack()
        self.frame.after(2000,player_added.pack_forget)
        
    def _initialize_options(self):
        option_button = ttk.Button(self.frame,
                                   text="Asetukset")
        option_button.pack(side=BOTTOM, pady=45)
        
    def initialize_startwindow(self):
        self.frame.grid(row=0,column=0, sticky="nsew")
        self.frame.grid_propagate(0)
        self._widgets()
        
    def show_frame(self):
        self.frame.tkraise()
