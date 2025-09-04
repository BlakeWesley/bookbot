def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

# Counts how many words are in the string
def count_words(string):
    words = string.split()
    number_of_words = len(words)
    return number_of_words


def main():
    filepath = 'books/frankenstein.txt'
    file_contents = get_book_text(filepath)
    number_of_words = count_words(file_contents)
    print(f"{number_of_words} words found in the document")

main()