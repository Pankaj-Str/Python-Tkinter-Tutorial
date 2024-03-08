**Section 1: Tkinter Fundamentals**

**1.1 Tkinter Hello, World!**

The "Hello, World!" program is a classic introductory example in programming. Let's create a simple Tkinter application that displays a window with the text "Hello, World!".

```python
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Create a label widget with the text "Hello, World!"
label = tk.Label(root, text="Hello, World!")

# Pack the label into the window
label.pack()

# Start the Tkinter event loop
root.mainloop()
```

**1.2 Window Manipulation**

In this part, we'll explore various attributes of a Tkinter window, such as its title, size, location, resizability, transparency, and stacking order.

```python
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set window attributes
root.title("My Window")
root.geometry("300x200")  # Set window size (width x height)
root.resizable(True, True)  # Allow resizing both horizontally and vertically
root.attributes("-alpha", 0.8)  # Set transparency (0.0 to 1.0)
root.attributes("-topmost", True)  # Set stacking order (True places window on top)

# Start the Tkinter event loop
root.mainloop()
```

**1.3 Tk Themed Widgets**

Tkinter offers themed widgets with a modern look and feel. Let's create a button using a themed widget.

```python
import tkinter as tk
from tkinter import ttk  # Import themed widgets

# Create the main application window
root = tk.Tk()

# Create a themed button widget
button = ttk.Button(root, text="Click Me")

# Pack the button into the window
button.pack()

# Start the Tkinter event loop
root.mainloop()
```

**1.4 Setting Options for a Widget**

Widgets in Tkinter can have various options that determine their appearance and behavior. Let's set some options for a button widget.

```python
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Create a button widget with options
button = tk.Button(root, text="Click Me", fg="red", bg="yellow", padx=10, pady=5)

# Pack the button into the window
button.pack()

# Start the Tkinter event loop
root.mainloop()
```

**1.5 Command Binding**

Command binding allows us to associate a function with a widget event, such as a button click. Let's bind a function to a button click event.

```python
import tkinter as tk

# Define a function to be called on button click
def greet():
    print("Hello, Tkinter!")

# Create the main application window
root = tk.Tk()

# Create a button widget with command binding
button = tk.Button(root, text="Click Me", command=greet)

# Pack the button into the window
button.pack()

# Start the Tkinter event loop
root.mainloop()
```

**1.6 Event Binding**

Event binding allows us to bind a function to a specific event of a widget. Let's bind a function to the `<Button-1>` event (left mouse button click) of a button widget.

```python
import tkinter as tk

# Define a function to be called on button click
def greet(event):
    print("Hello, Tkinter!")

# Create the main application window
root = tk.Tk()

# Create a button widget
button = tk.Button(root, text="Click Me")

# Bind the function to the left mouse button click event
button.bind("<Button-1>", greet)

# Pack the button into the window
button.pack()

# Start the Tkinter event loop
root.mainloop()
```

**1.7 Label Widget**

The Label widget is used to display text or images on a frame or window. Let's create a label widget displaying some text.

```python
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Create a label widget with text
label = tk.Label(root, text="This is a Label")

# Pack the label into the window
label.pack()

# Start the Tkinter event loop
root.mainloop()
```

**1.8 Button Widget**

Buttons are essential for user interaction. Let's create a button widget and bind a function to its click event.

```python
import tkinter as tk

# Define a function to be called on button click
def button_click():
    print("Button Clicked")

# Create the main application window
root = tk.Tk()

# Create a button widget
button = tk.Button(root, text="Click Me", command=button_click)

# Pack the button into the window
button.pack()

# Start the Tkinter event loop
root.mainloop()
```

**1.9 Entry Widget**

The Entry widget is used to create text entry boxes. Let's create an entry widget for user input.

```python
import tkinter as tk

# Define a function to be called on pressing Enter in the entry widget
def on_enter(event):
    print("Text entered:", entry.get())

# Create the main application window
root = tk.Tk()

# Create an entry widget
entry = tk.Entry(root)

# Bind the function to the Enter key press event
entry.bind("<Return>", on_enter)

# Pack the entry widget into the window
entry.pack()

# Start the Tkinter event loop
root.mainloop()
```

These fundamental concepts of Tkinter provide a solid foundation for building more complex GUI applications in Python. Experiment with these examples to gain a deeper understanding of Tkinter's capabilities and unleash your creativity in GUI development.
