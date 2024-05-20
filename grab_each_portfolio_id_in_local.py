def grab_each_portfolio_id_in_local(json_data):
    portfolio_id_in_json_data = []
    for each_portfolio_id in json_data.keys():
        existing_portfolio_id = each_portfolio_id.split(":")[0]
        portfolio_id_in_json_data.append(existing_portfolio_id)
    return portfolio_id_in_json_data
