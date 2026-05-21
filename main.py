from stats import word_counter, character_counter, dict_sort
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = word_counter(text)
    char_counts = character_counter(text)
    sorted_chars = dict_sort(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        char = item["char"]
        num = item["num"]

        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ===============")

main()