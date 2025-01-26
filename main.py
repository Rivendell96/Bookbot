def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    count_words = get_num_words(book_text)
    character_dict = get_chars_dict(book_text)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words} words found in the document")
    for name in character_dict:
        if name.isalpha():
            print(f"The '{name}' character was found {character_dict[name]} times")
    print("--- End report ---")


def get_chars_dict(text):
    character_dict = {}
    for word in text:
        for character in word.lower():
            if character in character_dict:
                character_dict[character] += 1
            else:
                character_dict[character] = 1

    return character_dict


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
        with open(path) as f:
            return f.read()

main()