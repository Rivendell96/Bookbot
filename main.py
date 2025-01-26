def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()

    words = file_content.split()
    count_words = len(words)
    print(file_content)
    print(count_words)

main()