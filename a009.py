string = input()

result = ""

for character in string:
    result += chr(ord(character) - 7)

print(result)