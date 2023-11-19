import tkinter

equation = ""


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def close_window():
    window.destroy()


def visualize_button_press(button):
    global equation
    if equation == "Error":
        equation = ""
    text = button.cget("text")
    equation += text
    operation_field.config(text=equation)


def clear():
    global equation
    equation = ""
    operation_field.config(text=equation)


def calculate():
    global equation

    if equation != "":
        try:
            equation = str(eval(equation))
            if is_float(equation):
                if len(equation) > 8:
                    equation = str(round(eval(equation), 2))
        except (SyntaxError, ZeroDivisionError):
            equation = "Error"

    operation_field.config(text=equation)

    return


# create a window
window = tkinter.Tk()
window.title("CalculatorApp")
window.resizable(False, False)

operation_frame = tkinter.Frame(window, width=500, height=100)
operation_frame.pack()

operators_frame = tkinter.Frame(window, width=500, height=500)
operators_frame.pack()

# set the size of the window
window_height = 600
window_width = 500

# center the window
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

y_coordinate = int((screen_height / 2) - (window_height / 2))
x_coordinate = int((screen_width / 2) - (window_width / 2))

window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# place a writing field
operation_field = tkinter.Label(operation_frame, font=("Roboto", 50), background="White")
operation_field.place(x=0, y=0, width=500, height=100)

# operators buttons
add_button = tkinter.Button(operators_frame, text="+", font=("Times", 30), command=lambda: visualize_button_press(add_button))
add_button.place(x=0, y=0, width=100, height=90)
subtract_button = tkinter.Button(operators_frame, text="-", font=("Times", 30), command=lambda: visualize_button_press(subtract_button))
subtract_button.place(x=0, y=90, width=100, height=90)
divide_button = tkinter.Button(operators_frame, text="/", font=("Times", 30), command=lambda: visualize_button_press(divide_button))
divide_button.place(x=0, y=180, width=100, height=90)
multiplicate_button = tkinter.Button(operators_frame, text="*", font=("Times", 30), command=lambda: visualize_button_press(multiplicate_button))
multiplicate_button.place(x=100, y=0, width=100, height=90)
square_root_button = tkinter.Button(operators_frame, text="√", font=("Times", 30), command=lambda: visualize_button_press(square_root_button))
square_root_button.place(x=200, y=0, width=100, height=90)
power_to_button = tkinter.Button(operators_frame, text="**", font=("Times", 30), command=lambda: visualize_button_press(power_to_button))
power_to_button.place(x=300, y=0, width=100, height=90)

# number buttons
one_button = tkinter.Button(operators_frame, text="1", font=("Times", 30), command=lambda: visualize_button_press(one_button))
one_button.place(x=100, y= 90, width=100, height=90)
two_button = tkinter.Button(operators_frame, text="2", font=("Times", 30), command=lambda: visualize_button_press(two_button))
two_button.place(x=200, y=90, width=100, height=90)
three_button = tkinter.Button(operators_frame, text="3", font=("Times", 30), command=lambda: visualize_button_press(three_button))
three_button.place(x=300, y=90, width=100, height=90)

four_button = tkinter.Button(operators_frame, text="4", font=("Times", 30), command=lambda: visualize_button_press(four_button))
four_button.place(x=100, y=180, width=100, height=90)
five_button = tkinter.Button(operators_frame, text="5", font=("Times", 30), command=lambda: visualize_button_press(five_button))
five_button.place(x=200, y=180, width=100, height=90)
six_button = tkinter.Button(operators_frame, text="6", font=("Times", 30), command=lambda: visualize_button_press(six_button))
six_button.place(x=300, y=180, width=100, height=90)

seven_button = tkinter.Button(operators_frame, text="7", font=("Times", 30), command=lambda: visualize_button_press(seven_button))
seven_button.place(x=100, y=270, width=100, height=90)
eight_button = tkinter.Button(operators_frame, text="8", font=("Times", 30), command=lambda: visualize_button_press(eight_button))
eight_button.place(x=200, y=270, width=100, height=90)
nine_button = tkinter.Button(operators_frame, text="9", font=("Times", 30), command=lambda: visualize_button_press(nine_button))
nine_button.place(x=300, y=270, width=100, height=90)

zero_button = tkinter.Button(operators_frame, text="0", font=("Times", 30), command=lambda: visualize_button_press(zero_button))
zero_button.place(x=200, y=360, width=100, height=90)

# special buttons
delete_button = tkinter.Button(operators_frame, text="C", font=("Times", 30), command=clear)
delete_button.place(x=400, y=0, width=100, height=90)
equals_button = tkinter.Button(operators_frame, text="==", font=("Times", 30), command=calculate)
equals_button.place(x=300, y=360, width=100, height=90)
close_button = tkinter.Button(operators_frame, text="Exit", font=("Times", 30), command=close_window)
close_button.place(x=0, y=270, width=100, height=180)
point_button = tkinter.Button(operators_frame, text=".", font=("Times", 30), command= lambda: visualize_button_press(point_button))
point_button.place(x=100, y=360, width=100, height=90)


window.mainloop()
