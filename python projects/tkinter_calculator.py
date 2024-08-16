from tkinter import *

first = second = operator = None


def get_digit(digit):
    current = result_label["text"]
    new = current + str(digit)
    result_label.config(text=new)


def clear():
    result_label.config(text="")


def operation(op):
    global first, operator
    first = float(result_label["text"])
    operator = op
    result_label.config(text="")


def get_result():
    global first, second, operator
    second = float(result_label["text"])
    if operator == "+":
        result_label.config(text=str(first + second))
    elif operator == "-":
        result_label.config(text=str(first - second))
    elif operator == "*":
        result_label.config(text=str(first * second))
    else:
        if second == 0:
            result_label.config(text="ERROR")
        else:
            result_label.config(text=str(round(first / second, 2)))


root = Tk()
root.title("tkinter_calculator")
root.geometry("290x310")
root.resizable(0, 0)
root.configure(bg="black")

result_label = Label(root, text="", bg="black", fg="white")
result_label.grid(row=0, column=0, pady=(50, 25), columnspan=4, sticky="e")
result_label.config(font=("verdana", 30, "bold"))

btn_0 = Button(
    root,
    text="0",
    bg="#FF9912",
    fg="black",
    width=4,
    height=2,
    command=lambda: get_digit(0),
)
btn_0.grid(row=4, column=1)
btn_0.config(font=("verdana", 14))

btn_1 = Button(
    root,
    text="1",
    bg="#FF9912",
    fg="black",
    width=4,
    height=2,
    command=lambda: get_digit(1),
)
btn_1.grid(row=3, column=0)
btn_1.config(font=("verdana", 14))

btn_2 = Button(
    root,
    text="2",
    bg="#FF9912",
    fg="black",
    width=4,
    height=2,
    command=lambda: get_digit(2),
)
btn_2.grid(row=3, column=1)
btn_2.config(font=("verdana", 14))

btn_3 = Button(
    root,
    text="3",
    bg="#FF9912",
    fg="black",
    width=4,
    height=2,
    command=lambda: get_digit(3),
)
btn_3.grid(row=3, column=2)
btn_3.config(font=("verdana", 14))

btn_4 = Button(
    root,
    text="4",
    bg="#FF9912",
    fg="black",
    width=4,
    height=2,
    command=lambda: get_digit(4),
)
btn_4.grid(row=2, column=0)
btn_4.config(font=("verdana", 14))

btn_5 = Button(
    root,
    text="5",
    bg="#FF9912",
    fg="black",
    width=4,
    height=2,
    command=lambda: get_digit(5),
)
btn_5.grid(row=2, column=1)
btn_5.config(font=("verdana", 14))

btn_6 = Button(
    root,
    text="6",
    bg="#FF9912",
    fg="black",
    width=4,
    height=2,
    command=lambda: get_digit(6),
)
btn_6.grid(row=2, column=2)
btn_6.config(font=("verdana", 14))

btn_7 = Button(
    root,
    text="7",
    bg="#FF9912",
    fg="black",
    width=4,
    height=2,
    command=lambda: get_digit(7),
)
btn_7.grid(row=1, column=0)
btn_7.config(font=("verdana", 14))

btn_8 = Button(
    root,
    text="8",
    bg="#FF9912",
    fg="black",
    width=4,
    height=2,
    command=lambda: get_digit(8),
)
btn_8.grid(row=1, column=1)
btn_8.config(font=("verdana", 14))

btn_9 = Button(
    root,
    text="9",
    bg="#FF9912",
    fg="black",
    width=4,
    height=2,
    command=lambda: get_digit(9),
)
btn_9.grid(row=1, column=2)
btn_9.config(font=("verdana", 14))

btn_add = Button(
    root,
    text="+",
    bg="#FF9912",
    fg="black",
    width=4,
    height=2,
    command=lambda: operation("+"),
)
btn_add.grid(row=1, column=3)
btn_add.config(font=("verdana", 14))

btn_sub = Button(
    root,
    text="-",
    bg="#FF9912",
    fg="black",
    width=4,
    height=2,
    command=lambda: operation("-"),
)
btn_sub.grid(row=2, column=3)
btn_sub.config(font=("verdana", 14))

btn_mul = Button(
    root,
    text="*",
    bg="#FF9912",
    fg="black",
    width=4,
    height=2,
    command=lambda: operation("*"),
)
btn_mul.grid(row=3, column=3)
btn_mul.config(font=("verdana", 14))

btn_clear = Button(
    root,
    text="AC",
    bg="#FF9912",
    fg="black",
    width=4,
    height=2,
    command=lambda: clear(),
)
btn_clear.grid(row=4, column=0)
btn_clear.config(font=("verdana", 14))

btn_equals = Button(
    root,
    text="=",
    bg="#FF9912",
    fg="black",
    width=4,
    height=2,
    command=get_result,
)
btn_equals.grid(row=4, column=2)
btn_equals.config(font=("verdana", 14))

btn_div = Button(
    root,
    text="/",
    bg="#FF9912",
    fg="black",
    width=4,
    height=2,
    command=lambda: operation("/"),
)
btn_div.grid(row=4, column=3)
btn_div.config(font=("verdana", 14))

root.mainloop()
