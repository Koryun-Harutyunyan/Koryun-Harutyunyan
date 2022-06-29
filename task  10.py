filename = input("Enter filename: ")


def remove_punc(string):
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for elem in string:
        if elem in punc:
            string = string.replace(elem, "")
    return string


try:
    with open(filename, 'r', encoding="utf-8") as f:
        data = f.read()
    with open(filename, "w+", encoding="utf-8") as f:
        f.write(remove_punc(data))
    print("Removed punctuations from the file", filename)
except FileNotFoundError:
    print("File not found")