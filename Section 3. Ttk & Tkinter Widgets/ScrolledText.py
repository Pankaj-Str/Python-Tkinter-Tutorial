import tkinter as tk
from tkinter import scrolledtext

# Create the main application window
root = tk.Tk()

# Create a scrolled text widget
scrolled_text = scrolledtext.ScrolledText(root, height=5, width=30)
scrolled_text.pack()

# Start the Tkinter event loop
root.mainloop()