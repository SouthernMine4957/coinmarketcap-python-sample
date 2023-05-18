def current_quoted_prices(show_json_string, fiat_currency):
    symbol_same_sorting = []
    quoted_prices = []
    for each_symbol in show_json_string['data']:
        quoted_price = show_json_string['data'][each_symbol]['quote'][fiat_currency]['price']
        symbol_same_sorting.append(each_symbol)
        quoted_prices.append(quoted_price)
    return symbol_same_sorting, quoted_prices