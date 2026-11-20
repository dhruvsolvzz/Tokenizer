import unicodedata

text = "Hello नमस्ते"

for char in text:
    print(char ,hex(ord(char)), unicodedata.category(char))