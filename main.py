import sys
from stats import get_num_words, get_num_chars, sort

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main(argv):
    file_contents = get_book_text(argv)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {argv}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(file_contents)} total words")
    print("--------- Character Count -------")
    dict = get_num_chars(file_contents)
    sorted = sort(dict)
    for x in sorted:
        print(f'{x["name"]}: {x["num"]}')
    print("============= END ===============")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])
