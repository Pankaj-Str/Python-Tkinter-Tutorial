# import the Tkinter module
import tkinter as tk

# Create the application window
root = tk.Tk()

# Set the window title
root.title("Basic Example")

# Set the window size
root.geometry("300x200")

# Not Allow resizing both horizontally and vertically
root.resizable(False, False)

# Create a label widget
message = tk.Label(root, text="Hello, World!")

# Pack the label widget into the root window
message.pack()


# Run the Tkinter event loop
root.mainloop()
