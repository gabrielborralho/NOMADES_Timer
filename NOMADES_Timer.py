import time
import tkinter as tk
from tkinter import PhotoImage

counter = 1  # Adicionando um contador global


def check_continuous_timer():
    global continuous_elapsed_time, running
    if running:
        continuous_elapsed_time += 1
    continuous_minutes, continuous_seconds = divmod(
        continuous_elapsed_time, 60)
    continuous_time_str = f'Online: {int(continuous_minutes):02d}:{
        int(continuous_seconds):02d}'
    continuous_label.config(text=continuous_time_str)
    root.after(1000, check_continuous_timer)


def check_timer():
    global start_time, running, remaining_time, counter
    if running:
        current_time = time.time()
        elapsed_time = current_time - start_time
        remaining_time = max_countdown - elapsed_time

        if remaining_time <= 0:
            start_time = current_time
            remaining_time = max_countdown
            counter += 1  # Incrementando o contador ao zerar o temporizador
            print(f"Timer zerado {counter} vezes.")
    minutes, seconds = divmod(remaining_time, 60)
    time_str = f'Save: {int(minutes):02d}:{int(seconds):02d} ({int(counter)})'
    label.config(text=time_str)

    root.after(1000, check_timer)


def start_timer():
    global running, start_time
    running = True
    start_time = time.time()
    print('Start button pressed')


def pause_timer():
    global running
    running = not running
    print('Pause button pressed')


def reset_timer():
    global remaining_time, continuous_elapsed_time
    remaining_time = max_countdown
    continuous_elapsed_time = 0
    start_timer()
    print('Reset button pressed')


if __name__ == "__main__":
    root = tk.Tk()
    root.title("NOMADES Timer")
    root.attributes("-topmost", True)
    root.geometry('275x150')
    root.configure(bg='black')
    root.attributes("-alpha", 0.8)

    # Convertendo a imagem do ícone para o formato adequado
    icon = PhotoImage(file="images/icon.png")
    root.iconphoto(True, icon)

    label = tk.Label(root, fg='orange', bg='black', font=('Helvetica', 18))
    label.pack(pady=8)

    continuous_elapsed_time = 0
    continuous_label = tk.Label(
        root, fg='orange', bg='black', font=('Helvetica', 12))
    continuous_label.pack(pady=8)

    max_countdown = 15 * 60
    remaining_time = max_countdown
    start_time = time.time()
    running = True

    check_timer()
    check_continuous_timer()

    button_frame = tk.Frame(root, bg='black')
    button_frame.pack()

    start_img = PhotoImage(file="images/start_icon.png")
    start_button = tk.Button(button_frame, image=start_img, command=start_timer,
                             highlightthickness=0, highlightbackground='black', bd=0, bg='black', activebackground='orange')
    start_button.image = start_img
    start_button.pack(side='left', padx=8)

    pause_img = PhotoImage(file="images/pause_icon.png")
    pause_button = tk.Button(button_frame, image=pause_img, command=pause_timer,
                             highlightthickness=0, highlightbackground='black', bd=0, bg='black', activebackground='orange')
    pause_button.image = pause_img
    pause_button.pack(side='left', padx=8)

    reset_img = PhotoImage(file="images/reset_icon.png")
    reset_button = tk.Button(button_frame, image=reset_img, command=reset_timer,
                             highlightthickness=0, highlightbackground='black', bd=0, bg='black', activebackground='orange')
    reset_button.image = reset_img
    reset_button.pack(side='left', padx=8)

    root.mainloop()
