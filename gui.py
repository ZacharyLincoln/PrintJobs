import glob
import os
import tkinter as tk
from tkinter import ttk, CENTER, DISABLED, NORMAL, RAISED, END

from File import File
from PrintJob import PrintJob
from Printer import Printer

printers = []

height = 500
width = 1000

root = tk.Tk()
root.geometry(str(width) + "x" + str(height))
root.resizable(False, False)
root.title('Printing Que')

pixelVirtual = tk.PhotoImage(width=1, height=1)

root.columnconfigure(5, weight=1)
root.rowconfigure(9, weight=1)

# Left section

left_width = 400

# gcode dir path input
gcode_dir_path = tk.StringVar()
gcode_dir_path.set("C:\\Users\\Zach\\Desktop")
gcode_dir_entry = tk.Entry(root, textvariable=gcode_dir_path, font=('calibre', 10, 'normal'),width=int(left_width/10))

gcode_dir_entry.grid(row=0, column=0, columnspan=2)

# gcode file tree
gcode_file_tree = ttk.Treeview(root, column=("c1", "c2"), show='headings', height=20)

gcode_file_tree.column("# 1", anchor=CENTER, width=int(left_width/2))
gcode_file_tree.heading("# 1", text="File Name")
gcode_file_tree.column("# 2", anchor=CENTER, width=int(left_width/2))
gcode_file_tree.heading("# 2", text="File Path")

def select_item(a):
    current_item = gcode_file_tree.focus()
    print(gcode_file_tree.item(current_item))


gcode_file_tree.bind('<ButtonRelease-1>', select_item)


gcode_file_tree.grid(row=1, column=0, columnspan=2, rowspan=7)

# refresh gcode s
def refresh_gcode_tree():
    for item in gcode_file_tree.get_children():
        gcode_file_tree.delete(item)

    for file_path in glob.glob(gcode_dir_path.get() + "\\*.gcode"):
        file_path = file_path.replace("\\", "\\\\")
        gcode_file_tree.insert('', 'end', text="100", values=(file_path.split("\\\\")[len(file_path.split("\\\\"))-1],file_path))
refresh_gcode_tree()

refresh_gcode_btn = tk.Button(root, text="Refresh", image=pixelVirtual, width=left_width, height=height/6, compound=CENTER, command=refresh_gcode_tree)

refresh_gcode_btn.grid(row=9, column=0, columnspan=2)


# Center section

center_width = 200

# qty input
qty = tk.StringVar()
qty_entry = tk.Entry(root, textvariable=qty, font=('calibre', 10, 'normal'), width=int(center_width/10))

qty_entry.grid(row=0, column=2, columnspan=1)

# qty label
qty_label = tk.Label(root, text="QTY", width=3)
qty_label.grid(row=0, column=3, sticky="", columnspan=1)

# color label
color_label = tk.Label(root, text="Color", width=4)
color_label.grid(row=1, column=2, sticky="", columnspan=1)

# color drop down
colors = ["Any"]
clicked_color = tk.StringVar()
clicked_color.set("Any")

color_drop_down = tk.OptionMenu(root, clicked_color, *colors)
color_drop_down.grid(row=1, column=3, sticky="", columnspan=1)

# nozzle label
nozzle_label = tk.Label(root, text="Nozzle", width=4)
nozzle_label.grid(row=2, column=2, sticky="", columnspan=1)

# nozzle drop down
nozzle = ["None"]
clicked_nozzle = tk.StringVar()
clicked_nozzle.set("None")

nozzle_drop_down = tk.OptionMenu(root, clicked_nozzle, *nozzle)
nozzle_drop_down.grid(row=2, column=3, sticky="", columnspan=1)


def add_print_job():
    # Check if color and nozzle is selected
    item_id = gcode_file_tree.focus()
    values = gcode_file_tree.item(item_id).get('values')

    if not item_id:
        print("Please select a print job")
        return

    if qty.get() == "" or clicked_color.get() == "" or clicked_nozzle.get() == "":
        print("Please enter a qty, color, and nozzle")
        return



    file = File(clicked_nozzle.get(), clicked_color.get(), local_path=values[1])

    for printer in Printer.download_all():
        file.upload_to_octoprint(printer)

    job = PrintJob(file)
    for i in range(int(qty.get())):
        job.upload()
        refresh_job_tree()




# Add btn
add_btn = tk.Button(root, text="Add --->", image=pixelVirtual, width=center_width, height=height/15, compound=CENTER, command=add_print_job)

