def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    letter_count = count_letters(book_text)
    sorted_letters = sort_letters(letter_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    for letter_count in sorted_letters:
        letter = letter_count[0]
        count = letter_count[1]
        print(f"The '{letter}' character was found {count} times")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(string):
    return len(string.split())

def count_letters(string):
    letters = {}
    for char in string.lower():
        if char == " " or not char.isalpha():
            continue
        elif char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

    return letters

def sort_letters(letter_dict):
    letter_list = list(letter_dict.items())
    print(letter_list)
    print(list(letter_dict))
    return sorted(letter_list, reverse=True, key=lambda x: x[1])

main()
