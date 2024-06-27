def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_word=count_word(text)
    char_dict=count_char(text)
    chars_sorted_list = chars_dict_to_sorted_list(char_dict)          
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_word} words found in the document""\n")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")
    


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
def sort_on(d):
    return d["num"]
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list    

main()
    

