def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()

    words = file_content.split()
    count_words = len(words)

    character_dict = {}
    for word in file_content:
        for character in word.lower():
            if character in character_dict:
                character_dict[character] += 1
            else:
                character_dict[character] = 1
    
    print(character_dict)
    print(file_content)
    print(count_words)

main()