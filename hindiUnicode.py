import unicodedata

def group_characters(text):
    result = []

    for char in text:
        if unicodedata.category(char).startswith('M'):
                result[-1] += char # result gives ["कि"]

        elif result and result[-1].endswith('्'):
            # attach next consonant  
            result[-1] += char
        else:
            result.append(char) # append gives ["क", "ि"]

    return result


# print(group_characters("किताब"))
# print(group_characters("नमस्ते"))
# print(group_characters("भारत"))
# print(group_characters("Hello दुनिया"))
print(group_characters("स्त"))