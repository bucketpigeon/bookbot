def main():
    book = "books/frankenstein.txt"
    text = book_text(book)
    num_words = word_count(text)
    num_chara = character_count(text)
    list_of_dicts = iterate_over_dict(num_chara)
    list_of_dicts.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of {book} ---")
    print(f"{num_words} words found in the document")
    for dictionary in list_of_dicts:
        print(f"The '{dictionary["letter"]}' character was found {dictionary["num"]} times")
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

def iterate_over_dict(dict):
    variable = []
    for i, j in dict.items():
        variable.append({"letter": i, "num": j})
    return variable

def sort_on(dict):
    return dict["num"]

main()