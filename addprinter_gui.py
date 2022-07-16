import tkinter as tk
from tkinter import ttk, CENTER, DISABLED, NORMAL, RAISED, END

from Printer import Printer

def add_printer():

    if not ip.get() or not api_key.get() or not nozzle_size.get() or not color.get():
        print("A entry is empty")
        return

    if "http://" not in ip.get().lower():
        ip.set("http://" + ip.get())

    printer = Printer(ip.get(), api_key.get(), float(nozzle_size.get()), color.get())
    printer.upload()
    exit()




height = 125
width = 250

root = tk.Tk()
root.geometry(str(width) + "x" + str(height))
root.resizable(False, False)
root.title('Add Printer')

root.columnconfigure(3, weight=1)
root.rowconfigure(5, weight=1)

# ip, api_key, nozzle_size, color

# ip input
ip = tk.StringVar()
ip_entry = tk.Entry(root, textvariable=ip, font=('calibre', 10, 'normal'), width=25)

ip_entry.grid(row=0, column=2, columnspan=1)

# qty label
ip_label = tk.Label(root, text="IP", width=3)
ip_label.grid(row=0, column=3, sticky="", columnspan=1)

# api_key input
api_key = tk.StringVar()
api_key_entry = tk.Entry(root, textvariable=api_key, font=('calibre', 10, 'normal'), width=int(25))

api_key_entry.grid(row=1, column=2, columnspan=1)

# api_key label
api_key_label = tk.Label(root, text="api_key", width=5)
api_key_label.grid(row=1, column=3, sticky="", columnspan=1)

# nozzle_size input
nozzle_size = tk.StringVar()
nozzle_size_entry = tk.Entry(root, textvariable=nozzle_size, font=('calibre', 10, 'normal'), width=int(25))

nozzle_size_entry.grid(row=2, column=2, columnspan=1)

# nozzle_size label
nozzle_size_label = tk.Label(root, text="nozzle_size", width=10)
nozzle_size_label.grid(row=2, column=3, sticky="", columnspan=1)

# color input
color = tk.StringVar()
color_entry = tk.Entry(root, textvariable=color, font=('calibre', 10, 'normal'), width=int(25))

color_entry.grid(row=3, column=2, columnspan=1)

# color label
color_label = tk.Label(root, text="color", width=10)
color_label.grid(row=3, column=3, sticky="", columnspan=1)


# Add btn
add_btn = tk.Button(root, text="Create Printer", width=200, height=25, compound=CENTER,
                    command=add_printer)

add_btn.grid(row=4, column=2, columnspan=2, rowspan=2)


root.mainloop()

