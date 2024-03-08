**Section 4: Tkinter Examples**

**4.1 Tkinter Example: Fahrenheit to Celsius Converter**

Let's create a simple Tkinter application that converts a temperature from Fahrenheit to Celsius. We'll include an entry widget for users to input the temperature in Fahrenheit, a button to trigger the conversion, and a label to display the result in Celsius.

```python
import tkinter as tk

def convert():
    # Get the temperature in Fahrenheit from the entry widget
    fahrenheit = float(entry.get())

    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5/9

    # Update the result label with the converted temperature
    result_label.config(text=f"{fahrenheit}°F is {celsius:.2f}°C")

# Create the main application window
root = tk.Tk()
root.title("Fahrenheit to Celsius Converter")

# Create an entry widget for temperature input
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a button to trigger the conversion
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack()

# Create a label to display the result
result_label = tk.Label(root)
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
```

In this example, we define a function `convert()` to handle the conversion process. Inside this function, we retrieve the temperature in Fahrenheit from the entry widget, convert it to Celsius using the conversion formula, and update the text of the result label with the converted temperature. The main application window consists of an entry widget for temperature input, a button to trigger the conversion, and a label to display the result.

By running this application, users can input a temperature in Fahrenheit, click the "Convert" button, and instantly see the converted temperature in Celsius. This simple example demonstrates the basic structure and functionality of a Tkinter application, illustrating how easy it is to create interactive GUIs with Python.
