def get_list_from_dict(dictionary):
    lst = []
    for char, count in dictionary.items():
        new_dict = {"character": char, "count": count}
        lst.append(new_dict)
    return lst

def sort_on(dictionary):
    return dictionary["count"]

def get_sort_list(dictionary):
    lst = get_list_from_dict(dictionary)
    lst.sort(reverse=True, key=sort_on)
    return lst

def get_unique_chars_num(text):
    lowercase_characters = text.lower()
    character_counts = {}
    for character in lowercase_characters:
        if ord(character) >= 97 and ord(character) <= 122:
            character_counts[character] = character_counts.get(character, 0) + 1
    return character_counts

def get_number_of_words(text):
    words = text.split()
    return len(words)
    
def get_book(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)
    num_words = get_number_of_words(text)
    unique_characters_num = get_unique_chars_num(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    sorted_unique_characters_num = get_sort_list(unique_characters_num)
    for char in sorted_unique_characters_num:
        print(f"The '{char["character"]}' character was found {char["count"]} times")
    print("--- End report ---")


if __name__ == '__main__':
    main()