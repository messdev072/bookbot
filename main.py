def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_word=count_word(text)
    #char_dict=count_char(text)
    #print(text)
    print(f"{num_word} words found in the document")
    #print(char_dict)
    count_char(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()
def count_word(text):
    words = text.split()
    return len(words)
def count_char(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
    

main()
    

