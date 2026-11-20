text = "Hello नमस्ते"
#ord(char)   gives ascii value of char
encodedString = []
for char in text:
    encodedString.append(hex(ord(char)))

print (encodedString)

decodedString = []

for char in encodedString:
    decodedString.append(chr(int(char, 16)))

result = "".join(decodedString)
print(result)