def grab_each_symbols_in_api(json_data):
    symbols_in_api = []
    for crypto in json_data["data"]:
        symbol_in_api = crypto["symbol"]
        symbols_in_api.append(symbol_in_api)
    return symbols_in_api
