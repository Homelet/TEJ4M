import re


sentence = input()

digit = re.findall("[0-9]", sentence)
letters = re.findall("[a-zA-z]", sentence)

print("LETTERS {}\nDIGITS {}".format(letters.__len__(), digit.__len__()))
