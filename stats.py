def get_num_words(file_contents):
   return len(file_contents.split())

def get_num_chars(file_contents):
    dict = {}
    for char in file_contents:
        lower = char.lower()
        if dict.get(lower):
            dict[lower] = dict[lower]+ 1
        else:
            dict[lower] = 1
    return dict

def sort_on(dict):
    return dict["num"]

def sort(dict):
    sorted = []
    for x in dict:
        if x.isalpha():
            sorted.append({ "name": x, "num": dict[x]})
    sorted.sort(reverse = True, key=sort_on)
    return sorted
