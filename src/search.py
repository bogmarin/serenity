def by_author(quotes, author):
    return [
        q for q in quotes
        if author.lower() in q["author"].lower()
    ]
