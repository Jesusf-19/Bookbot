from stats import word_counter, character_counter

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text



def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = word_counter(text)
    character_count = character_counter(text)
    print(f"Found {word_count} total words")
    print(f"{character_count}")

main()