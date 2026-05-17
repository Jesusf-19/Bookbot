def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text

def word_counter(text):
    words = text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count


def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = word_counter(text)
    print(f"Found {word_count} total words")

main()