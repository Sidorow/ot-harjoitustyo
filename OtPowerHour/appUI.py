from tkinter import StringVar, IntVar, Tk, Toplevel , ttk
from tkinter.constants import BOTTOM

class UI():
    def __init__(self, root):
        self.root = root
        self.timer_minutes = IntVar()
        self.timer_minutes.set(59)
        self.timer_seconds = IntVar()
        self.timer_seconds.set(59)
        self.start_pause = StringVar()
        self.start_pause.set("Aloita")
        self.timer_on = False
        
    def widgets(self):
        self.timer_minute_label = ttk.Label(master=self.root,
                               textvariable= self.timer_minutes)
        self.timer_minute_label.config(font=("Arial",130))

        self.timer_second_label = ttk.Label(master=self.root,
                               textvariable= self.timer_seconds)
        self.timer_second_label.config(font=("Arial",130))
        
        self.timer_label = ttk.Label(master=self.root,
                               text=":")
        self.timer_label.config(font=("Arial",130))
        
        self.startbutton = ttk.Button(master=self.root,
                            text ="Aloita",
                            command = self.start_timer)
        self.stopbutton = ttk.Button(master=self.root,
                            text = "Pysäytä",
                            command = self.stop_timer)
        
        self.timer_minute_label.grid(row=1, column=1)
        self.timer_label.grid(row=1, column=2)
        self.timer_second_label.grid(row=1, column=3)
        self.startbutton.grid(row=3, column=2,pady=25)
        window.grid_rowconfigure(3,weight=0)
        window.grid_rowconfigure(1,weight=0)
    
    def update_timer(self):
        if not self.timer_on:
            return
        new_time = self.timer_seconds.get() - 1
        self.timer_seconds.set(new_time)
        if self.timer_seconds.get() <= 0:
            if self.timer_minutes.get() <= 0:
                return
            self.timer_minutes.set(self.timer_minutes.get() -1)
            self.timer_seconds.set(59)
            #self.drink(["Matti","Maija"])
            self.task_window("Jippii", "Kirous!")
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
        
    def drink(self, players):
        self.drink_label = ttk.Label(master=self.root,
                                     text= f"Pelaajat {players[0]} ja {players[1]} ottavat hörpsyndeeruksen :D",)
        self.drink_label.config(font= ("Arial",20))
        self.drink_label.grid()
        window.after(7500, self.drink_label.grid_forget)
    
    def task_window(self,message,type):
        self.stop_timer()
        new_window = Toplevel()
        new_window.geometry("250x200")
        new_window.title(type)
        task = ttk.Label(new_window,
                        text= message)
        task.pack(pady=15)
        ok = ttk.Button(new_window,
                        text= "Jatka peliä",
                        command = lambda: [new_window.destroy(),self.start_timer()])
        ok.pack(side=BOTTOM,pady=10)
        
        
window = Tk()
window.geometry("475x650")
window.title("PowerHour")

ui = UI(window)
ui.widgets()

window.mainloop()