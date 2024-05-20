import json


def read_local_json_file(json_local_file):
    # Open the existing JSON file (if it exists) and read its contents into the 'json_data' dictionary
    try:
        with open(json_local_file, "r") as opened_json_local_file:
            json_file_contents = opened_json_local_file.read()
            if json_file_contents:
                json_data = json.loads(json_file_contents)
                return json_data
            else:
                json_data = {}
                return json_data
    except FileNotFoundError:
        json_data = {}
        return json_data
