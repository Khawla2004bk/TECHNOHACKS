# Principal reasoning behind the currency conversion.
def convert_currency(amount, source_cur, target_cur, exchange_rates):
    if (source_cur not in exchange_rates):
        print("Invalid source currency.")
        return None
    elif (target_cur not in exchange_rates):
        print("Invalid target currency.")
        return None
    
    # Retrieving the exchange rates for the source and target currencies.
    source_rate = exchange_rates[source_cur]
    target_rate = exchange_rates[target_cur]

    converted_amount = amount * (target_rate / source_rate)
    return converted_amount