def grab_each_currencies_in_api(json_data):
    currencies_in_api = []
    for currency in json_data['data']:
        currency_in_api = currency["symbol"]
        currencies_in_api.append(currency_in_api)
    return currencies_in_api