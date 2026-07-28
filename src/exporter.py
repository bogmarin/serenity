import json

def export(quotes):
    with open(
        "data/exports/quotes.json",
        "w",
        encoding="utf8"
    ) as f:
        json.dump(quotes, f, indent=4)
