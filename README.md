# Coinmarketcap-python-public-sample repo
This is a simple command-line tool used for tracking cryptocurrency portfolio. 
The tool allows the user to create portfolios, specifying multiple cryptocurrency symbols and their respective quantities, and display an approximate valuation in a selectable-fiat currency of each portfolio according to the current market prices.

# Below are some additional information about the tool:
- "main.py" contains the main flow of the program.
- The tool has 2 main commands.
    - “save” (create or overwrite a portfolio)
    - “show” (display an approximate valuation of a portfolio)
- "crypto.json" is a sample data file where the portfolios are saved to. The "Show" command grabs the data file from this json file. 
- Guidelines on how to use the coinmarket cap API can be found here: https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide.

# Guidelines to run the tool:
- Sign up for a free account to get an API key at https://pro.coinmarketcap.com/account/. You can then put in your API key into the "settings.json" file. 
- Run the “python main.py -h” command to show more help on how to use the tool. Below is how the help command will look like. 
- To run this tool in docker desktop, you can use the docker command “docker run -it coinmarketcappython”.

Usage: python main.py <command> [args]
Commands:
  save <portfolio_id> <Crypto Symbol=Units,Crypto Symbol=Units,...> - Save/Overwrite the cryptocurrency for a portfolio
  show <portfolio_id> <fiat_currency> - Display the approximate valuation of a portfolio
  help - Display this usage information

# Future Updates: 
Feel free to reach out to me if you have any feedback for me. I have received some feedback to combine and reorganise the functions in a better way for better readability and will update the code down the track. 