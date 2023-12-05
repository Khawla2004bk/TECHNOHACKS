# Currency Converter

A Python program that converts currency from one form to another using the latest exchange rates from the Fixer.io API.

## Project Structure
* converter.py: Contains the function for currency conversion.
* get_input.py: Contains the function for handling user input.
* handle_api.py: Contains the function for interacting with the Fixer.io API.
* main.py: Contains the main logic for calling functions and displaying results.

## Contributing
If you'd like to contribute to this project, please follow these steps:

1- Fork the repository.
2- Create a new branch for your feature or bug fix.
3- Make your changes.
4- Commit your changes.
5- Push to your fork and submit a pull request.

## Error Handling
The program may encounter errors if there are issues with the API request or if the currencies are not valid. Make sure to enter valid currencies and check for error messages in the console.

## How to Use

Follow these steps to use the Currency Converter:

1. **Install Dependencies:**
    - Make sure you have Python 3.x installed on your system.
    - Install the required dependencies using the following command:

    ```bash
    pip install requests
    ```

2. **Obtain API Key:**
    - Sign up for a free API key at [Fixer.io](https://fixer.io/signup).

3. **Configure API Key:**
    - Open `main.py` in a text editor.
    - Locate the line with `API_KEY = "YOUR_API_KEY"`.
    - Replace `"YOUR_API_KEY"` with your actual Fixer.io API key.

4. **Run the Program:**
    - Open a terminal or command prompt.
    - Navigate to the project directory.
    - Run the main script using the following command:

    ```bash
    python main.py
    ```

5. **Enter Conversion Details:**
    - When prompted, enter the amount to convert, source currency, and target currency.
    - Follow the on-screen instructions.

6. **View the Result:**
    - The program will display the converted amount.

Example:

```bash
Enter the amount to convert: 100
Enter the source currency: EUR
Enter the target currency: USD

Result: 100.00 EUR is equal to 117.45 USD

