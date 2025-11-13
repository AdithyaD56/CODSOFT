from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error, invalid Input")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def key_event(event):
    char = event.char
    if char in "0123456789.+-*/":
        press(char)
    elif event.keysym == "Return":
        equalpress()
    elif event.keysym == "BackSpace":
        backspace()
    elif event.keysym == "Escape":
        clear()

gui = Tk()
gui.configure(background="lightgrey")
gui.title("Simple Calculator")
gui.geometry("350x300")
equation = StringVar()
expression_field = Entry(gui, textvariable=equation, font=("Arial",16), state="readonly", justify='right')
expression_field.grid(columnspan=4, ipadx=50, ipady=8)
gui.bind("<Key>", key_event)

Button(gui, text='1', command=lambda: press(1), width=7, height=2).grid(row=2, column=0)
Button(gui, text='2', command=lambda: press(2), width=7, height=2).grid(row=2, column=1)
Button(gui, text='3', command=lambda: press(3), width=7, height=2).grid(row=2, column=2)

Button(gui, text='4', command=lambda: press(4), width=7, height=2).grid(row=3, column=0)
Button(gui, text='5', command=lambda: press(5), width=7, height=2).grid(row=3, column=1)
Button(gui, text='6', command=lambda: press(6), width=7, height=2).grid(row=3, column=2)

Button(gui, text='7', command=lambda: press(7), width=7, height=2).grid(row=4, column=0)
Button(gui, text='8', command=lambda: press(8), width=7, height=2).grid(row=4, column=1)
Button(gui, text='9', command=lambda: press(9), width=7, height=2).grid(row=4, column=2)

Button(gui, text='0', command=lambda: press(0), width=7, height=2).grid(row=5, column=0)
Button(gui, text='.', command=lambda: press('.'), width=7, height=2).grid(row=5, column=1)

Button(gui, text='=', command=equalpress, width=7, height=2).grid(row=5, column=2)
Button(gui, text='+', command=lambda: press('+'), width=7, height=2).grid(row=2, column=3)
Button(gui, text='-', command=lambda: press('-'), width=7, height=2).grid(row=3, column=3)
Button(gui, text='*', command=lambda: press('*'), width=7, height=2).grid(row=4, column=3)
Button(gui, text='/', command=lambda: press('/'), width=7, height=2).grid(row=5, column=3)

Button(gui, text='Backspace', command=backspace, width=29, height=2).grid(row=6, columnspan=4)
Button(gui, text='Clear', command=clear, width=29, height=2).grid(row=7, columnspan=4)

gui.mainloop()