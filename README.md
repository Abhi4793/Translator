# Translator
These Projects are developed for Hackademy 2020


import pandas as pd

# Define the path to your Excel file
excel_file_path = 'path/to/your/file.xlsx'

# Specify the sheet name (if there are multiple sheets)
sheet_name = 'Sheet1'

# Specify the column name and row index
column_name = 'ColumnName'
row_index = 1

# Read the Excel file
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

# Access the specific cell value using column name and row index
cell_value = df.loc[row_index, column_name]

# Print the cell value
print(cell_value)



Tkinter

import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

def read_excel_row():
    # Open file dialog to select the Excel file
    file_path = filedialog.askopenfilename(filetypes=[('Excel Files', '*.xlsx')])
    
    # Check if a file was selected
    if file_path:
        try:
            # Specify the sheet name (if there are multiple sheets)
            sheet_name = 'Sheet1'

            # Specify the column name and row index
            column_name = 'ColumnName'
            row_index = 1

            # Read the Excel file
            df = pd.read_excel(file_path, sheet_name=sheet_name)

            # Access the specific cell value using column name and row index
            cell_value = df.loc[row_index, column_name]

            # Show the cell value in a message box
            messagebox.showinfo("Cell Value", f"The cell value is: {cell_value}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Create the Tkinter window
window = tk.Tk()
window.title("Excel Reader")

# Create a button to trigger the Excel reading
button = tk.Button(window, text="Read Excel", command=read_excel_row)
button.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()


Output with a csv file using tkinter

import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

def read_excel_row():
    # Open file dialog to select the Excel file
    file_path = filedialog.askopenfilename(filetypes=[('Excel Files', '*.xlsx')])
    
    # Check if a file was selected
    if file_path:
        try:
            # Specify the sheet name (if there are multiple sheets)
            sheet_name = 'Sheet1'

            # Specify the column name and row index
            column_name = 'ColumnName'
            row_index = 1

            # Read the Excel file
            df = pd.read_excel(file_path, sheet_name=sheet_name)

            # Access the specific cell value using column name and row index
            cell_value = df.loc[row_index, column_name]

            # Save the extracted data to a new Excel file
            output_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx',
                                                            filetypes=[('Excel Files', '*.xlsx')])
            if output_file_path:
                df_extracted = pd.DataFrame({'Cell Value': [cell_value]})
                df_extracted.to_excel(output_file_path, index=False)
                messagebox.showinfo("Success", "Data saved successfully!")
            else:
                messagebox.showinfo("Info", "No output file selected.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Create the Tkinter window
window = tk.Tk()
window.title("Excel Reader")

# Create a button to trigger the Excel reading
button = tk.Button(window, text="Read Excel", command=read_excel_row)
button.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()
