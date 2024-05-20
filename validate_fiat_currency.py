import re


def validate_fiat_currency(fiat_currency):
    pattern = "^[a-zA-Z]+$"
    if re.match(
        pattern, fiat_currency
    ):  # If it matches alphabets. No symbols or numerics allowed
        print("Fiat Currency input is valid!")
        return True
    else:
        print("Invalid characters found in Fiat Currency")
        return False
