"""
Things to improve:
- Unit testing
- Division by zero
- Decimal checking
- Bracket within bracket cases
"""

import tkinter as tk
import re
import operator

button_labels = {
    "00": "Delete", "01": "(", "02": ")", "03": "÷",
    "10": "7", "11": "8", "12": "9", "13": "x",
    "20": "4", "21": "5", "22": "6", "23": "-",
    "30": "1", "31": "2", "32": "3", "33": "+",
    "40": "%", "41": "0", "42": ".", "43": "="
}
calculator_functions = {
    "00": lambda: delete_item(), "01": lambda: insert_item(0,1), "02": lambda: insert_item(0,2), "03": lambda: insert_operation(0,3),
    "10": lambda: insert_item(1,0), "11": lambda: insert_item(1,1), "12": lambda: insert_item(1,2), "13": lambda: insert_operation(1,3),
    "20": lambda: insert_item(2,0), "21": lambda: insert_item(2,1), "22": lambda: insert_item(2,2), "23": lambda: insert_operation(2,3),
    "30": lambda: insert_item(3,0), "31": lambda: insert_item(3,1), "32": lambda: insert_item(3,2), "33": lambda: insert_operation(3,3),
    "40": lambda: insert_item(4,0), "41": lambda: insert_item(4,1), "42": lambda: insert_decimal(), "43": lambda: calculate()
}
button_dict = {}

def delete_item():
    """Deletes a value in the entry."""
    ent_input.delete(ent_input.index("end") - 1)

def insert_item(i: int, j: int):
    """Takes the button value and inserts it into the entry."""
    value = button_labels[f"{i}{j}"]
    ent_input.insert(tk.END, value)

def insert_operation(i: int, j: int):
    """Inserts operation at end of entry."""
    str_value = ent_input.get()
    if str_value[-1] not in ["+", "-", "÷", "x"]:
        value = button_labels[f"{i}{j}"]
        ent_input.insert(tk.END, value)

def insert_decimal():
    """Inserts a decimal into entry."""
    # if "." not in ent_input.get():
    #     ent_input.insert(tk.END, ".")
    ent_input.insert(tk.END, ".")

def operations(expression: str):
    """Performs bedmas operations on an expression. expression -> result (single float)"""
    bedmas = [
        r"(-?\d+(\.\d+)?)([÷x%])(-?\d+(\.\d+)?)",
        r"(-?\d+(\.\d+)?)([+\-])(-?\d+(\.\d+)?)",
    ]
    operation = {
        "+": operator.add,
        "-": operator.sub,
        "÷": operator.truediv,
        "x": operator.mul,
        "%": operator.mod
    }

    for i in range(len(bedmas)):                            # Loops through bedmas
        while True:
            op_match = re.search(bedmas[i], expression)     # Searches for the first occurance in bedmas
            if op_match == None:                            # Stops loop if there are no occurances
                break
            op_calculation = operation[op_match.group(3)](float(op_match.group(1)), float(op_match.group(4)))   # Performs operation
            expression = expression.replace(op_match.group(0), str(op_calculation), 1)                          # Replaces result of operation back into str_value
    return expression


def calculate():
    """Calculates the values in the entry."""
    str_value = ent_input.get()
    ent_input.delete(0, tk.END)

    #print(f"Original: {str_value}")
    while True:
        op_match = re.search(r"\((.*?)\)", str_value)
        if op_match == None:
            break
        reduce = operations(op_match.group(1))
        str_value = str_value.replace(op_match.group(0), str(reduce), 1)
    str_value = operations(str_value)
    #print(f"Output: {str_value}")

    ent_input.insert(0, str_value)


# Calculator Window Frame
window = tk.Tk()
window.title("Calculator")

ent_input = tk.Entry(master=window)     # Entry for calculations
ent_input.pack(fill=tk.X)

frm_buttons = tk.Frame(master=window)   # Frame for buttons
frm_buttons.pack()

frm_buttons.rowconfigure(list(range(5)), weight=1, minsize=25)
frm_buttons.columnconfigure(list(range(4)), weight=1, minsize=25)
for i in range(5):
    for j in range(4):
        button = tk.Button(
            master=frm_buttons,
            relief=tk.RAISED,
            borderwidth=1,
            text=button_labels[f"{i}{j}"],                      # Buttons have text values from dictionary
            command=calculator_functions[f"{i}{j}"],            # Buttons have functions from dictionary
            width=4,
            height=2
        )
        button.grid(row=i, column=j, padx=5, pady=5, sticky="nesw")
        button_dict[f"{i}{j}"] = button                         # Records button in dictionary (in case of later use)

window.mainloop()