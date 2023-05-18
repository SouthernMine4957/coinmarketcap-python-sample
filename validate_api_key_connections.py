from requests.exceptions import HTTPError, ConnectionError, Timeout, TooManyRedirects

def validate_api_key_connections(response):
    try: 
        response.raise_for_status()
        return True
    except (HTTPError, ConnectionError, Timeout, TooManyRedirects) as error:
        print("Invalid API key:", error)
        return False