import json

def load_json_file(path):
    with open(path) as json_file:
        return json.load(json_file)