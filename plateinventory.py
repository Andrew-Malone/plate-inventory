import tkinter as tk
from configparser import ConfigParser
from tkinter import filedialog
import pandas as pd
import os

class LabeledEntry(tk.Frame):
    def __init__(self, master, label_text, fontSize, padding):
        super().__init__(master)
        self.label = tk.Label(self, text=label_text, font=('Helvetica', fontSize))
        self.label.grid(row=0, column=0, pady=padding)
        self.entry = tk.Entry(self)
        self.entry.grid(row=0, column=1, pady=padding)

    def get(self):
        return self.entry.get()

# ************************************
# Update the form values on user entry
# ************************************
def update_values(self):
    # Get the values from the entries
    monday_val = int(monday_entry.get()) if monday_entry.get().isdigit() else 0
    press_val = int(press_entry.get()) if press_entry.get().isdigit() else 0
    pp_val = int(pp_entry.get()) if pp_entry.get().isdigit() else 0
    good_val = int(good_entry.get()) if good_entry.get().isdigit() else 0
    inv_val = int(inv_entry.get()) if inv_entry.get().isdigit() else 0
    
    # Calculate the total used and friday total
    total_used = press_val + pp_val + good_val
    friday_total = monday_val - total_used + inv_val
    
    # Update the values dictionary
    values['Monday'] = monday_val
    values['Press Remakes'] = press_val
    values['PP Scrap'] = pp_val
    values['Total Good'] = good_val
    values['Total Used'] = total_used
    values['Inventory Addition'] = inv_val
    values['Friday'] = friday_total
    
    # Update the labels
    total_used_label.config(text=str(total_used))
    friday_label.config(text=str(friday_total))

# *********************
# Export the excel file
# *********************
def export_excel():
    # Get the default path from the config
    default_path = config.get('DEFAULTS', 'defaultfilepath')

    # Open the file dialog for file name and directory selection
    file_path = filedialog.asksaveasfilename(
            initialdir=default_path,
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx")],
            title="Save the Excel File"
        )

    # Export the Excel file
    if file_path:
        # Get the directory path to save as default in the config
        dir_path  = os.path.dirname(file_path)
        
        # Save the excel file
        df = pd.DataFrame([values])
        df.to_excel(file_path, index=False)

        # Update the default path in the config
        config.set('DEFAULTS', 'defaultfilepath', dir_path)
        with open('exportLocation.ini', 'w') as configfile:
            config.write(configfile)

    # Focus back on the main Tkinter window
    root.focus_force()

#***********************
# Create the main window
#***********************
root = tk.Tk()
root.title("Plate Inventory - Enter Data")
root.resizable(False, False)

# Create a dictionary to store the values
values = {
    'Monday': 0,
    'Press Remakes': 0,
    'PP Scrap': 0,
    'Total Good': 0,
    'Total Used': 0,
    'Inventory Addition': 0,
    'Friday': 0
}

# Get the default file export path
config = ConfigParser()
config.read('exportLocation.ini')

# Create the labeled entries and labels sticky="e"
monday_entry = LabeledEntry(root, "Monday:", 24, 10)
monday_entry.grid(row=0, column=0, sticky="e")
monday_entry.bind("<FocusOut>", update_values)

press_entry = LabeledEntry(root, "Press Remakes:", 16, 0)
press_entry.grid(row=1, column=0, sticky="e")
press_entry.bind("<FocusOut>", update_values)

pp_entry = LabeledEntry(root, "PP Scrap:", 16, 0)
pp_entry.grid(row=2, column=0, sticky="e")
pp_entry.bind("<FocusOut>", update_values)

good_entry = LabeledEntry(root, "Total Good:", 16, 0)
good_entry.grid(row=3, column=0, sticky="e")
good_entry.bind("<FocusOut>", update_values)

total_used_name_label = tk.Label(root, text="Total Used:", font=("Helvetica", 24))
total_used_name_label.grid(row=4, column=0, sticky="w", pady=10)
total_used_label = tk.Label(root, text="0", font=("Helvetica", 24))
#total_used_label.config(bg="lightgrey")
total_used_label.grid(row=4, column=0, sticky="e")

inv_entry = LabeledEntry(root, "Inventory Addition:", 16, 0)
inv_entry.grid(row=5, column=0, sticky="e")
inv_entry.bind("<FocusOut>", update_values)

friday_name_label = tk.Label(root, text="Friday Total:", font=("Helvetica", 24))
friday_name_label.grid(row=6, column=0, sticky="w", pady=10)
friday_label = tk.Label(root, text="0", font=("Helvetica", 24))
friday_label.grid(row=6, column=0, sticky="e")

excel_button = tk.Button(root, text="Export Excel File", command=export_excel)
excel_button.grid(row=7, column=0, sticky="e", pady=10)

# Set focus on the Monday entry
monday_entry.entry.focus_set()

# Center the window
    # code here later

root.mainloop()
