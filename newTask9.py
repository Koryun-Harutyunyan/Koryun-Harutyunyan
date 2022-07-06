filename = input("Enter filename: ")


def remove_punc(string):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for elem in string:
        if elem in punc:
            string = string.replace(elem, "")
    return string


def replace_letters(string):
    letter = 'a'
    for elem in string:
        if elem in letter:
            string = string.replace(elem, "u")
    return string


try:
    with open(filename, 'r', encoding="utf-8") as f:
        data = f.read()
    with open(filename, "w+", encoding="utf-8") as f:
        f.write(remove_punc(data))
        f.write(replace_letters(data))
    print("Removed punctuations from the file", filename)
except FileNotFoundError:
    print("File not found")
