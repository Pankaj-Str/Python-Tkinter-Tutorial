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