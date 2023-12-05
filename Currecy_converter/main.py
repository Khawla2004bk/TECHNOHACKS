# A simple currency converter program using Fixer.io API.

# Import necessary functions from other modules
from api_handler import exchange_rates
from currency_converter import convert_currency
from user_input import get_input

def main():
    # Step 1: Get API key and exchange rates
    api_key = "dac0061e483cc5057db44e3f32c523ae" 
    rates = exchange_rates(api_key)

    # Step 2: Get user input for conversion
    if rates:
        amount, source_cur, target_cur = get_input()

        # Step 3: Perform currency conversion
        if amount is not None:
            converted_amount = convert_currency(amount, source_cur, target_cur, rates)
        
            # Step 4: Display the result
            if converted_amount is not None:
                # Proceed with currency conversion
                print(f"Converting {amount} from {source_cur} to {target_cur}...")
                print(f"{amount} {source_cur} is equal to {converted_amount:.2f} {target_cur}")
            else:
                print("Invalid input. Exiting.")

if __name__ == "__main__":
    main()