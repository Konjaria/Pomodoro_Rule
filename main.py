from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#90B77D"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(Timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # It's time to work
        countdown(long_break_sec)
        label.config(text="Break", fg=RED)
    if reps % 2 == 0:
        countdown(short_break_sec)
        label.config(text="Break", fg=PINK)

    else:
        countdown(work_sec)
        label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_min = floor(count / 60)
    count_sec = count % 60
    timer = ""
    if count_min < 10:
        timer += f"0{count_min}"
    else:
        timer += f"{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
        timer += f":{count_sec}"
    else:
        timer += f":{count_sec}"
    canvas.itemconfig(timer_text, text=timer)
    if count > 0:
        global Timer
        Timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(floor(reps / 2)):
            mark += "✔ "
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Create a Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomodoro_pic)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

# Create a Label
label = Label(text="Timer",
              fg=GREEN,
              bg=YELLOW,
              font=(FONT_NAME, 35, "bold"))
label.grid(row=0, column=1)

# Buttons
Button(text="Start", command=start_timer, bg=GREEN, fg="black").grid(column=0, row=2)
Button(text="Reset", command=reset_timer, bg=GREEN, fg="black").grid(column=2, row=2)

# Check Mark
check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)
window.mainloop()
