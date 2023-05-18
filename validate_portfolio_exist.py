def validate_portfolio_exist(portfolio_id, portfolio_id_in_json_data):
    if portfolio_id in portfolio_id_in_json_data:
        print("Portfolio ID inputted matches Portfolio ID in JSON data file!")
        return True
    else:
        print("Portfolio ID inputted does not match any Portfolio ID in JSON data file!")
        return False