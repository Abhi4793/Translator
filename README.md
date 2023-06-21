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

        # Define a dictionary to store the cell values, category, metrics, location, and quarter for each sheet
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

            # Define the cell ranges for the desired values
            cell_ranges = [
                (13, 17),  # Cell value 1
                (14, 17),  # Cell value 2
                (15, 17),  # Cell value 3
                # Add more cell ranges as needed
            ]

            # Read the cell values
            cell_values = [source_sheet.range(row, col).value for row, col in cell_ranges]

            # Define the row index and column index for the quarter
            quarter_row_index = 10
            quarter_column_index = 54

            # Read the quarter value
            quarter_value = source_sheet.range(quarter_row_index, quarter_column_index).value

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

            # Store the cell values, category, metrics, location, and quarter in the dictionary
            sheet_data[sheet_name] = {'cell_values': cell_values, 'category': category, 'metrics': metrics, 'location': location, 'quarter': quarter_value}

        # Create a new workbook to write the cell values
        output_file_path = filedialog.asksaveasfilename(filetypes=[('Excel Files', '*.xlsx')])

        if output_file_path:
            # Check if the output file already exists
            if xw.Book(output_file_path).sheets:
                # Open the existing output file
                output_workbook = xw.Book(output_file_path)
            else:
                # Create a new output file
                output_workbook = xw.Book()
            
            # Select the first sheet in the output workbook
            output_sheet = output_workbook.sheets[0]

            # Find the next available row in the output sheet
            row = output_sheet.range((output_sheet.cells.last_cell.row, 1)).end('up').

            # Find the next available row in the output sheet
            row = output_sheet.range((output_sheet.cells.last_cell.row, 1)).end('up').row + 1

            # Write the cell values, category, metrics, location, quarter, and unit to the output sheet
            output_sheet.range(f'A{row}').value = 'Sheet Name'
            output_sheet.range(f'B{row}').value = 'Cell Value 1'
            output_sheet.range(f'C{row}').value = 'Cell Value 2'
            output_sheet.range(f'D{row}').value = 'Cell Value 3'
            output_sheet.range(f'E{row}').value = 'Category'
            output_sheet.range(f'F{row}').value = 'Metrics'
            output_sheet.range(f'G{row}').value = 'Location'
            output_sheet.range(f'H{row}').value = 'Quarter'
            output_sheet.range(f'I{row}').value = 'Unit'

            # Write the data to the output sheet
            for sheet_name, data in sheet_data.items():
                output_sheet.range(f'A{row}').offset(column_offset=1).value = sheet_name
                output_sheet.range(f'B{row}').offset(column_offset=1).value = data['cell_values'][0]
                output_sheet.range(f'C{row}').offset(column_offset=1).value = data['cell_values'][1]
                output_sheet.range(f'D{row}').offset(column_offset=1).value = data['cell_values'][2]
                output_sheet.range(f'E{row}').offset(column_offset=1).value = data['category']
                output_sheet.range(f'F{row}').offset(column_offset=1).value = data['metrics']
                output_sheet.range(f'G{row}').offset(column_offset=1).value = data['location']
                output_sheet.range(f'H{row}').offset(column_offset=1).value = data['quarter']
                output_sheet.range(f'I{row}').offset(column_offset=1).value = 'kWh'
                row += 1

            # Save the output workbook
            output_workbook.save(output_file_path)
            output_workbook.close()

            # Close the source workbook
            source_workbook.close()

            print("Output file generated successfully!")
        else:
            print("No output file selected.")


# Create a Tkinter root window
root = tk.Tk()

# Create a button to trigger the file selection and processing
button = tk.Button(root, text="Select and Process File", command=process_file)
button.pack()

# Run the Tkinter event loop
root.mainloop()
