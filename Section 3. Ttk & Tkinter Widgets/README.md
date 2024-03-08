**Section 3: Ttk & Tkinter Widgets**

**3.1 Frame Widget**

The Frame widget is a container used to group other widgets together. It helps in organizing the layout of your GUI application.

```python
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Create a frame widget
frame = tk.Frame(root, bg="lightblue", bd=5)
frame.pack()

# Create widgets inside the frame
label = tk.Label(frame, text="Inside the Frame")
label.pack()

# Start the Tkinter event loop
root.mainloop()
```

**3.2 Text Widget**

The Text widget allows multi-line text input. It is useful for accepting larger amounts of text from users.

```python
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Create a text widget
text = tk.Text(root, height=5, width=30)
text.pack()

# Start the Tkinter event loop
root.mainloop()
```

**3.3 Scrollbar Widget**

The Scrollbar widget is used to add scrolling capability to widgets such as the Text widget. It allows users to navigate through content that exceeds the visible area.

```python
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Create a text widget
text = tk.Text(root, height=5, width=30)

# Create a scrollbar
scrollbar = tk.Scrollbar(root)

# Attach the scrollbar to the text widget
text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)

# Pack the widgets
text.pack(side=tk.LEFT, fill=tk.Y)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Start the Tkinter event loop
root.mainloop()
```

**3.4 ScrolledText Widget**

The ScrolledText widget combines a Text widget and a vertical Scrollbar widget into one, providing a convenient way to create a scrollable text area.

```python
import tkinter as tk
from tkinter import scrolledtext

# Create the main application window
root = tk.Tk()

# Create a scrolled text widget
scrolled_text = scrolledtext.ScrolledText(root, height=5, width=30)
scrolled_text.pack()

# Start the Tkinter event loop
root.mainloop()
```

**3.5 Separator Widget**

The Separator widget is used to visually separate groups of widgets in a GUI.

```python
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Create a separator widget
separator = tk.Separator(root, orient='horizontal')
separator.pack(fill='x')

# Start the Tkinter event loop
root.mainloop()
```

**3.6 Checkbox Widget**

A Checkbox widget allows users to select one or more options from a list of choices.

```python
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Create a checkbox widget
checkbox = tk.Checkbutton(root, text="Check Me")
checkbox.pack()

# Start the Tkinter event loop
root.mainloop()
```

**3.7 Radio Button Widget**

Radio buttons allow users to select one option from a list of mutually exclusive choices.

```python
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Create radio button widgets
option1 = tk.Radiobutton(root, text="Option 1", value=1)
option1.pack()

option2 = tk.Radiobutton(root, text="Option 2", value=2)
option2.pack()

# Start the Tkinter event loop
root.mainloop()
```

**3.8 Combobox Widget**

A Combobox widget is a combination of an Entry widget and a drop-down list, allowing users to select from a list of options or enter custom values.

```python
import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()

# Create a combobox widget
combo = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combo.pack()

# Start the Tkinter event loop
root.mainloop()
```

**3.9 Listbox Widget**

The Listbox widget displays a list of single-line text items, allowing users to select one or more items from the list.

```python
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Create a listbox widget
listbox = tk.Listbox(root)
listbox.pack()

# Add items to the listbox
for item in ["Item 1", "Item 2", "Item 3"]:
    listbox.insert(tk.END, item)

# Start the Tkinter event loop
root.mainloop()
```

**3.10 PanedWindow Widget**

The PanedWindow widget divides the space of a frame or window into panes, allowing users to resize them as needed.

```python
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Create a PanedWindow
paned_window = tk.PanedWindow(orient=tk.HORIZONTAL)
paned_window.pack(fill=tk.BOTH, expand=True)

# Add widgets to the PanedWindow
frame1 = tk.Frame(paned_window, bg="lightblue", width=100, height=200)
paned_window.add(frame1)

frame2 = tk.Frame(paned_window, bg="lightgreen", width=100, height=200)
paned_window.add(frame2)

# Start the Tkinter event loop
root.mainloop()
```

**3.11 Slider Widget**

The Slider widget, also known as the Scale widget, allows users to select a value from a range by moving a slider thumb.

```python
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Create a slider widget
slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
slider.pack()

# Start the Tkinter event loop
root.mainloop()
```

**3.12 Spinbox Widget**

The Spinbox widget allows users to select a value from a range by clicking arrow buttons to increment or decrement the value.

```python
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Create a spinbox widget
spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack()

# Start the Tkinter event loop
root.mainloop()
```

**3.13 Sizegrip Widget**

The Sizegrip widget is used to allow users to resize the entire application window by dragging the grip in the corner.

```python
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Create a frame
frame = tk.Frame(root)
frame.pack()

# Create a Sizegrip widget
sizegrip = tk.Sizegrip(frame)
sizegrip.pack(side=tk.RIGHT)

# Start the Tkinter event loop
root.mainloop()
```

**3.14 LabelFrame Widget**

The LabelFrame widget is used to group related widgets together with a border and optional title.

```python
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Create a label frame widget
label_frame = tk.LabelFrame(root, text="LabelFrame")
label_frame.pack()

# Create widgets inside the label frame
label = tk.Label(label_frame, text="Inside the LabelFrame

")
label.pack()

# Start the Tkinter event loop
root.mainloop()
```

**3.15 Progressbar Widget**

The Progressbar widget is used to indicate the progress of a long-running task.

```python
import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()

# Create a progressbar widget
progressbar = ttk.Progressbar(root, orient='horizontal', mode='determinate')
progressbar.pack()

# Start the Tkinter event loop
root.mainloop()
```

**3.16 Notebook Widget**

The Notebook widget, also known as a tabbed notebook or tabbed pane, allows users to switch between different pages or tabs.

```python
import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()

# Create a notebook widget
notebook = ttk.Notebook(root)
notebook.pack()

# Create tabs (pages) inside the notebook
frame1 = ttk.Frame(notebook)
notebook.add(frame1, text='Tab 1')

frame2 = ttk.Frame(notebook)
notebook.add(frame2, text='Tab 2')

# Start the Tkinter event loop
root.mainloop()
```

**3.17 Treeview Widget**

The Treeview widget displays tabular and hierarchical data in a tree-like structure, allowing users to expand or collapse nodes.

```python
import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()

# Create a Treeview widget
tree = ttk.Treeview(root)
tree.pack()

# Insert items into the treeview
tree.insert("", "end", text="Item 1")
tree.insert("", "end", text="Item 2")

# Start the Tkinter event loop
root.mainloop()
```

**3.18 Canvas Widget**

The Canvas widget is used for drawing shapes, lines, and images on a rectangular area.

```python
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Create a canvas widget
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# Draw a rectangle on the canvas
canvas.create_rectangle(50, 50, 150, 150, fill="blue")

# Start the Tkinter event loop
root.mainloop()
```

**3.19 Cursors**

You can change the mouse cursor when it hovers over a widget using the `cursor` option.

```python
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Create a button with a custom cursor
button = tk.Button(root, text="Hover Over Me", cursor="hand2")
button.pack()

# Start the Tkinter event loop
root.mainloop()
```

Understanding these Tkinter widgets and how to use them effectively will greatly enhance your ability to create versatile and interactive GUI applications in Python. Experiment with different widgets and explore their properties to create powerful user interfaces tailored to your specific needs.
