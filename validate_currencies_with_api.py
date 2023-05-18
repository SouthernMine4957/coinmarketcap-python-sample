def validate_currencies_with_api(fiat_currency, currencies_in_api):
    # Check if inputted currency symbol is present in currency symbols from API
    if fiat_currency in currencies_in_api:
        print("Currency symbol inputted matches a currency symbol in API!")
        return True
    else:
        print("Currency symbol inputted does not match any currency symbols in API!")
        return False