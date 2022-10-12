string = str(input("enter your string: "))

while True:
    char_num = int(input("enter your character that you want it to be removed: "))
    if char_num <= len(string):
        break

a = string[:char_num - 1]
b = string[char_num:]

print(a + b)