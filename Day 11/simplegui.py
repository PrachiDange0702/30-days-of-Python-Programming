import tkinter as tk

def on_button_click():
    value = entry.get()
    label.config(text=value)

def on_checkbutton_click():
    if var.get() == 1:
        label.config(fg="red")
    else:
        label.config(fg="black")

# Create the main window
window = tk.Tk()
window.title("Simple GUI")

# Create a frame
frame = tk.Frame(window)
frame.pack(pady=10)

# Create an entry widget
entry = tk.Entry(frame, width=30)
entry.pack(side=tk.LEFT)

# Create a button widget
button = tk.Button(frame, text="Submit", command=on_button_click)
button.pack(side=tk.LEFT, padx=5)

# Create a checkbutton widget
var = tk.IntVar()
checkbutton = tk.Checkbutton(window, text="Change Label Color", variable=var, command=on_checkbutton_click)
checkbutton.pack()

# Create a label widget
label = tk.Label(window, text="Hello, World!")
label.pack(pady=10)

# Run the GUI
window.mainloop()
