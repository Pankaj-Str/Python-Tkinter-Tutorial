**Section 2: Layout Management**

**2.1 Pack Geometry Manager**

The pack geometry manager organizes widgets in blocks before placing them in the parent widget. Let's see how to use the pack manager to arrange widgets on a window.

```python
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Create three buttons and pack them vertically
button1 = tk.Button(root, text="Button 1")
button1.pack()

button2 = tk.Button(root, text="Button 2")
button2.pack()

button3 = tk.Button(root, text="Button 3")
button3.pack()

# Start the Tkinter event loop
root.mainloop()
```

**2.2 Grid Geometry Manager**

The grid geometry manager allows you to place widgets in a grid-like layout within a container. Let's see how to use the grid manager to place widgets on a window.

```python
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Create three buttons and place them in a grid layout
button1 = tk.Button(root, text="Button 1")
button1.grid(row=0, column=0)

button2 = tk.Button(root, text="Button 2")
button2.grid(row=0, column=1)

button3 = tk.Button(root, text="Button 3")
button3.grid(row=1, column=0, columnspan=2)

# Start the Tkinter event loop
root.mainloop()
```

**2.3 Place Geometry Manager**

The place geometry manager allows you to precisely position widgets using the (x, y) coordinate system. Let's see how to use the place manager to position widgets within a container.

```python
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Create a label and place it at specific coordinates
label = tk.Label(root, text="Label at (50, 50)", bg="lightblue")
label.place(x=50, y=50)

# Create a button and place it relative to the label
button = tk.Button(root, text="Button below label")
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Start the Tkinter event loop
root.mainloop()
```

**2.4 Tkinter Widget Size**

You can control the size of widgets using the `height` and `width` properties or by using layout methods such as `pack`, `grid`, or `place`. Let's understand how to adjust the size of widgets.

```python
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Create a label with specified width and height
label = tk.Label(root, text="Resizable Label", bg="lightgreen", width=20, height=5)
label.pack()

# Create a button with fixed size using pack
button = tk.Button(root, text="Fixed Size Button")
button.pack(padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
```

Understanding layout management in Tkinter is crucial for creating well-organized and visually appealing GUI applications. Experiment with different geometry managers and widget sizes to design user interfaces that meet your application's requirements.
