from tkinter import Tk, Toplevel, ttk
from tkinter.constants import BOTTOM
from ui.startwindow import StartWindow
from ui.gamewindow import GameWindow
from app.gameservice import Service

class UI:
    """Luokka, joka hallitsee sovelluksen kahta peli-ikkunaa
    
    Attributes:
        app: Pelin sovelluslogiikan luokka.
        window: Ikkuna, jonka päälle luokka laittaa kahden ikkunan kehykset (frame).
        startwindow: Pelin aloitusikkuna.
        gamewindow: Pelin varsinainen ikkuna, jossa pelaaminen tapahtuu.
     
    """
    
    def __init__(self):
        """Luokan konstruktori, joka luo sovelluksen käyttöliittymän
        
        """
        
        self.app = Service()
        self.window = Tk()
        self.startwindow = StartWindow(self.window, self.app)
        self.gamewindow = GameWindow(self.window, self.app)
        
    def _initialize_start(self):
        """Alustaa sovelluksen aloitusikkunan kutsumalla startwindow -luokan metodia, joka rakentaa kehyksen sisältäen siihen liittyvät widgetit.
        
        """
        
        self.startwindow.initialize_startwindow()
        
    def _initialize_game(self):
        """Alustaa sovelluksen varsinaisen peli-ikkunan kutsumalla gamewindow -luokan metodia, joka rakentaa kehyksen sisältäen siihen liittyvät widgetit.
        
        """
        
        self.gamewindow.initialize_gamewindow()
        
    def _show_start(self):
        """Nostaa aloitusikkunan kehyksen päällimmäiseksi käyttäjän näkyville.
        
        """
        
        self.startwindow.show_frame()
        
    def _show_game(self):
        """Nostaa peli-ikkunan kehyksen päällimmäiseksi käyttäjän näkyville.
        
        """
        
        self.gamewindow.show_frame()
    
    def _navigation_button(self):
        """Tämän luokan kannalta ainoa ns "liikkuva osa"
        
        Nappi, jonka avulla voidaan vaihdella ikkunan näkymää aloitus- ja peli-ikkunan välillä.
        """
        
        option_button = ttk.Button(self.window,
                                   text="Peliasetukset",
                                   command= self._options_window)
        option_button.grid(row=1, pady=20)
        
        button = ttk.Button(self.window,
                            text= "Eteenpäin",
                            command= lambda: [self._show_game(),
                                              button.grid_forget(), option_button.grid_forget(), button2.grid(row=2, pady=20)])
        button.grid(row=2)
        
        button2 =ttk.Button(self.window,
                            text= "Takaisin",
                            command= lambda: [self._show_start(), self.gamewindow._stop_timer(),
                                              button2.grid_forget(), option_button.grid(row=1,pady=20), button.grid(row=2)])
        
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
                                         command= lambda: [self._handle_task_entry()])
        curse_button = ttk.Button(entry_frame,
                                         text= "Lisää kirous",
                                         command= lambda: [self._handle_curse_entry()])
        
        task_delete = ttk.Button(entry_frame,
                                 text= "Poista viimeisin tehtävä",
                                 command= lambda: [self._handle_last_task_delete()])
        
        curse_delete = ttk.Button(entry_frame,
                                 text= "Poista viimeisin kirous",
                                 command= lambda: [self._handle_last_curse_delete()])
        
        error_frame = ttk.Labelframe(new_window,
                                     width=200,
                                     height=50)
        
        entry_frame.pack(pady=10, padx=10)
        self.taskcurse_entry.pack(pady=10)
        task_button.pack(pady=10)
        curse_button.pack(pady=10)
        task_delete.pack(pady=10)
        curse_delete.pack(pady=10)
        error_frame.pack(pady=10)
        
        continue_button = ttk.Button(new_window,
                        text= "Takaisin",
                        command = lambda: [new_window.destroy()])
        
        modeframe.pack(padx=40, pady=20)
        modebutton1.pack(pady=10, padx=20)
        modebutton2.pack(pady=10, padx=20)
        continue_button.pack(side=BOTTOM,pady=10)
        
    def _handle_task_entry(self):
        task = self.taskcurse_entry.get()
        self.app.write_task(task)
        self.taskcurse_entry.delete(0, "end")
    
    def _handle_curse_entry(self):
        curse = self.taskcurse_entry.get()
        self.app.write_curse(curse)
        self.taskcurse_entry.delete(0, "end")
        
    def _handle_last_task_delete(self):
        print(self.app.delete_last_task())
        
    def _handle_last_curse_delete(self):
        print(self.app.delete_last_curse())
    
    def initialize(self):
        """Funktio, joka alustaa pelin varsinaisen ikkunan, jonka päälle rakennetaan aloitus- ja peli-ikkunoiden kehykset.
        
        """
        
        self.window.geometry("600x750")
        self.window.title("PowerHour")
        self.window.resizable(False, False)
        self._navigation_button()
        self._initialize_start()
        self._initialize_game()
        self._show_start()
        self.app.spread_task_times(60)
        self.app.spread_curse_times(60)
        self.window.mainloop()
        
    
        