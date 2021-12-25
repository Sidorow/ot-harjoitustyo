from tkinter import Tk, ttk
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
        self.gamewindow = GameWindow(self.window, self.app)
        self.startwindow = StartWindow(self.window, self.app, self.gamewindow)
        
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
        
        button = ttk.Button(self.window,
                            text= "Eteenpäin",
                            command= lambda: [self._show_game(),
                                              button.grid_forget(), button2.grid(row=2, pady=20)])
        button.grid(row=2, pady=20)
        
        button2 =ttk.Button(self.window,
                            text= "Takaisin",
                            command= lambda: [self._show_start(), self.gamewindow._stop_timer(),
                                              button2.grid_forget(), button.grid(row=2, pady=20)])
    
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
        self.app.spread_task_times()
        self.app.spread_curse_times()
        self.window.mainloop()
        
    
        