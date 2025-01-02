import tkinter as tk
from tkinter import *

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input .set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator = ""
#create main window
cal = Tk()
cal.title("Calculator")

#center the window
window_width = 400
window_height = 300
screen_width = cal.winfo_screenwidth()
screen_height = cal.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
cal.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

operator = ""
text_input = StringVar()

txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_input, bd=30, insertwidth=4,
                   bg="powder blue", justify='right')
txtDisplay.grid(columnspan=4)  # columnspan=4 means the entry will take 4 columns
# create buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3)
]
for (text, row, column) in buttons:
    if text == 'C':
        Button(cal, text=text, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
               bg="powder blue", command=btnClearDisplay).grid(row=row, column=column)
    elif text == '=':
        Button(cal, text=text, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
               bg="powder blue", command=btnEqualsInput).grid(row=row, column=column)
    else:
        Button(cal, text=text, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
               bg="powder blue", command=lambda t=text: btnClick(t)).grid(row=row, column=column)

 
cal.mainloop()