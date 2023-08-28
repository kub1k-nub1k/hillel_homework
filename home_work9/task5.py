text = 'python is good language to code'
count = {}

for char in text:
    if char != ' ':
        count[char] = text.count(char)

print(count)