def repeated_char(string, char):
    string = str(string)
    char = str(char)
    counter = 0
    
    for i in string:
        if char == i:
            counter += 1

    return counter
