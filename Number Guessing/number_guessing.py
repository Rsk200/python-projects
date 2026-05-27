import random

def display_welcome():
    """
    Prints the welcome message and instructions for the game.
    """
    print("=======================================")
    print("  Welcome to the Number Guessing Game! ")
    print("=======================================")
    print("I am thinking of a number between 1 and 100.")

def get_player_guess():
    """
    Takes user input, ensures it's a valid integer, and returns it.
    """
    while True:
        # Prompt the user for input
        guess_str = input("Enter your guess: ")
        
        # Check if the input consists only of digits (basic validation)
        if guess_str.isdigit():
            # Convert the string to an integer and return it
            return int(guess_str)
        else:
            print("Invalid input! Please enter a whole number.")

def play_game():
    """
    Handles the core logic for a single round of the game.
    """
    display_welcome()
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Variable to keep track of the number of attempts
    attempts = 0
    
    # Boolean variable to control the guessing loop
    is_guessing = True
    
    while is_guessing:
        # Get the player's guess
        guess = get_player_guess()
        
        # Increase the attempt counter by 1
        attempts += 1
        
        # Compare the guess to the secret number
        if guess < secret_number:
            print("Too Low! Try again.")
        elif guess > secret_number:
            print("Too High! Try again.")
        else:
            # If it's not too low and not too high, it must be exactly right!
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            is_guessing = False # This stops the while loop

def main():
    """
    The main entry point of the game, including the replay loop.
    """
    # Infinite loop to allow playing multiple times
    while True:
        play_game()
        
        # Ask if the player wants to play again
        replay = input("\nDo you want to play again? (yes/no): ").lower()
        
        # If the answer is not 'yes' or 'y', break out of the infinite loop
        if replay != "yes" and replay != "y":
            print("Thanks for playing! Goodbye.")
            break # Exits the while loop

# This ensures the game only runs if this file is executed directly
if __name__ == "__main__":
    main()
