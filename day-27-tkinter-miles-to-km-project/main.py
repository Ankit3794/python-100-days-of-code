import tkinter

FONT = ("Arial", 16)
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

# Miles input
miles = tkinter.Entry(width=10)
miles.grid(column=1, row=0)

# Miles label
miles_label = tkinter.Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

# text label
is_equals_label = tkinter.Label(text="is equal to", font=FONT)
is_equals_label.grid(column=0, row=1)

# km value label
km_value_label = tkinter.Label(text="0", font=FONT)
km_value_label.grid(column=1, row=1)

# km label
km_label = tkinter.Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)


def convert_mile_to_km():
    mile = float(miles.get())
    km = mile * 1.60934
    km_value_label.config(text=f"{km:.3f}")


# calculate button
calculate_btn = tkinter.Button(text="Calculate", command=convert_mile_to_km)
calculate_btn.grid(column=1, row=2)

window.mainloop()
