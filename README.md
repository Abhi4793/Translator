test code

import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os

# Function to derive the quarter from the month
def derive_quarter(month):
    if month in ['Jan', 'Feb', 'Mar']:
        return 'Q1'
    elif month in ['Apr', 'May', 'Jun']:
        return 'Q2'
    elif month in ['Jul', 'Aug', 'Sep']:
        return 'Q3'
    elif month in ['Oct', 'Nov', 'Dec']:
        return 'Q4'
    else:
        return ''

# Function to handle button click and process the data
def process_data():
    # Get the selected file paths
    input_file_path = input_entry.get()
    output_file_path = output_entry.get()
    
    # Extract the location from the input file name
    file_name = os.path.basename(input_file_path)
    if 'pune' in file_name.lower():
        location = 'HTI_Pune'
    elif 'hyd' in file_name.lower():
        location = 'HTI_Hyd'
    else:
        location = 'Unknown'

    # Define the tab names
    tab_names = ['electricity', 'PPA', 'Diesel']

    # Read the data from the input file
    data = {}
    for tab_name in tab_names:
        data[tab_name] = pd.read_excel(input_file_path, sheet_name=tab_name)

    # Create an empty DataFrame for the output
    output_data = pd.DataFrame(columns=['Category', 'Type', 'Year', 'Quarter', 'Amount', 'Unit', 'Location'])

    # Process the data for each tab
    for tab_name, df in data.items():
        # Determine the quarter from the column names
        quarters = [derive_quarter(col) for col in df.columns if col != 'office']

        # Iterate over the quarters and read the corresponding values
        for quarter in quarters:
            # Extract the year from the quarter column name
            year = quarter.split()[1]

            # Read the values from specific cells
            electricity = df.loc[13, 'office']
            solar = df.loc[13, 'office.1']
            diesel = df.loc[13, 'office.2']

            # Append the data to the output DataFrame
            output_data = output_data.append({
                'Category': 'Energy',
                'Type': tab_name,
                'Year': int(year),
                'Quarter': quarter,
                'Amount': electricity if tab_name == 'electricity' else solar if tab_name == 'PPA' else diesel,
                'Unit': 'kWh',
                'Location': location
            }, ignore_index=True)

    # Write the output data to the output file
    output_data.to_excel(output_file_path, index=False)
    output_label.config(text="Output file generated successfully!")

# Create the main window
window = tk.Tk()
window.title("Excel Data Processor")

# Create and position the input file path label and entry
input_label = tk.Label(window, text="Input File:")
input_label.pack()
input_entry = tk.Entry(window, width=50)
input_entry.pack()

# Create and position the input file path browse button
def browse_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)

input_button = tk.Button(window, text="Browse", command=browse_input_file)
input_button.pack()

# Create and position the output file path label and entry
output
