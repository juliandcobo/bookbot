from stats import *

path_book = "./books/frankenstein.txt"

def get_book_text(path_book):
    with open(path_book) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text(path_book)
    num_words(book_text)
    d = count_char(book_text)
    print(d)
main()

