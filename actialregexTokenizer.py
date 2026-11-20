import re

text = input("Enter string to convert into tokens: ")

def tokenize(text):
    pattern = r"[\w\u0900-\u097F]+|[^\w\s]"
    tokens = re.findall(pattern, text)
    return tokens

tokenizedAns = tokenize(text)

print(tokenizedAns)