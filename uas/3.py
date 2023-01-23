import tkinter as tk

def on_button_click():
    label.config(text="Hallo, Dian syamdova")

root = tk.Tk()

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

label = tk.Label(root, text="Welcome to Tkinter!")
label.pack()

root.mainloop()