def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_word=count_word(text)
    #print(text)
    print(num_word)


def get_book_text(path):
    with open(path) as f:
        return f.read()
def count_word(text):
    words = text.split()
    return len(words)



main()
    

