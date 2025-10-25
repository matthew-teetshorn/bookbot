import sys

from stats import get_num_words
from stats import get_char_count
from stats import sort_dict

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_file = sys.argv[1]

    file_contents = get_book_text(path_to_file)
    num_words = get_num_words(file_contents)
    char_count = get_char_count(file_contents)
    char_count_sorted = sort_dict(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in char_count_sorted:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")

main()