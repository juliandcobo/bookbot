from stats import *
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]
#path_book = "./books/frankenstein.txt"



def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

#template = """============ BOOKBOT ============
#Analyzing book found at books/frankenstein.txt...
#----------- Word Count ----------
#Found 75767 total words
#--------- Character Count -------"""


def main():
    book_text = get_book_text(sys.argv[1])
    word_count = num_words(book_text)
    d = count_char(book_text)
    the_list = dict_sort(d)
    print(f""""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")

    for char in the_list:
        print(f"{char['char']}: {char['num']}")
main()

