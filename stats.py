def num_words(file_contents):
    book_split = file_contents.split()
    num_words = 0
    for word in book_split:
        num_words += 1
    print(f"{num_words} words found in the document")



def count_char(file_contents):
    book_lower = file_contents.lower()
    d = dict()
    for char in book_lower:
        d.setdefault(char, 0)
        d[char] += 1
    return d
