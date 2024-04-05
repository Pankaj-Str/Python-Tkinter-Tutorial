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