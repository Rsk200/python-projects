def show_welcome():
    """Prints the welcome banner to the user."""
    print("=================================")
    print("   Welcome to Python Calculator  ")
    print("=================================")

# --- Math Functions ---
# We keep these separated so they are modular and reusable.
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


# --- Main Application Logic ---
def main():
    show_welcome()
    
    while True:
        print("\n--- Menu ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("\nSelect an operation (1-5): ")
        
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break  # Exit the while loop
            
        if choice in ['1', '2', '3', '4']:
            # 1. Input Validation Block
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Error: Please enter valid numbers only.")
                continue # Restart the loop from the top
                
            # 2. Calculation Block using match/case
            match choice:
                case '1':
                    print(f"\nResult: {num1} + {num2} = {add(num1, num2)}")
                case '2':
                    print(f"\nResult: {num1} - {num2} = {subtract(num1, num2)}")
                case '3':
                    print(f"\nResult: {num1} * {num2} = {multiply(num1, num2)}")
                case '4':
                    result = divide(num1, num2)
                    if type(result) == str: 
                        # Check if we returned the text error message
                        print(f"\n{result}")
                    else:
                        print(f"\nResult: {num1} / {num2} = {result}")
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")

# --- Program Entry Point ---
if __name__ == "__main__":
    main()
