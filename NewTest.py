import tkinter as tk
from tkinter import filedialog
import xlwings as xw

# Function to process the input file and generate the output file
def process_file():
    # Prompt the user to select the input file
    file_path = filedialog.askopenfilename(filetypes=[('Excel Files', '*.xlsx')])

    # Check if a file was selected
    if file_path:
        # Open the source Excel file
        source_workbook = xw.Book(file_path)

        # Select the sheet names you want to read from
        sheet_names = ['sheet1', 'sheet2', 'sheet3']

        # Define a dictionary to store the cell values, category, metrics, and location for each sheet
        sheet_data = {}

        # Determine the location based on the input file name
        if 'Pune' in file_path:
            location = 'HTI-Pune'
        elif 'Hyd' in file_path:
            location = 'HTI-Hyderabad'
        else:
            location = None

        # Iterate over the selected sheet names
        for sheet_name in sheet_names:
            # Select the sheet from the source workbook
            source_sheet = source_workbook.sheets[sheet_name]

            # Define the row index and column index
            row_index = 13
            column_index = 17

            # Read the cell value
            cell_value = source_sheet.range(row_index, column_index).value

            # Determine the category based on the sheet name
            category = 'Energy' if sheet_name in ['Electricity1', 'PPA', 'Diesel'] else None

            # Determine the metrics based on the sheet name
            if sheet_name == 'Diesel':
                metrics = 'Generator Diesel [kWh]'
            elif sheet_name == 'PPA':
                metrics = 'PPA-Solar [kWh]'
            elif sheet_name == 'Electricity1':
                metrics = 'Total Electricity (purchased) [kWh]'
            else:
                metrics = None

            # Store the cell value, category, metrics, and location in the dictionary
            sheet_data[sheet_name] = {'cell_value': cell_value, 'category': category, 'metrics': metrics, 'location': location}

        # Create a new workbook to write the cell values
        output_file = 'output_file.xlsx'
        output_workbook = xw.Book()
        output_sheet = output_workbook.sheets.add()

        # Write the cell values, category, metrics, location, and unit to the output sheet
        output_sheet.range('A1').value = 'Sheet Name'
        output_sheet.range('B1').value = 'Cell Value'
        output_sheet.range('C1').value = 'Category'
        output_sheet.range('D1').value = 'Metrics'
        output_sheet.range('E1').value = 'Location'
        output_sheet.range('F1').value = 'Unit'

        for row, (sheet_name, data) in enumerate(sheet_data.items(), start=2):
            output_sheet.range(f'A{row}').value = sheet_name
            output_sheet.range(f'B{row}').value = data['cell_value']
            output_sheet.range(f'C{row}').value = data['category']
            output_sheet.range(f'D{row}').value = data['metrics']
            output_sheet.range(f'E{row}').value = data['location']
            output_sheet.range(f'F{row}').value = 'kWh'
        # Save the output workbook
        output_workbook.save(output_file)
        output_workbook.close()

        # Close the source workbook
        source_workbook.close()

        print("Output file generated successfully!")
    else:
        print("No file selected.")


# Create a Tkinter root window
root = tk.Tk()

# Create a button to trigger the file selection and processing
button = tk.Button(root, text="Select and Process File", command=process_file)
button.pack()

# Run the Tkinter event loop
root.mainloop()

