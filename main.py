def main():
    book_path = "book/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_char(text)

    sorted_chars = sorted(num_char.items(), key=lambda item: item[1], reverse=True)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")

    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_char(text):
    char = {}
    for w in text:
       lower = w.lower()
       if lower in char:
           char[lower] += 1
       else:
            char[lower] = 1
    return char



main()
