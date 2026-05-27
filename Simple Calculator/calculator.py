import os

# Get the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HISTORY_FILE = os.path.join(SCRIPT_DIR, "history.txt")

def show_welcome():
    """Prints the welcome banner to the user."""
    print("=================================")
    print("   Welcome to Python Calculator  ")
    print("    (Advanced Edition ✨)        ")
    print("=================================")

# --- Math Functions using Lambdas ---
# These replace standard 'def' functions with ultra-clean one-liners!
add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
# Ternary operator for division to handle zero safely in a lambda
divide = lambda a, b: "Error: Cannot divide by zero!" if b == 0 else a / b
power = lambda a, b: a ** b
modulo = lambda a, b: a % b

def save_history(record):
    """Saves a calculation string to history.txt"""
    # Append mode 'a' will create the file if it doesn't exist
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(record + "\n")

def read_history():
    """Reads and prints the history.txt file"""
    if os.path.exists(HISTORY_FILE):
        print("\n--- Calculation History ---")
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            print(file.read().strip())
        print("---------------------------")
    else:
        print("\n[No history found yet]")

def get_number(prompt, allow_ans=False, last_ans=None):
    """Helper function to get a float or the 'ans' keyword."""
    while True:
        user_input = input(prompt).strip().lower()
        if allow_ans and user_input == 'ans':
            if last_ans is None:
                print("Error: No previous answer available to use. Please enter a number.")
                continue
            return last_ans
        try:
            return float(user_input)
        except ValueError:
            print("Error: Please enter a valid number.")

# --- Main Application Logic ---
def main():
    show_welcome()
    last_ans = None
    
    while True:
        print("\n--- Menu ---")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Power (**)")
        print("6. Modulo (%)")
        print("7. View History")
        print("8. Exit")
        
        choice = input("\nSelect an option (1-8): ").strip()
        
        if choice == '8':
            print("Exiting calculator. Goodbye!")
            break
            
        elif choice == '7':
            read_history()
            continue
            
        elif choice in ['1', '2', '3', '4', '5', '6']:
            print("\n(Tip: Type 'ans' for the first number to use your previous result)")
            
            num1 = get_number("Enter first number: ", allow_ans=True, last_ans=last_ans)
            num2 = get_number("Enter second number: ", allow_ans=False)
                
            record = ""
            
            # Calculation Block using match/case
            match choice:
                case '1':
                    result = add(num1, num2)
                    record = f"{num1} + {num2} = {result}"
                case '2':
                    result = subtract(num1, num2)
                    record = f"{num1} - {num2} = {result}"
                case '3':
                    result = multiply(num1, num2)
                    record = f"{num1} * {num2} = {result}"
                case '4':
                    result = divide(num1, num2)
                    if type(result) == str: 
                        record = result # It's the error string
                    else:
                        record = f"{num1} / {num2} = {result}"
                case '5':
                    result = power(num1, num2)
                    record = f"{num1} ^ {num2} = {result}"
                case '6':
                    result = modulo(num1, num2)
                    record = f"{num1} % {num2} = {result}"
            
            # Display result
            print(f"\nResult: {record}")
            
            # If it wasn't an error, save it
            if "Error" not in record:
                save_history(record)
                last_ans = result # Save for 'ans'
        else:
            print("Invalid choice. Please select 1-8.")

# --- Program Entry Point ---
if __name__ == "__main__":
    main()
