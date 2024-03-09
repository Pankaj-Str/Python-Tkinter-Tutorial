import tkinter as tk

def get_input():
    input_value = entry_box.get()
    print("Input value is:", input_value)

app = tk.Tk()
app.title("Get Input Example")

label = tk.Label(app, text="Enter something:")
label.pack()

entry_box = tk.Entry(app)
entry_box.pack()

button = tk.Button(app, text="Get Input", command=get_input)
button.pack()

app.mainloop()