from tkinter import IntVar, Toplevel, ttk
from tkinter.constants import BOTTOM, CENTER, LEFT, RIGHT, TOP
from app.gameservice import Service

class GameWindow:
    def __init__(self, window, app):
        self.app = app
        self.frame = ttk.LabelFrame(window,
                                    width=600,
                                    height=650,
                                    borderwidth=0)
        self.timer_on = False

    def _widgets(self):
        self._initialize_timer_widget()
        self._initialize_start_button()
        self._initialize_stop_button()
        self._initialize_target_label()
        self._initialize_textbox()
        self.frame.grid_rowconfigure(1,weight=0)
        self.frame.grid_rowconfigure(2,weight=0)
        self.frame.grid_rowconfigure(3,weight=0)
        self.frame.grid_rowconfigure(4,weight=0)

    def _initialize_start_button(self):
        self.startbutton = ttk.Button(self.frame,
                            text ="Aloita",
                            command = self._start_timer)
        self.startbutton.grid(row=2, column=2,pady=25)

    def _initialize_stop_button(self):
        self.stopbutton = ttk.Button(self.frame,
                            text = "Pysäytä",
                            command = self._stop_timer)

    def _initialize_timer_widget(self):
        timer_frame = ttk.Labelframe(self.frame,
                                     width=550,
                                     height=240,
                                     text="Ajastin")
        timer_frame.grid(row=1,column=2,padx=25, pady=10)
        timer_frame.grid_propagate(0)
        self.timer_minutes = IntVar()
        self.timer_minutes.set(60)
        self.timer_seconds = IntVar()
        self.timer_seconds.set(10)

        self.timer_minute_label = ttk.Label(timer_frame,
                               textvariable= self.timer_minutes,
                               padding=15,
                               justify=LEFT)
        self.timer_minute_label.config(font=("Helvetica",130))

        self.timer_second_label = ttk.Label(timer_frame,
                               textvariable= self.timer_seconds,
                               padding=15,
                               justify=RIGHT)
        self.timer_second_label.config(font=("Helvetica",130))

        self.timer_label = ttk.Label(timer_frame,
                               text= ":",
                               padding=20,
                               justify=CENTER)
        self.timer_label.config(font=("Helvetica",130))

        self.timer_minute_label.grid(row=1, column=1)
        self.timer_label.grid(row=1, column=2)
        self.timer_second_label.grid(row=1, column=3)
        
    def _initialize_target_label(self):
        self.target_frame = ttk.Labelframe(self.frame,
                                      width=200,
                                      height=70,
                                      text="Kohdepelaaja:",
                                      padding=15)
        
        self.target_frame.grid(row=3, column=2,pady=10)

    def _initialize_textbox(self):
        self.text_frame = ttk.Labelframe(self.frame,
                               width=300,
                               height=150,
                               text= "Juoman ottavat pelaajat:")
        self.text_frame.grid(row=4,column=2)

    def _update_timer(self):
        if self.timer_on == False:
            return
        new_time = self.timer_seconds.get() - 1
        self.timer_seconds.set(new_time)
        if self.timer_seconds.get() <= 0:
            if self.timer_minutes.get() <= 0:
                self.timer_on == False
                return
            self.timer_minutes.set(self.timer_minutes.get() -1)
            self.timer_seconds.set(59)
            self._update_target_player(self.app.target())
            self._choose(self.timer_minutes.get())
            self._drink(self.app.drink_select())
            
        self.frame.after(1000,self._update_timer)

    def _start_timer(self):
        if self.app.check_players() == True:
            self.timer_on = True
            self.startbutton.grid_forget()
            self.stopbutton.grid(row=2, column=2,pady=25)
            self._update_timer()
        else:
            error_label = ttk.Label(self.frame,
                                    text= "Lisää vähintään 3 pelaajaa!")
            error_label.grid(row=7,column=2)
            self.frame.after(5000,error_label.grid_forget)

    def _stop_timer(self):
        self.timer_on = False
        self.stopbutton.grid_forget()
        self.startbutton.configure(text="Jatka")
        self.startbutton.grid(row=2, column=2,pady=25)

    def _drink(self, message):
        drink_label = ttk.Label(self.text_frame,
                                     text= message,
                                     wraplength=250,
                                     justify= CENTER)
        drink_label.config(font= ("Helvetica",20))
        drink_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.frame.after(10000, drink_label.place_forget)
        
    def _update_target_player(self, player):
        self.target_label = ttk.Label(self.target_frame,
                         text= player,
                         wraplength=175,
                         justify= CENTER)
        self.target_label.config(font=("Helvetica", 20))
        self.target_label.place(relx=0.5, rely=0.4, anchor=CENTER)
        
    def _choose(self,minutes):
        if minutes in self.app.task_times:
            self._task_window()
        elif minutes in self.app.curse_times:
            self._curse_window()

    def _task_window(self):
        self._stop_timer()
        task = self.app.task_random()
        new_window = Toplevel()
        new_window.geometry("300x350")
        new_window.title("Tehtävä!")
        task_label = ttk.Label(new_window,
                        text= task,
                        wraplength=250)
        task_label.pack(pady=15)
        task_label.configure(font=("Helvetica", 25))
        continue_button = ttk.Button(new_window,
                        text= "Jatka peliä",
                        command = lambda: [new_window.destroy(),self._start_timer()])
        continue_button.pack(side=BOTTOM,pady=10)
        
    def _curse_window(self):
        self._stop_timer()
        curse = self.app.curse_random()
        new_window = Toplevel()
        new_window.geometry("300x250")
        new_window.title("Kirous!")
        curse_label = ttk.Label(new_window,
                        text= curse,
                        wraplength=250)
        curse_label.pack(pady=15)
        curse_label.configure(font=("Helvetica", 25))
        continue_button = ttk.Button(new_window,
                        text= "Jatka peliä",
                        command = lambda: [new_window.destroy(),self._start_timer()])
        continue_button.pack(side=BOTTOM,pady=10)

    def initialize_gamewindow(self):
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.grid_propagate(0)
        self._widgets()
        
    def show_frame(self):
        self.frame.tkraise()
        
    def hide(self):
        self.frame.pack_forget()