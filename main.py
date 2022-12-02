from tkinter import *
import math

PINK = "#F5D5AE"
RED = "#DBA39A"
GREEN = "#B3FFAE"
YELLOW = "#FFCACA"
BACKGROUND = "#372948"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
    

def start_timer():
    global reps 
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg = RED)
    
    elif reps % 2 ==0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg= PINK)
    else:
        count_down(work_sec)
        title_label.config(text ="Work", fg=GREEN)

        

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
        
        
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(0, reps/2)):
            marks += "✔️"
        check_marks.config(text = marks)   


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BACKGROUND)

canvas = Canvas(width = 200, height=223, bg=BACKGROUND, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


#? "Timer"
title_label = Label(text="Timer",bg=BACKGROUND ,fg=GREEN, font=(FONT_NAME, 50))
title_label.grid(column=1, row =0)

#? create a start and reset button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0 ,row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

#?check marks
check_marks = Label(foreground=GREEN, bg=BACKGROUND)
check_marks.grid(column=1, row=3)


window.mainloop()