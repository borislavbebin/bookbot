import os
import sys

from stats import get_words_num, get_symbols_count, get_sorted


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_contents = get_book_text(os.path.abspath("./books/frankenstein.txt"))
    words_count = get_words_num(book_contents)
    symbols = get_symbols_count(book_contents)
    sorted_symbols = get_sorted(symbols)

    # Final Report
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for symbol, count in sorted_symbols.items():
        print(f"{symbol}: {count}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
