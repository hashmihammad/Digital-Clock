import tkinter as tk
import time

root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x150")
root.configure(bg="#1c1c1c")

clock_label = tk.Label(root, font=('Segoe UI', 40, 'bold'), bg="#1c1c1c", fg="#00FFCC")
clock_label.pack(expand=True)

def update_clock():
    current_time = time.strftime("%I:%M:%S %p")
    clock_label.config(text=current_time)
    root.after(1000, update_clock)

update_clock()
root.mainloop()
