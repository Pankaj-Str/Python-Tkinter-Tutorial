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

**Tkinter Example: Simple Number Guessing Game**

In this example, we'll create a simple number guessing game using Tkinter. The objective of the game is to guess a randomly generated number within a specified range. The user will input their guess, and the game will provide feedback on whether the guess is too high, too low, or correct. Let's get started:

```python
import tkinter as tk
import random

# Function to check the user's guess
def check_guess():
    guess = int(guess_entry.get())
    if guess == secret_number:
        result_label.config(text="Congratulations! You guessed it right!")
    elif guess < secret_number:
        result_label.config(text="Too low! Try again.")
    else:
        result_label.config(text="Too high! Try again.")

# Function to start a new game
def new_game():
    global secret_number
    secret_number = random.randint(1, 100)
    result_label.config(text="")
    guess_entry.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("Number Guessing Game")

# Generate a random number for the game
secret_number = random.randint(1, 100)

# Create a label for instructions
instructions_label = tk.Label(root, text="Guess a number between 1 and 100:")
instructions_label.pack(pady=10)

# Create an entry widget for the user's guess
guess_entry = tk.Entry(root)
guess_entry.pack()

# Create a button to submit the guess
guess_button = tk.Button(root, text="Submit Guess", command=check_guess)
guess_button.pack(pady=5)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Create a button to start a new game
new_game_button = tk.Button(root, text="New Game", command=new_game)
new_game_button.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
```

In this game, a random number between 1 and 100 is generated at the start of each game. The user inputs their guess into the entry widget and clicks the "Submit Guess" button. The `check_guess()` function compares the user's guess with the secret number and updates the result label accordingly. If the guess is correct, the user is congratulated. If the guess is too high or too low, they are prompted to try again. The user can start a new game at any time by clicking the "New Game" button.

This example demonstrates how to create a simple interactive game using Tkinter, providing users with a fun and engaging experience. You can customize the game further by adding features such as score tracking, difficulty levels, or visual enhancements to make it even more enjoyable.
