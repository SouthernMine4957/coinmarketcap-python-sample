import re


def validate_portfolio_id(portfolio_id):
    pattern = "^[a-zA-Z0-9]+$"
    if re.match(
        pattern, portfolio_id
    ):  # If it matches alphanumeric. No symbols allowed
        print("Portfolio ID input is valid!")
        return True
    else:
        print("Invalid characters found in Portfolio ID")
        return False
