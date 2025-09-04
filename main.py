import sys
from stats import count_words, count_characters, sorted_dicts

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    file_contents = get_book_text(filepath)

    # Get our analysis
    number_of_words = count_words(file_contents)
    chars_dict = count_characters(file_contents)
    sorted_char_list = sorted_dicts(chars_dict)

    # Format the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for pair in sorted_char_list:
        if pair["char"].isalpha():
            print(f"{pair["char"]}: {pair["num"]}")
    print("============= END ===============")

main()