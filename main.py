def count_words(file_contents):
   return len(file_contents.split())

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    file_contents = get_book_text("./books/frankenstein.txt")
    print(f"{count_words(file_contents)} words found in the document")

main()
