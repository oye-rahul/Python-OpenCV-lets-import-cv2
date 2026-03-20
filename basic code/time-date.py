import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=('Arial', 48))
label.pack()

def time():
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000,time)
label = tk.Label(root, font=('Digital-7', 40), bg='black', fg='lime')
label.pack(anchor='center')

time()
root.mainloop()