from tkinter import *


def miles_to_km(miles, km_label):
    try:
        miles_float = float(miles)
        km_label.config(text=miles_float * 1.60934)
    except ValueError:
        km_label.config(text="ERROR: Entra un nombre vàlid.")


window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=100, height=100)

Label(text="is equal to").grid(column=0, row=1, padx=10, pady=10)
Label(text="Miles").grid(column=2, row=0, padx=10, pady=10)
Label(text="Km").grid(column=2, row=1, padx=10, pady=10)

miles_ = Entry(width=5)
miles_.grid(column=1, row=0)

kms = 0
kilometers_label = Label(text=kms)
kilometers_label.grid(column=1, row=1, padx=10, pady=10)

calculate = Button(text="Calculate", command=lambda: miles_to_km(miles_.get(), kilometers_label))
calculate.grid(column=1, row=2)

window.mainloop()
