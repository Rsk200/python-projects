# Number Guessing Game 🎮

A fun, interactive, and beginner-friendly Number Guessing Game built in Python. This project was created as a complete learning journey to master fundamental Python concepts.

## 📖 Description

The Number Guessing Game is a classic terminal-based program where the computer selects a random secret number, and the player attempts to guess it. After each guess, the game provides hints ("Too High!" or "Too Low!") and tracks the number of attempts it took to find the correct number. Once guessed, the player is asked if they'd like to play again.

## ✨ Features

- **Random Number Generation**: The game thinks of a new number every round.
- **Interactive Gameplay**: Hints guide the player to the correct answer.
- **Attempt Tracking**: Counts how many tries it takes to win.
- **Input Validation**: Prevents the game from crashing if you type text instead of numbers!
- **Replayability**: Automatically loops back for another game without having to restart the script.

## 🛠️ Technologies Used

- **Language**: Python 3.x
- **Standard Libraries**: `random`

## 🚀 Installation & Setup

1. **Install Python**: Ensure you have Python installed on your computer. You can download it from [python.org](https://www.python.org/).
2. **Download the File**: Save the `number_guessing.py` file to your computer.
3. **Open your Terminal/Command Prompt**: Navigate to the folder where you saved the file.

## 🎮 Usage

Run the game by typing the following command in your terminal:

```bash
python number_guessing.py
```

### Example Gameplay

```text
=======================================
  Welcome to the Number Guessing Game! 
=======================================
I am thinking of a number between 1 and 100.
Enter your guess: 50
Too Low! Try again.
Enter your guess: 75
Too High! Try again.
Enter your guess: 63
Congratulations! You guessed the number 63 in 3 attempts.

Do you want to play again? (yes/no): no
Thanks for playing! Goodbye.
```

## 🧠 Concepts Learned

Building this project teaches several foundational programming concepts:
- **Variables & Data Types**: Storing numbers, text, and true/false values.
- **I/O (Input/Output)**: Using `print()` and `input()` to talk to the user.
- **Type Casting**: Converting text strings into integers (`int()`).
- **Control Flow**: Using `if`, `elif`, and `else` to make decisions.
- **Loops**: Utilizing `while` loops for repeating tasks until a condition is met.
- **Functions**: Grouping code into modular blocks (`def`) for cleaner architecture.
- **Modules**: Importing standard libraries like `random`.
- **String Formatting**: Using `f-strings` to easily inject variables into text.

## 🔮 Future Improvements (Try adding these yourself!)

1. **Difficulty Levels**: Let the player choose between Easy (1-50), Medium (1-100), and Hard (1-1000).
2. **Limited Attempts**: Give the player only 10 guesses before they get a "Game Over".
3. **Score System**: Award points based on how quickly the player guesses correctly.
4. **Colored Text**: Use a library like `colorama` to make the "Too High" / "Too Low" hints red and the winning text green!

## 👨‍💻 Author

Created by a passionate Python student!
