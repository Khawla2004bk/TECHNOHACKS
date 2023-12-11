# Communicates over the Fixer.io API.
import requests

def exchange_rates(api_key, base_currency="EUR"):
    url = f"http://data.fixer.io/api/latest?access_key=dac0061e483cc5057db44e3f32c523ae&base={base_currency}"

    try:
        response = requests.get(url)
        # Raise an HTTPError for bad responses
        response.raise_for_status()  
        data = response.json()
        # Returning the dictionary of exchange rates extracted from the JSON response
        return data["rates"]
    except requests.exceptions.RequestException as exep:
        print(f"Error fetching exchange rates: {exep}")
        return None