import tkinter as tk
import math

def click(btn):
    current = entry.get()
    if btn == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif btn == "C":
        entry.delete(0, tk.END)
    #TRIG FUNCTIONS
    elif btn in ("sin", "cos", "tan"):
        try:
            # Convert to radians and apply the trig function
            value = float(current)
            if btn == "sin":
                result = math.sin(math.radians(value))
            elif btn == "cos":
                result = math.cos(math.radians(value))
            elif btn == "tan":
                result = math.tan(math.radians(value))
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    else:
        entry.insert(tk.END, btn)

# Create main window
root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)

# Entry widget (display)
entry = tk.Entry(root, width=25, font=("Arial", 18), bd=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create and place buttons in grid
row = 1
col = 0
for b in buttons:
    #STANDARD BUTTONS
    tk.Button(root, text=b, width=5, height=2, font=("Arial", 18),
              command=lambda x=b: click(x)).grid(row=row, column=col, padx=5, pady=5)
    #TRIG BUTTONS
    tk.Button(root, text='sin', width=5, height=2, font=("Arial", 18),
              command=lambda: click('sin')).grid(row=5, column=0)

    tk.Button(root, text='cos', width=5, height=2, font=("Arial", 18),
              command=lambda: click('cos')).grid(row=5, column=1)

    tk.Button(root, text='tan', width=5, height=2, font=("Arial", 18),
              command=lambda: click('tan')).grid(row=5, column=2)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the GUI loop
root.mainloop()

