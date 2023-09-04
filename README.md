// This is a conceptual example and doesn't represent actual Kafka source code.

// CustomLeaderElection class that implements a simplified leader election process
public class CustomLeaderElection {
    private Map<Integer, Broker> brokers; // Map of broker IDs to Broker instances

    public CustomLeaderElection(Map<Integer, Broker> brokers) {
        this.brokers = brokers;
    }

    // Custom leader election logic
    public int electLeader() {
        int leaderId = -1; // Initialize with an invalid value

        // Implement your custom leader election algorithm here.
        // For example, you might choose the broker with the highest uptime as the leader.
        for (Broker broker : brokers.values()) {
            if (leaderId == -1 || broker.getUptime() > brokers.get(leaderId).getUptime()) {
                leaderId = broker.getId();
            }
        }

        return leaderId;
    }

    // Method to start the leader election process
    public void startLeaderElection() {
        int newLeaderId = electLeader();

        // Update the metadata to reflect the new leader
        MetadataManager.updateLeader(newLeaderId);
    }
}






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













openpyxl

import openpyxl
from tkinter import Tk, filedialog, messagebox

def read_excel_files():
    # Open file dialog to select multiple Excel files
    file_paths = filedialog.askopenfilenames(filetypes=[('Excel Files', '*.xlsx')])
    
    # Check if files were selected
    if file_paths:
        try:
            # Specify the sheet name (if there are multiple sheets)
            sheet_name = 'Sheet1'

            # Specify the column names and row index
            column_names = ['Column1', 'Column2', 'Column3']
            row_index = 1

            # Create an empty list to store extracted values
            extracted_values = []

            # Read each Excel file and extract the specified cell values
            for file_path in file_paths:
                workbook = openpyxl.load_workbook(file_path, read_only=True)
                
                # Check if the input sheet name contains 'pune' or 'Pune'
                sheet_names = workbook.sheetnames
                target_sheet = None
                for name in sheet_names:
                    if 'pune' in name.lower() or 'Pune' in name:
                        target_sheet = workbook[name]
                        break
                
                if target_sheet:
                    cell_values = [target_sheet.cell(row=row_index, column=target_sheet.cell(row=row_index, column=1).column + i).value
                                   for i, column_name in enumerate(column_names)]
                    extracted_values.append(cell_values)

            # Create a new Excel workbook
            output_workbook = openpyxl.Workbook()
            output_worksheet = output_workbook.active

            # Write the extracted values to the output worksheet
            for row_index, cell_values in enumerate(extracted_values, start=row_index):
                for col_index, cell_value in enumerate(cell_values):
                    output_worksheet.cell(row=row_index, column=col_index+1, value=cell_value)
                
                # Check the input sheet name and append 'Pune' or 'Hyd' to the output file name
                input_sheet_name = sheet_names[row_index - 1]
                output_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx',
                                                                filetypes=[('Excel Files', '*.xlsx')])

                if output_file_path:
                    if 'pune' in input_sheet_name.lower() or 'Pune' in input_sheet_name:
                        output_file_path = output_file_path[:-5] + "_Pune.xlsx"  # Append '_Pune' to the output file name
                    elif 'hyd' in input_sheet_name.lower() or 'Hyd' in input_sheet_name or 'Hyderabad' in input_sheet_name:
                        output_file_path = output_file_path[:-5] + "_Hyd.xlsx"  # Append '_Hyd' to the output file name

                    output_workbook.save(output_file_path)
                    messagebox.showinfo("Success", "Data saved successfully!")
                else:
                    messagebox.showinfo("Info", "No output file selected.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Create the Tkinter window
window = Tk()
window.title("Excel Reader")

# Create a button to trigger the Excel reading
button = Button(window, text="Read Excel Files", command=read_excel_files)
button.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()
