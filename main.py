def main():
    book = "books/frankenstein.txt"
    text = book_text(book)
    num_words = word_count(text)
    print(num_words)

def book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

main()