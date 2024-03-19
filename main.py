def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_letter_count(text)
    letter_count=breaker(letter_count)
    letter_count.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    breakdown(letter_count)
    print("--- End Report ---")

          


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_letter_count(text):
    text_lower= text.lower()
    letter_breakdown = {}
    for i in set(text_lower):
        if i.isalpha():
            letter_breakdown[i] = text_lower.count(i)
    return letter_breakdown

def breaker(dict):
    broken = list(dict.items())
    return broken

def sort_on(dict):
    return dict[1]

def breakdown(items):
    for i in items:
        print(f"The '{i[0]}' character was found {i[1]} times")

main()