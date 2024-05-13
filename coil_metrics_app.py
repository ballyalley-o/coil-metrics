import csv
import math
import tkinter as tk
from tkinter import filedialog



def calculate_operation_counts():
    """
    Calculate the counts of each operation from a CSV file and display the results in a text widget.

    This function prompts the user to select a CSV file using a file dialog. It then reads the selected file,
    skips the header row, and iterates over each row to count the occurrences of each operation. The operation
    counts are stored in a dictionary, where the operation name is the key and the count is the value. Finally,
    the function displays the operation counts in a text widget.

    Note: This function assumes the existence of a `text` widget and the `filedialog` and `csv` modules.

    Returns:
        None
    """
    file_type = [("CSV files", "*.csv")]
    csvfile = filedialog.askopenfilename(filetypes=file_type)
    operation_counts = {}

    text.insert(tk.END, '\n')
    text.insert(tk.END, f'HOWICK Ltd.', 'bold_title')
    text.insert(tk.END, ' CSV Metrics \n', 'gray')
    # text.insert(tk.END, f'File: {csvfile.split("/")[-1]}\n', 'gray')
    text.insert(tk.END, '\n')
    text.insert(tk.END, f'Operations: \n', 'bold_default')

    with open(csvfile, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            for i in range(14, len(row), 2):
                operation = row[i]
                if operation in operation_counts:
                    operation_counts[operation] += 1
                else:
                    operation_counts[operation] = 1

    for operation, count in operation_counts.items():
        text.insert(tk.END, f'{operation}: ')
        text.insert(tk.END, f'{count}\n', 'bold_default')

    # scrape coil metrics
    total_meterage = 0
    row_count = 0
    components = 0
    profile = ''
    coil_thickness = ''
    frameset = ''


    with open(csvfile, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            row_count += 1
            if row_count == 4:
                frameset = row[1]
                continue

            if row_count >= 5:
                web_width = row[6]
                flange_height = row[7]
                coil_thickness = row[8]
                profile = f'{web_width}X{flange_height}'
                total_meterage += round(float(row[4]), 2)
                rounded_meterage = math.floor(total_meterage * 100) / 100
                components += 1


    text.insert(tk.END, '\n')
    text.insert(tk.END, 'Total Components: ', 'gray')
    text.insert(tk.END, f'{components}\n', 'bold_default')
    text.insert(tk.END, 'Total Meterage: ', 'gray')
    text.insert(tk.END, f'{rounded_meterage}\n','bold_default')
    text.insert(tk.END, '\n')
    text.insert(tk.END, f'Profile: ', 'gray')
    text.insert(tk.END, f'{profile}\n', 'bold_default')
    text.insert(tk.END, f'Coil Thickness: ', 'gray')
    text.insert(tk.END, f'{coil_thickness}\n', 'bold_default')
    text.insert(tk.END, f'Frameset: ', 'gray')
    text.insert(tk.END, f'{frameset}\n', 'bold_default')

    text.tag_config('blue', foreground='blue')
    text.tag_config('red', foreground='red')
    text.tag_config('yellow', foreground='yellow')
    text.tag_config('green', foreground='green')
    text.tag_config('purple', foreground='purple')
    text.tag_config('orange', foreground='orange')
    text.tag_config('black', foreground='black')
    text.tag_config('gray', foreground='gray')
    text.tag_config('pink', foreground='pink')
    text.tag_config('bold', font='Helvetica 12 bold')
    text.tag_config('bold_yellow', foreground='yellow', font=('Helvetica', '12', 'bold'))
    text.tag_config('bold_default', foreground='black', font=('Helvetica', '10', 'bold'))
    text.tag_config('bold_title', foreground='blue', font=('Helvetica', '10', 'bold'))



root = tk.Tk()
root.title("CSV Metrics")

text = tk.Text(root)
text.pack()

button = tk.Button(root, text="Open CSV", command=calculate_operation_counts)
button.pack()

root.mainloop()