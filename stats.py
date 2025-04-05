def get_words_num(book_contents):
    words_count = len(book_contents.split())
    return words_count

def get_symbols_count(book_contents):
    words = book_contents.lower() # .replace(" ", "").replace("\n", "")
    symbols = {}
    for symbol in words:
        symbols[symbol] = symbols.get(symbol, 0) + 1
    return symbols

def get_sorted(characters):
    characters = dict(sorted(characters.items(), key=lambda item: item[1], reverse=True))
    return characters