add_btn.grid(row=3, column=2, columnspan=2)


def remove_print_job():
    item_id = job_tree.focus()
    values = job_tree.item(item_id).get('values')
    job_to_remove = PrintJob(File(values[2], values[1], octoprint_path="local/"+values[0]))
    job_to_remove.remove_from_database()
    refresh_job_tree()
    print(values)


# Remove print job btn
remove_btn = tk.Button(root, text="<--- Remove", image=pixelVirtual, width=center_width, height=height/15, compound=CENTER, command=remove_print_job)

remove_btn.grid(row=4, column=2, columnspan=2)




# Show log check box

def add_printer():
    os.system('addprinter_gui.py')

# Add printer btn
add_printer_btn = tk.Button(root, text="Add Printer", image=pixelVirtual, width=center_width, height=height/15, compound=CENTER, command=add_printer)

add_printer_btn.grid(row=6, column=2, columnspan=2)


def remove_printer():
    item_id = printer_tree.focus()
    values = printer_tree.item(item_id).get('values')
    Printer.remove_from_database(values[0], values[4], values[3])
    refresh_job_tree()
    print(values)

# Remove printer btn
remove_printer_btn = tk.Button(root, text="Remove Printer", image=pixelVirtual, width=center_width, height=height/15, compound=CENTER, command=remove_printer)

remove_printer_btn.grid(row=7, column=2, columnspan=2)


# Right section

right_width = 400


# gcode file tree
job_tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings', height=13)

job_tree.column("# 1", anchor=CENTER, width=int(left_width/3))
job_tree.heading("# 1", text="File Name")
job_tree.column("# 2", anchor=CENTER, width=int(left_width/3))
job_tree.heading("# 2", text="Color")
job_tree.column("# 3", anchor=CENTER, width=int(left_width/3))
job_tree.heading("# 3", text="Nozzle Size")

job_tree.grid(row=0, column=4, columnspan=2, rowspan=5)


printer_tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5"), show='headings', height=7)

printer_tree.column("# 1", anchor=CENTER, width=int(left_width/5))
printer_tree.heading("# 1", text="IP")
printer_tree.column("# 2", anchor=CENTER, width=int(left_width/5))
printer_tree.heading("# 2", text="Currently Printing")
printer_tree.column("# 3", anchor=CENTER, width=int(left_width/5))
printer_tree.heading("# 3", text="Bed Temp")
printer_tree.column("# 4", anchor=CENTER, width=int(left_width/5))
printer_tree.heading("# 4", text="Color")
printer_tree.column("# 5", anchor=CENTER, width=int(left_width/5))
printer_tree.heading("# 5", text="Nozzle Size")

printer_tree.grid(row=5, column=4, columnspan=2, rowspan=3)


# refresh jobs
def refresh_job_tree():
    colors = []
    nozzle = []

    for item in job_tree.get_children():
        job_tree.delete(item)
    print_jobs = PrintJob.download_all()

    for print_job in print_jobs:
        job_tree.insert('', 'end', text="100", values=(str(print_job.file.octoprint_path).replace("local/",""), print_job.file.color, print_job.file.nozzle_size))

    for item in printer_tree.get_children():
        printer_tree.delete(item)
    printers = Printer.download_all()

    for printer in printers:
        printer_tree.insert('', 'end', text="100", values=(str(printer.ip).replace("http://", ""), printer.is_printing(), printer.get_bed_temp(), printer.color, printer.nozzle_size))
        print(printer.color)
        if printer.color not in colors:
            colors.append(printer.color)

        if printer.nozzle_size not in nozzle:
            nozzle.append(printer.nozzle_size)

    print(nozzle)

    global color_drop_down
    global nozzle_drop_down

    color_drop_down = tk.OptionMenu(root, clicked_color, *colors)
    color_drop_down.grid(row=1, column=3, sticky="", columnspan=1)

    nozzle_drop_down = tk.OptionMenu(root, clicked_nozzle, *nozzle)
    nozzle_drop_down.grid(row=2, column=3, sticky="", columnspan=1)






refresh_job_tree()


# refresh jobs
refresh_job_btn = tk.Button(root, text="Refresh", image=pixelVirtual, width=left_width, height=height/6, compound=CENTER, command=refresh_job_tree)


refresh_job_btn.grid(row=9, column=4, columnspan=2)



# job tree

# job refresh btn



root.mainloop()
