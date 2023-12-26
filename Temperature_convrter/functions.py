
def main():    
    while True:
        try:
            T = float(input("Enter the temperature to convert: "))
            # Exit the loop if temperature input is valid
            break
        except ValueError:
            print("Invalid input. Please enter a valid temperature value: ")
        
    while True:
        try:
            unit = input("Choose the unit to convert to; \"F\" for Fahrenheit and \"C\" for Celsius: ").upper()

            if unit == "F":
                T1 = (T - 32) * 5/9
                print(f"{T} F is equal to {T1:.2f} C")
                break

            elif unit == "C":
                T1 = (T * 9/5) + 32
                print(f"{T} C is equal to {T1:.2f} F")
                break

            else:
               print("Invalid unit. Please enter 'F' or 'C'.")
    
        
    
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()