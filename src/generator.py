import random
from repository import load_quotes

def random_quote():
    quotes = load_quotes()

    if not quotes:
        return None

    return random.choice(quotes)
