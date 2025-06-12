import tkinter as tk
import math

def click(btn):
    current = entry.get()
    if btn == "=":
        try:
            if "!" in current:
                number = int(current.replace("!",""))
                result = math.factorial(number)
            else:
                result = eval(current.replace("^","**"))
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except:                         # HANDLE ANY ERRORS IN EVALUATION, CLEAR THE ENTRY AND SHOW "ERROR"
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif btn == "C":
        entry.delete(0, tk.END)
    #TRIG FUNCTIONS
    elif btn in ("sin", "cos", "tan"):
        try:
            # CONVERT TO RADIANS AND APPLY THE TRIG FUNCTION
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
    #ADDITIONAL FUNCTIONS
    elif btn  == "sqrt":
        try:
            value = float(current)
            result = math.sqrt(value)
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error") 
    elif btn == "log":
        try:
            value = float(current)
            result = math.log10(value)
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    #CONSTANTS AND FACTORIALS
    elif btn == "!":
        try:
            entry.insert(tk.END, "!")
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")

    elif btn == "pi":
        entry.insert(tk.END, str(math.pi))
    elif btn == "e":
        entry.insert(tk.END, str(math.e))

    else:
        entry.insert(tk.END, btn)

#ENTER HANDLER
def handle_enter(event):
    click("=")


# CREATE MAIN WINDOW
root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)

# ENTRY WIDGET (DISPLAY)
entry = tk.Entry(root, width=25, font=("Arial", 18), bd=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# BIND ENTER KEY
entry.bind("<Return>",  lambda event: click("=")) 

# BUTTON LABELS
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# CREATE AND PLACE BUTTONS IN GRID
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
    #ADDITIONAL BUTTONS
    tk.Button(root, text = 'sqrt', width=5, height=2, font=("Arial", 18),
              command=lambda: click('sqrt')).grid(row=5, column=3)
    tk.Button(root, text = '^', width=5, height=2, font=("Arial", 18),
              command=lambda: click('**')).grid(row=6, column=1)
    #CONSTANTS & FACTORIALS
    tk.Button(root, text='pi', width=5, height=2, font=("Arial", 18),
              command=lambda: click('pi')).grid(row=6, column=0)
    tk.Button(root, text='e', width=5, height=2, font=("Arial", 18),
              command=lambda: click('e')).grid(row=6, column=2)
    tk.Button(root, text='!', width=5, height=2, font=("Arial", 18),
              command=lambda: click('!')).grid(row=6, column=3)

    col += 1
    if col > 3:
        col = 0
        row += 1

# START THE GUI LOOP
root.mainloop()

