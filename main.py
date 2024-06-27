def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_word=count_word(text)
    char_dict=count_char(text)
    #print(text)
    print(f"{num_word} words found in the document")
    print(char_dict)


def get_book_text(path):
    with open(path) as f:
        return f.read()
def count_word(text):
    words = text.split()
    return len(words)
def count_char(text):
    char_dict={}
    words=text.split()
    for word in words:
        lower_word=word.lower()
        chars=[x for x in lower_word]
        for char in chars:
            if char in char_dict:
                char_dict[char]+=1
            else:
                char_dict[char]=1
    return char_dict


main()
    

