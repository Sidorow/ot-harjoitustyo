from tkinter import Grid, IntVar, StringVar, Tk, Toplevel , ttk
from tkinter.constants import BOTTOM, CENTER, COMMAND, LEFT, RIGHT, S
from app.gameservice import Service

class UI:
    def __init__(self, root):
        self.app = Service()
        self.root = root
        self.timer_on = False

    def widgets(self):
        self._initialize_timer_widget()
        self._initialize_start_button()
        self._initialize_stop_button()
        #self._initialize_textbox()
        self._initialize_player_entry()
        window.grid_rowconfigure(1,weight=0)
        window.grid_rowconfigure(2,weight=0)
        window.grid_rowconfigure(3,weight=0)
        window.grid_rowconfigure(4,weight=0)

    def _initialize_start_button(self):
        self.startbutton = ttk.Button(master=self.root,
                            text ="Aloita",
                            command = self.start_timer)
        self.startbutton.grid(row=3, column=2,pady=25)

    def _initialize_stop_button(self):
        self.stopbutton = ttk.Button(master=self.root,
                            text = "Pysäytä",
                            command = self.stop_timer)

    def _initialize_player_entry(self):
        self.player_entry = ttk.Entry(master=self.root,
                                      width= 20)

        self.player_entry_button = ttk.Button(master= self.root,
                                         text= "Lisää pelaaja",
                                         command= self._handle_player_entry)
        self.player_entry.grid(row=6, column= 2, pady=40)
        self.player_entry_button.grid(row=7,column=2,pady=5)

    def _handle_player_entry(self):
        player = self.player_entry.get()
        self.app.add_players(player)
        self.player_entry.delete(0, "end")

    def _initialize_timer_widget(self):
        self.timer_minutes = IntVar()
        self.timer_minutes.set(59)
        self.timer_seconds = IntVar()
        self.timer_seconds.set(59)

        self.timer_minute_label = ttk.Label(master=self.root,
                               textvariable= self.timer_minutes,
                               wraplength=200,
                               justify=LEFT)
        self.timer_minute_label.config(font=("Arial",130))

        self.timer_second_label = ttk.Label(master=self.root,
                               textvariable= self.timer_seconds,
                               wraplength=200,
                               justify=RIGHT)
        self.timer_second_label.config(font=("Arial",130))

        self.timer_label = ttk.Label(master=self.root,
                               text= ":",
                               wraplength=200,
                               justify=CENTER)
        self.timer_label.config(font=("Arial",130))

        self.timer_minute_label.grid(row=1, column=1)
        self.timer_label.grid(row=1, column=2)
        self.timer_second_label.grid(row=1, column=3)

    def _initialize_textbox(self):
        message = self.app.target()
        text = ttk.Label(master= self.root,
                         text= message,
                         wraplength=200)

        text.grid(row=4, column=2)

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
            self.drink(self.app.drink_select())
        window.after(1000,self.update_timer)

    def start_timer(self):
        self.timer_on = True
        self.startbutton.grid_forget()
        self.stopbutton.grid(row=3, column=2,pady=25)
        self.update_timer()

    def stop_timer(self):
        self.timer_on = False
        self.stopbutton.grid_forget()
        self.startbutton.configure(text="Jatka")
        self.startbutton.grid(row=3, column=2,pady=25)

    def drink(self, message):
        drink_label = ttk.Label(master=self.root,
                                     text= message,
                                     wraplength=200,
                                     justify= CENTER)
        drink_label.config(font= ("Arial",20))
        drink_label.grid(row=5, column=2, )
        window.after(10000, drink_label.grid_forget)

    def task_window(self):
        self.stop_timer()
        new_window = Toplevel()
        new_window.geometry("250x200")
        new_window.title(type)
        task = ttk.Label(new_window,
                        text= "bruh")
        task.pack(pady=15)
        continue_button = ttk.Button(new_window,
                        text= "Jatka peliä",
                        command = lambda: [new_window.destroy(),self.start_timer()])
        continue_button.pack(side=BOTTOM,pady=10)

    def initialize_gamewindow():
        window.geometry("575x650")
        window.maxsize(575,650)
        #window.grid_propagate(0)
        ui.widgets()
        window.title("PowerHour")
        window.resizable(False,False)
        window.mainloop()

window = Tk()
ui = UI(window)
UI.initialize_gamewindow()