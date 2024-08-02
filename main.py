from customtkinter import *
from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
DARK_GREEN = "#379B46"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.configure(text="Timer")
    check_marks.configure(text="")
    global reps
    reps = 0


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        title.configure(text="Long Break", text_color=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title.configure(text="Short Break", text_color=PINK)
    else:
        countdown(work_sec)
        title.configure(text="Work", text_color=DARK_GREEN)


def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for n in range(math.floor(reps / 2)):
            marks += "✔"
        check_marks.configure(text=marks)


window = CTk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(column=1, row=1)

title = CTkLabel(master=window, text="Pomodoro Timer", fg_color=YELLOW, font=(FONT_NAME, 35, "bold"), text_color=GREEN)
title.grid(column=1, row=0)

start_button = CTkButton(master=window, text="Start", corner_radius=32, fg_color=GREEN, hover_color="white",
                         text_color=RED, font=(FONT_NAME, 20, "bold"), bg_color=YELLOW, command=start_timer)
start_button.grid(column=0, row=3)

reset_button = CTkButton(master=window, text="Reset", corner_radius=32, fg_color=GREEN, hover_color="white",
                         text_color=RED, font=(FONT_NAME, 20, "bold"), bg_color=YELLOW, command=reset_timer)
reset_button.grid(column=3, row=3)

check_marks = CTkLabel(master=window, text="", text_color=GREEN, font=(FONT_NAME, 26, "bold"), bg_color=YELLOW)
check_marks.grid(column=1, row=4)

window.mainloop()
