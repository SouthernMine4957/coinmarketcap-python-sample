def validate_symbols_with_api(symbols_inputted, symbols_in_api):
    # Convert both lists to sets for faster comparison
    symbols_inputted_set = set(symbols_inputted)
    symbols_in_api_set = set(symbols_in_api)

    # Check if all symbols in symbols_inputted exist in symbol_in_api
    if symbols_inputted_set.issubset(symbols_in_api_set):
        print("Symbols inputted match symbols in API!")
        return True
    else:
        print("Symbols inputted do not match symbols in API")
        return False