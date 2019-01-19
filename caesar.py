def rotate_string(text,rot):

    output = ""
    for i in range(0,len(text)):
        output = output + rotate_character(text[i],rot)

    return output

def rotate_character(char, rot):

    if char.isalpha():
        new_position = ord(char) + int(rot)
        new_position %= 26
        return char(new_position)

    if char.isalpha() != True:
        return char