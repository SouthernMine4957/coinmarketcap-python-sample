import re


def validate_symbols_units(symbols_units):
    symbols_inputted = []  # Creates an empty list
    for symbol_unit in symbols_units.split(
        ","
    ):  # Splits all combination of symbol=units,symbol=units by the ',' into individual combination
        symbol, unit = symbol_unit.split(
            "="
        )  # Splits each combination of symbol=units into symbol and unit by '='
        if not re.match(
            "^[a-zA-Z0-9]+$", symbol
        ):  # If it does not match alphanumeric. No symbols allowed
            print("Invalid Symbol found:", symbol)
            return False
        try:
            float(unit)
        except ValueError:
            print("Invalid Unit found:", unit)
            return False
        symbols_inputted.append(
            symbol
        )  # Append all symbols found into a list into the initial empty symbols_inputted list
    print("Symbols & Units is valid!")
    return symbols_inputted  # Returns the list of symbols inputted into main.py
