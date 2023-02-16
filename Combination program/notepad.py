#exe label and dynamic output from lot number
# lot exe label
exe_static_label = tk.Label(root, text="exe:")
exe_static_label.grid(row=4, column=0)
exe_static_label.config(font=("Helvetica", 12))

# lot exe variable to display
lot_exe_var = tk.StringVar()
lot_exe_var.set("Variable Output")

# label that displays the lot exe
lot_exe_dynamic_label = tk.Label(root, textvariable=lot_exe_var)
lot_exe_dynamic_label.grid(row=4, column=1)

#
# exe label with text entry next to it
exe_label = tk.Label(root, text="exe:")
exe_label.grid(row=4, column=0)

exe_entry = tk.Entry(root)
exe_entry.grid(row=4, column=1)
exe_entry.config(font=("Helvetica", 12))

#
#calendar
def get_date(calendar):
    selected_date = calendar.selection_get()
    print("Selected date:", selected_date)

calendar = Calendar(root, selectmode='day', year=datetime.datetime.now().year, month=datetime.datetime.now().month, day=datetime.datetime.now().day)
calendar.grid(row=7, column = 3)

button = tk.Button(root, text="Get date", command=lambda: get_date(calendar))
button.grid(row=7, column = 4)

#better calandar
# Declare string variable for date
dateStr = tk.StringVar()
# Create a date picker widget
date_picker = DateEntry(root, date_pattern="yyyy-MM-dd",textvariable=dateStr)
date_picker.set_date(datetime.date.today())
date_picker.config(font=("Helvetica", 12))

#output label with color change
exe_static_label = tk.Label(root, text="exe:", fg=exe_color)
exe_static_label.grid(row=4, column=0)
exe_static_label.config(font=("Helvetica", 12))