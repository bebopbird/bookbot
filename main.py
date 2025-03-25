from stats import num_words, char_appear, sort_on, listing_dict
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    frankenstein = get_book_text(sys.argv[1])
    words_count = num_words(frankenstein)
    char_dict = char_appear(frankenstein)
    char_listdict = listing_dict(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for item in char_listdict:
        char = item["char"]

        count = item["count"]

        if char.isalpha():
            print(f"{char}: {count}")

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()

    return contents


main()