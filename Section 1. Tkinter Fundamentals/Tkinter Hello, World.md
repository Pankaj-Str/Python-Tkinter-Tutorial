### Tkinter Hello, World!

Welcome to **codeswithpankaj.com**! In this tutorial, we'll walk you through the creation of the quintessential "Hello, World!" program using Tkinter, Python's standard GUI library. Let's dive in step-by-step to understand how to develop this simple yet fundamental application.

#### Creating a Window

Let's start by displaying a basic window on the screen. Below is the code snippet to achieve this:

```python
import tkinter as tk

# Create the application window
root = tk.Tk()

# Run the Tkinter event loop
root.mainloop()
```

By running this code, you'll see a window appear on your screen.

**How it works:**

1. **Import tkinter Module:** We import the `tkinter` module using the alias `tk`. This module contains all the classes and functions necessary to create graphical user interfaces.
   
2. **Create the Window:** We create an instance of the `Tk` class, which represents the main application window. This window is conventionally named `root`, although you can use any other name.

3. **Run the Event Loop:** The `mainloop()` method is called on the `root` object. This method starts the Tkinter event loop, ensuring the window remains visible and responsive to user interactions.

#### Troubleshooting

If you encounter an error like `ImportError: No module named Tkinter`, it indicates that the `tkinter` module is not available. In such cases, you can install the module using the following command:

```bash
sudo apt-get install python3-tk
```

#### Displaying a Label

Now, let's add some content to our window by placing a label widget. This label will display the text "Hello, World!". Here's the updated code:

```python
import tkinter as tk

# Create the application window
root = tk.Tk()

# Create a label widget
message = tk.Label(root, text="Hello, World!")

# Place the label on the window
message.pack()

# Run the Tkinter event loop
root.mainloop()
```

Upon running this code, you'll see the text "Hello, World!" displayed within the window.

**How it works:**

- We create a `Label` widget, specifying its parent window (`root`) and the text to display.
  
- The `pack()` method is called on the label widget to place it within the window. This method organizes widgets in a block, allowing them to dynamically adjust their size and position.

#### Fixing Blurry UI on Windows

Sometimes, you may notice that the text and UI appear blurry on Windows. To fix this issue, you can use the `ctypes` library to adjust the DPI awareness. Here's how to do it:

```python
from ctypes import windll

try:
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()
```

This code ensures that the application's UI renders correctly across different platforms.

### Summary

In this tutorial, you've learned how to create a basic Tkinter application that displays a window and a label. We've covered essential concepts such as creating windows, adding widgets, and running the event loop. Stay tuned for more tutorials on Tkinter and other Python topics on **codeswithpankaj.com**!
