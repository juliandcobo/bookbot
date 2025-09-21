from stats import *

path_book = "./books/frankenstein.txt"

def get_book_text(path_book):
    with open(path_book) as f:
        file_contents = f.read()
        return file_contents

template = """============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------"""


def main():
    book_text = get_book_text(path_book)
    num_words(book_text)
    d = count_char(book_text)
    the_list = dict_sort(d)
    print(template)
    for char in the_list:
        print(f"{char['char']}: {char['num']}")
main()

