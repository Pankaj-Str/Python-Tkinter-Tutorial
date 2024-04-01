# import the Tkinter module
import tkinter as tk

# Create the application window
root = tk.Tk()

# button function print helloword

def hello():
    print("Hello, World!")

# print hellomsg into label
def hellomsg():
    message.config(text="congratulations, you clicked the button!")

# print hellomsg into label
def byemsg():
    message.config(text="Good Bye, World!")

# button widget

button1 = tk.Button(root, text="Hello" ,fg="red", bg="yellow", padx=20, pady=20 , command=hellomsg)


button2 = tk.Button(root, text="Bye" ,fg="red", bg="yellow", padx=20, pady=20 , command=byemsg)

# Set the window title
root.title("Basic Example")

# Set the window size
root.geometry("500x400")

# Not Allow resizing both horizontally and vertically
root.resizable(False, False)

# Create a label widget
message = tk.Label(root, text="Hello, World!")

# Pack the label widget into the root window
message.pack()

# button widget
button = tk.Button(root, text="Click Me!" ,fg="red", bg="yellow", padx=20, pady=20 , command=hello)

# Pack the button widget into the root window
button.pack()

button1.pack()
button2.pack()


# Run the Tkinter event loop
root.mainloop()
