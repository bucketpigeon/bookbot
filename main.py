def main():
    book = "books/frankenstein.txt"
    text = book_text(book)
    num_words = word_count(text)
    num_chara = character_count(text)
    
    print(f"--- Begin report of {book} ---")
    print(f"{num_words} words found in the document")
    for letter in num_chara:
        num = num_chara[letter]
        print(f"The '{letter}' character was found {num} times")
    print("--- End report ---")

def book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    char = text.lower()
    char_dict = {}
    for i in char:
        if i in char_dict:
            char_dict[i] += 1
        else:
            if i.isalpha() == True:
                char_dict[i] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

main()