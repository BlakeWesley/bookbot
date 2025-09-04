# Counts how many words are in the string
# Returns Integer
def count_words(string):
    words = string.split()
    number_of_words = len(words)
    return number_of_words

# Returns a dictionary of the number of times each character (including spaces and symbols) appears in a string
# Dictionary of String -> Integer
def count_characters(string):
    characters = {}

    for word in string:
        for char in word:
            char = char.lower()
            if char not in characters:
                characters[char] = 0
            characters[char] += 1

    return characters

# Helper function for sorting by num
def sort_on(items):
    return items["num"]

# Returns a sorted list of dictionaries
def sorted_dicts(character_dict):
    # We need to first get our dictionary into a list of dictionaries.
    char_list = []
    for char in character_dict:
        new_dict = {"char": char, "num": character_dict[char]}
        char_list.append(new_dict)

    # Now, we need to sort our list
    char_list.sort(reverse=True, key=sort_on)

    return char_list