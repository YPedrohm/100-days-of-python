
from tkinter import *

def button_clicked():
    km = round(float(input.get()) * 1.6, 2)
    result_label.config(text=f"{km:.2f}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(250, 150)

input = Entry(width=10)
input.grid(row=0, column=1, padx=10, pady=10)
input.get()

label = Label(window, text="Miles", font=("Arial", 10))
label.grid(row=0, column=2, padx=10, pady=10)

equal_label = Label(window, text="is equal to", font=("Arial", 10))
equal_label.grid(row=1, column=0, padx=10, pady=10)

result_label = Label(window, text="0", font=("Arial", 10))
result_label.grid(row=1, column=1, padx=10, pady=10)

km_label = Label(window, text="Km", font=("Arial", 10))
km_label.grid(row=1, column=2, padx=10, pady=10)

button = Button(window, text="Calculate", command=button_clicked)
button.grid(row=2, column=1, padx=10, pady=10)

window.mainloop()
