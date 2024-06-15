# I used the source code from Achudnova with minor modifications

import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import ttk, Style #L1: python -m pip install ttkbootstrap

#Let user choose the time for work & break in terminal
val1 = int(input("Your time for work (50 or 25): "))
val2 = int(input("Your time for break (5 or 10): "))

# Set the default time for work and break intervals
WORK_TIME = val1 * 60  #50mins work
SHORT_BREAK_TIME = val2 * 60 # 10mins break
LONG_BREAK_TIME = 15 * 60

class PomodoroTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x300")
        self.root.title("Pomodoro Timer")
        self.style = Style(theme="simplex")
        self.style.theme_use()

        self.timer_label = tk.Label(self.root, text="", font=("TkDefaultFont", 40))
        self.timer_label.pack(pady=20)

        #Start button
        self.start_button = ttk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=5)

        #Stop button
        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stop_timer,
                                      state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        #initialise timer settings
        self.work_time, self.break_time = WORK_TIME, SHORT_BREAK_TIME
        self.is_work_time, self.pomodoros_completed,  = True, 0 
        self.is_running = False

        #activate the loop
        self.root.mainloop()

    def start_timer(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.is_running = True
        self.update_timer()
    
    def stop_timer(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.is_running = False

    def update_timer(self):
        if self.is_running:
            if self.is_work_time:
                self.work_time -= 1
                if self.work_time == 0:
                    self.is_work_time = False
                    self.pomodoros_completed += 1 # count the complete pomodoro
                    self.break_time = LONG_BREAK_TIME if self.pomodoros_completed % 4 == 0 else SHORT_BREAK_TIME
                    messagebox.showinfo("Great job!" 
                                        if self.pomodoros_completed % 4 == 0
                                        else "Good job!", "Take a long break and rest your mind."
                                        
                                        if self.pomodoros_completed % 4 == 0
                                        else "Take a short break and strech your legs!")
            else:
                self.break_time -= 1 #count the complete break
                if self.break_time == 0: #when break time's up, start the work time
                    messagebox.showinfo("Time's up", "Get back to work!")
                    self.is_work_time, self.work_time = True, WORK_TIME
            
                    minutes, seconds = divmod(self.work_time 
                        if self.is_work_time else self.break_time, 60) 
            
                self.timer_label.config(text="{:03d}:{:03d}".format(minutes, seconds))
                self.root.after(1000, self.update_timer) #update the timer after 1 second 

PomodoroTimer()