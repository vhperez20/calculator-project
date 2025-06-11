import tkinter as tk

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
    tk.Button(root, text=b, width=5, height=2, font=("Arial", 18),
              command=lambda x=b: click(x)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the GUI loop
root.mainloop()

