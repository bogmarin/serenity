import json

FILE = "data/quotes.json"

def load_quotes():
    with open(FILE, encoding="utf8") as f:
        return json.load(f)
