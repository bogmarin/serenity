from src.search import by_author

def test_search():
    quotes = [
        {"author": "Albert Einstein"}
    ]

    assert len(by_author(quotes, "Einstein")) == 1
