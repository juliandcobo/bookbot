def num_words(file_contents):
    book_split = file_contents.split()
    num_words = 0
    for word in book_split:
        num_words += 1
    print(f"{num_words} words found in the document")

def sort_on(dict):
    return dict["num"]

def count_char(file_contents):
    book_lower = file_contents.lower()
    d = dict()
    for char in book_lower:
        if char.isalpha():
            d.setdefault(char, 0)
            d[char] += 1
        else:
            pass
    return d

def dict_sort(dictionary):
    char_list = [{"char": char, "num": count} for char, count in dictionary.items()]
    char_list.sort(reverse = True, key = sort_on)
    return char_list 
