from tkinter import IntVar, StringVar, Toplevel, ttk
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
        #self.update_target_player(self.app.target())
        self._initialize_textbox()
        self.frame.grid_rowconfigure(1,weight=0)
        self.frame.grid_rowconfigure(2,weight=0)
        self.frame.grid_rowconfigure(3,weight=0)
        self.frame.grid_rowconfigure(4,weight=0)

    def _initialize_start_button(self):
        self.startbutton = ttk.Button(self.frame,
                            text ="Aloita",
                            command = self.start_timer)
        self.startbutton.grid(row=2, column=2,pady=25)

    def _initialize_stop_button(self):
        self.stopbutton = ttk.Button(self.frame,
                            text = "Pysäytä",
                            command = self.stop_timer)

    def _initialize_timer_widget(self):
        timer_frame = ttk.Labelframe(self.frame,
                                     width=550,
                                     height=240,
                                     text="Ajastin")
        timer_frame.grid(row=1,column=2,padx=25, pady=10)
        timer_frame.grid_propagate(0)
        self.timer_minutes = IntVar()
        self.timer_minutes.set(59)
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

    def update_timer(self):
        if self.timer_on == False:
            return
        new_time = self.timer_seconds.get() - 1
        self.timer_seconds.set(new_time)
        if self.timer_seconds.get() <= 0:
            if self.timer_minutes.get() <= 0:
                return
            self.timer_minutes.set(self.timer_minutes.get() -1)
            self.timer_seconds.set(59)
            self.update_target_player(self.app.target())
            self.drink(self.app.drink_select())
        self.frame.after(1000,self.update_timer)

    def start_timer(self):
        if self.app.check_players() == True:
            self.timer_on = True
            self.startbutton.grid_forget()
            self.stopbutton.grid(row=2, column=2,pady=25)
            self.update_timer()
        else:
            error_label = ttk.Label(self.frame,
                                    text= "Lisää vähintään 3 pelaajaa!")
            error_label.grid(row=7,column=2)
            self.frame.after(5000,error_label.grid_forget)

    def stop_timer(self):
        self.timer_on = False
        self.stopbutton.grid_forget()
        self.startbutton.configure(text="Jatka")
        self.startbutton.grid(row=2, column=2,pady=25)

    def drink(self, message):
        drink_label = ttk.Label(self.text_frame,
                                     text= message,
                                     wraplength=250,
                                     justify= CENTER)
        drink_label.config(font= ("Helvetica",20))
        drink_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.frame.after(10000, drink_label.place_forget)
        
    def update_target_player(self, player):
        self.target_label = ttk.Label(self.target_frame,
                         text= player,
                         wraplength=175,
                         justify= CENTER)
        self.target_label.config(font=("Helvetica", 20))
        self.target_label.place(relx=0.5, rely=0.4, anchor=CENTER)

    def task_window(self):
        self.stop_timer()
        new_window = Toplevel()
        new_window.geometry("250x200")
        new_window.title("Tehtävä!")
        task = ttk.Label(new_window,
                        text= "bruh")
        task.pack(pady=15)
        continue_button = ttk.Button(new_window,
                        text= "Jatka peliä",
                        command = lambda: [new_window.destroy(),self.start_timer()])
        continue_button.pack(side=BOTTOM,pady=10)

    def initialize_gamewindow(self):
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.grid_propagate(0)
        self._widgets()
        
    def show_frame(self):
        self.frame.tkraise()
        
    def hide(self):
        self.frame.pack_forget()