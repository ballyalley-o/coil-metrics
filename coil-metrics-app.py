import os
import csv
import tkinter as tk
from tkinter import filedialog
from .constant.constant import *
from dotenv import load_dotenv
load_dotenv()


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
    csvfile = filedialog.askopenfilename(filetypes=[(CSV_TITLE, "*.csv")])
    operation_counts = {}

    with open(csvfile, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            for i in range(12, len(row), 2):
                operation = row[i]
                if operation in operation_counts:
                    operation_counts[operation] += 1
                else:
                    operation_counts[operation] = 1

    for operation, count in operation_counts.items():
        text.insert(tk.END, f'{operation}: {count}\n')

root = tk.Tk()
app_title = os.getenv("APP_TITLE")
root.title(app_title)

text = tk.Text(root)
text.pack()

button = tk.Button(root, text=APP_BUTTON_TEXT, command=calculate_operation_counts)
button.pack()

root.mainloop()