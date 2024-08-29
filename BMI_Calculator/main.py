# All modules imported into Tkinter
from tkinter import *

# Properties
FONT = ("Arial", 10, "bold")

# Window
window = Tk()
window.title("BMI Calculator")
window.config(pady=80)
window.minsize(width=200, height=300)

# Weight Label and Entry
label_weight = Label(text="Enter Your Weight (kg)", font=FONT)
label_weight.pack()
entry_weight = Entry(width=20)
entry_weight.pack()

# Height Label and Entry
label_height = Label(text="Enter Your Height (cm)", font=FONT)
label_height.pack()
entry_height = Entry(width=20)
entry_height.pack()

# Result Label
result_label = Label(text=f"Result:", font=FONT)
result_label.pack()


# Calculate BMI Function
def calculate_bmi():
    user_bmi = 0
    result = ""

    try:
        weight = int(entry_weight.get())
        height = int(entry_height.get()) / 100

        user_bmi = weight / (height ** 2)

        if user_bmi <= 18.5:
            result = "Underweight"
        elif 18.5 < user_bmi <= 24.9:
            result = "Normal"
        elif 25 <= user_bmi <= 29.9:
            result = "Overweight"
        else:
            result = "Obese"

    except ValueError:
        result = "Enter a Valid Number!"
    finally:
        result_label.config(text=f"Result: {result}")


# Calculate Button
calculate_button = Button(text="Calculate", command=calculate_bmi, fg="dark red")
calculate_button.pack()

# Mainloop
window.mainloop()
