import os

# --- 1. Math Functions (Using Lambdas!) ---
# Lambdas are perfect for simple, one-line math formulas.
c_to_f = lambda c: (c * 9/5) + 32
f_to_c = lambda f: (f - 32) * 5/9
c_to_k = lambda c: c + 273.15
k_to_c = lambda k: k - 273.15

# Rankine Formulas
c_to_r = lambda c: (c * 9/5) + 491.67
r_to_c = lambda r: (r - 491.67) * 5/9
f_to_r = lambda f: f + 459.67
r_to_f = lambda r: r - 459.67
k_to_r = lambda k: k * 1.8
r_to_k = lambda r: r * 5/9

# --- 2. History System (List of Dictionaries & File I/O) ---
conversion_history = []
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HISTORY_FILE = os.path.join(SCRIPT_DIR, "history.txt")

def add_to_history(orig_val, orig_unit, new_val, new_unit):
    """Saves to local memory AND a text file."""
    # List of Dictionaries concept
    record = {"from_val": orig_val, "from_unit": orig_unit, "to_val": new_val, "to_unit": new_unit}
    conversion_history.append(record)
    
    # File I/O Concept
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(f"{orig_val} {orig_unit} = {new_val:.2f} {new_unit}\n")

def show_history():
    """Reads from the text file."""
    print("\n--- Saved History ---")
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            print(file.read().strip())
    else:
        print("No history found yet.")
    print("---------------------")

# --- 3. User Input Validation ---
def get_temperature():
    """Traps the user until they provide a valid float."""
    while True:
        try:
            return float(input("\nEnter temperature to convert: "))
        except ValueError:
            print("Error: Please enter a numeric value.")

# --- 4. Main Application Engine ---
def main():
    print("=" * 40)
    print("TEMPERATURE CONVERTER".center(40))
    print("=" * 40)
    
    while True:
        print("\n--- Menu ---")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. View History")
        print("6. Exit")
        
        choice = input("\nSelect an option (1-6): ").strip()
        
        if choice == '6':
            print("Stay cool! Goodbye.")
            break
            
        if choice == '5':
            show_history()
            continue
            
        if choice in ['1', '2', '3', '4']:
            temp = get_temperature()
            
            # Using match/case for clean routing
            match choice:
                case '1':
                    result = c_to_f(temp)
                    print(f"\nResult: {temp}°C = {result:.2f}°F")
                    add_to_history(temp, "C", result, "F")
                case '2':
                    result = f_to_c(temp)
                    print(f"\nResult: {temp}°F = {result:.2f}°C")
                    add_to_history(temp, "F", result, "C")
                case '3':
                    result = c_to_k(temp)
                    print(f"\nResult: {temp}°C = {result:.2f}K")
                    add_to_history(temp, "C", result, "K")
                case '4':
                    result = k_to_c(temp)
                    print(f"\nResult: {temp}K = {result:.2f}°C")
                    add_to_history(temp, "K", result, "C")
        else:
            print("Invalid selection. Please choose 1-6.")

if __name__ == "__main__":
    main()
