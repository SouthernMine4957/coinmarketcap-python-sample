def grab_each_symbol_unit_from_pair(symbol_unit_of_portfolio_id):
    each_symbol_from_pair = []
    each_unit_from_pair = []
    for each_symbol_unit in symbol_unit_of_portfolio_id.split(","):
        each_symbol, each_unit = each_symbol_unit.split("=")
        each_symbol_from_pair.append(each_symbol)
        each_unit_from_pair.append(each_unit)
    return each_symbol_from_pair, each_unit_from_pair
