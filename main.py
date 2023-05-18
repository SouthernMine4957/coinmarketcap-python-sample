from requests import Session
from validate_api_key_connections import validate_api_key_connections
from validate_portfolio_id import validate_portfolio_id
from validate_symbols_units import validate_symbols_units
from grab_each_symbols_in_api import grab_each_symbols_in_api
from validate_symbols_with_api import validate_symbols_with_api
from read_local_json_file import read_local_json_file
from save_to_json_data_file import save_to_json_data_file
from validate_fiat_currency import validate_fiat_currency
from grab_each_currencies_in_api import grab_each_currencies_in_api
from validate_currencies_with_api import validate_currencies_with_api
from grab_each_portfolio_id_in_local import grab_each_portfolio_id_in_local
from validate_portfolio_exist import validate_portfolio_exist
from grab_symbol_unit_belonging_to_portfolio_id import grab_symbol_unit_belonging_to_portfolio_id
from grab_each_symbol_unit_from_pair import grab_each_symbol_unit_from_pair
from convert_symbols_list_to_string import convert_symbols_list_to_string
from current_quoted_prices import current_quoted_prices
from calculate_prices import calculate_prices
import json
import argparse

with open('settings.json') as f:
    settings = json.load(f)

# Settings from the settings.json file
# In CICD, there's a transform json to update the settings.json file if any values were to be different in each environment or when handling secrets
sandbox_api_key = settings['sandbox_api_key']
api_key = settings['api_key']
sandbox_url = settings['sandbox_url']
map_url = settings['map_url']
fiet_map_url = settings['fiet_map_url']
quotes_url = settings['quotes_url']
json_local_file = settings['json_local_file']

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': api_key,
  'Accept-Encoding': 'deflate, gzip',
}

session = Session()
session.headers.update(headers)

def help ():
    print("Usage: python main.py <command> [args]")
    print("")
    print("Commands:")
    print("  save <portfolio_id> <Crypto Symbol=Units,Crypto Symbol=Units,...> - Save/Overwrite the cryptocurrency for a portfolio")
    print("  show <portfolio_id> <fiat_currency> - Display the approximate valuation of a portfolio")
    print("  help - Display this usage information")
    print("")
    print("Please also ensure that your API Key is in the settings.json file")

def save(portfolio_id, symbols_units):
  try:
    # Ensures that the Portfolio ID is only made of alphanumerics
    if validate_portfolio_id(portfolio_id) == False:
       return

    # Ensures that the symbols are alphanumeric and that units are float
    symbols_inputted = validate_symbols_units(symbols_units)
    if symbols_inputted == False:
      return

    # Initiate the API call
    api_response = session.get(map_url) 

    # Ensures that the API key works and that the connection has no issues
    if validate_api_key_connections(api_response) == False:
       return

    # Deserialize JSON string from the API call
    json_string = json.loads(api_response.text) 

    # Grab each symbols from the JSON string
    symbols_in_api = grab_each_symbols_in_api(json_string) 

    # Ensures that the inputted symbols all matches the one present in the symbols from the API call
    if validate_symbols_with_api(symbols_inputted, symbols_in_api) == False:
       return

    # Reads the existing JSON data file
    json_data = read_local_json_file(json_local_file) 

    # Saves the JSON into the local JSON data file
    save_to_json_data_file(portfolio_id, symbols_units, json_local_file, json_data)

  except Exception as e:
    print("An error occurred:", e)
    return
  
def show(portfolio_id, fiat_currency):
  try:
    # Ensures that the Portfolio ID is only made of alphanumerics
    if validate_portfolio_id(portfolio_id) == False:
        return

    # Ensures that the Portfolio ID is only made of alphabets
    if validate_fiat_currency(fiat_currency) == False:
       return

    # Reads the existing JSON data file
    json_data = read_local_json_file(json_local_file) 

    # Grab the Portfolio ID from the local JSON data file for comparing with the inputted Portfolio ID
    portfolio_id_in_json_data = grab_each_portfolio_id_in_local(json_data)

    # Ensures that Portfolio ID exist in the current JSON data file
    if validate_portfolio_exist(portfolio_id, portfolio_id_in_json_data) == False:
       return

    # Initiate the API call
    api_response = session.get(fiet_map_url) 

    # Ensures that the API key works and that the connection has no issues
    if validate_api_key_connections(api_response) == False:
       return

    # Deserialize JSON string from the API call
    json_string = json.loads(api_response.text) 

    # Grab each currencies from the JSON string
    currencies_in_api = grab_each_currencies_in_api(json_string) 
    
    # Ensures that the inputted currency symbol matches the one present in the currency symbols from the API call
    if validate_currencies_with_api(fiat_currency, currencies_in_api) == False:
       return

    # Grab the Symbol Unit pairs that belong to the portfolio ID
    symbol_unit_of_portfolio_id = grab_symbol_unit_belonging_to_portfolio_id(json_data, portfolio_id)

    # Grab each Symbols and each Units from the Symbol Unit pairs that belong to the portfolio ID
    each_symbol_from_pair, each_unit_from_pair = grab_each_symbol_unit_from_pair(symbol_unit_of_portfolio_id) 

    # Convert the list of symbols into a comma separated string
    symbols_string = convert_symbols_list_to_string(each_symbol_from_pair) 

    # Prepare parameters for the latest quote API call
    parameters = {'symbol':symbols_string,'convert':fiat_currency} 

    # Run the latest quotes API call
    show_api_response = session.get(quotes_url, params=parameters) 

    # Deserialize JSON string from the API call
    show_json_string = json.loads(show_api_response.text) 

    # Show the current Market Price of each of the crypto currency in the inputted fiat currency
    symbol_same_sorting, quoted_prices = current_quoted_prices(show_json_string, fiat_currency)

    # Calculates the pricing of each cryptocurrency and also add them all together and then print the result
    calculate_prices(symbol_same_sorting, each_unit_from_pair, quoted_prices)

  except Exception as e:
    print("An error occurred:", e)
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    save_parser = subparsers.add_parser("save")
    save_parser.add_argument('portfolio_id', type=str, help='2nd arg of the save command requires a new or existing portfolio id')
    save_parser.add_argument('symbols_units', type=str, help='3rd arg of the save command requires symbol and quantity in this format Crypto Symbol=Units,Crypto Symbol=Units...')

    show_parser = subparsers.add_parser("show")
    show_parser.add_argument('portfolio_id', type=str, help='2nd arg of the show command requires an existing portfolio id')
    show_parser.add_argument('fiat_currency', type=str, help='3rd arg of the show command requires a fiat currency symbol (e.g. USD, EUR)')

    help_parser = subparsers.add_parser("help")

    save_parser.set_defaults(func=save)
    show_parser.set_defaults(func=show)
    help_parser.set_defaults(func=help)

    args = parser.parse_args()

    if args.command == 'save':
      save(args.portfolio_id, args.symbols_units)
    elif args.command == 'show':
      show(args.portfolio_id, args.fiat_currency)
    else:
      help()