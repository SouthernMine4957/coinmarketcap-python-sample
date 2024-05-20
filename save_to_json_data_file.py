import json


def save_to_json_data_file(portfolio_id, symbols_units, json_local_file, json_data):
    # Add the new portfolio_id and symbols_units to the 'json_data' dictionary
    json_data[portfolio_id] = symbols_units

    # Write the updated 'json_data' dictionary to the JSON file
    with open(json_local_file, "w") as updated_json_data:
        json.dump(json_data, updated_json_data, indent=4)
        print("Portfolio ID updated successfully")
