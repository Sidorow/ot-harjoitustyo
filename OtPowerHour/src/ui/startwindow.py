from tkinter import ttk, Toplevel
from tkinter.constants import *
from app.gameservice import Service

class  StartWindow:
    def __init__(self, window, app, game):
        self.gamewindow = game
        self.app = app
        self.frame = ttk.LabelFrame(window,
                                    width=600,
                                    height=600,
                                    borderwidth=0)
    
    def _widgets(self):
        self._title()
        self._initialize_player_entry()
        self._initialize_options_button()
        
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
        player = self.player_entry.get().strip()
        if not player:
            return
        self.app.add_players(player)
        self.player_entry.delete(0, "end")
        player_added = ttk.Label(self.entry_frame,
                                 text= f"{player} lisätty!")
        player_added.pack()
        self.frame.after(1500,player_added.pack_forget)
    
    def _initialize_options_button(self):
        option_button = ttk.Button(self.frame,
                                   text="Peliasetukset",
                                   command= self._options_window)
        option_button.pack(pady=10)    
            
    def _options_window(self):
        new_window = Toplevel()
        new_window.title("Asetukset")
        modeframe = ttk.Labelframe(new_window,
                                   text= "Pelimoodi",
                                   padding= 10)
        modebutton1 = ttk.Button(modeframe,
                                      text= "60min moodi",
                                      command= lambda: [self.gamewindow._stop_timer(), self.gamewindow.timer_minutes.set(60), self.gamewindow.timer_seconds.set(10),
                                                        modebutton1.state(["pressed"]), modebutton2.state(["!pressed"])])
        modebutton2 = ttk.Button(modeframe,
                                      text= "30min moodi",
                                      command= lambda: [self.gamewindow._stop_timer(), self.gamewindow.timer_minutes.set(30), self.gamewindow.timer_seconds.set(10),
                                                        modebutton2.state(["pressed"]), modebutton1.state(["!pressed"])])
        
        entry_frame = ttk.Labelframe(new_window,
                                     height=200,
                                     width=300,
                                     text="Lisää tehtäviä/kirouksia",
                                     padding=10)
        
        self.taskcurse_entry = ttk.Entry(entry_frame,
                                      width= 30)

        task_button = ttk.Button(entry_frame,
                                         text= "Lisää tehtävä",
                                         command= lambda: [self._handle_task_entry(), self._info_label("Tehtävä lisätty!")])
        curse_button = ttk.Button(entry_frame,
                                         text= "Lisää kirous",
                                         command= lambda: [self._handle_curse_entry(), self._info_label("Kirous lisätty!")])
        
        task_delete = ttk.Button(entry_frame,
                                 text= "Poista viimeisin tehtävä",
                                 command= lambda: [self._handle_last_task_delete(), self._info_label("Viimeisin tehtävä poistettu!")])
        
        curse_delete = ttk.Button(entry_frame,
                                 text= "Poista viimeisin kirous",
                                 command= lambda: [self._handle_last_curse_delete(), self._info_label("Viimeisin kirous poistettu!")])
        
        self.info_frame = ttk.Labelframe(new_window,
                                     width=300,
                                     height=75,
                                     padding=10)
        
        entry_frame.pack(pady=10, padx=10)
        self.taskcurse_entry.pack(pady=10)
        task_button.pack(pady=10)
        curse_button.pack(pady=10)
        task_delete.pack(pady=10)
        curse_delete.pack(pady=10)
        self.info_frame.pack(pady=10,padx=10)
        
        continue_button = ttk.Button(new_window,
                        text= "Takaisin",
                        command = lambda: [new_window.destroy()])
        
        modeframe.pack(padx=40, pady=20)
        modebutton1.pack(pady=10, padx=20)
        modebutton2.pack(pady=10, padx=20)
        continue_button.pack(side=BOTTOM,pady=10)
        
    def _handle_task_entry(self):
        task = self.taskcurse_entry.get().strip()
        if not task:
            return
        self.app.write_task(task)
        self.taskcurse_entry.delete(0, "end")
    
    def _handle_curse_entry(self):
        curse = self.taskcurse_entry.get()
        self.app.write_curse(curse)
        self.taskcurse_entry.delete(0, "end")
        
    def _handle_last_task_delete(self):
        self.app.delete_last_task()
        
    def _handle_last_curse_delete(self):
        self.app.delete_last_curse()
        
    def _info_label(self, message):
        info = ttk.Label(self.info_frame,
                         text=message,
                         wraplength=250)
        info.place(x=135, y=10, anchor="center")
        info.after(2000, info.place_forget)
        
        
    def initialize_startwindow(self):
        self.frame.grid(row=0,column=0, sticky="nsew")
        self.frame.grid_propagate(0)
        self._widgets()
        
    def show_frame(self):
        self.frame.tkraise()
