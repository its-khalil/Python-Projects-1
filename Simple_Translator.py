def translate(word):
    output = ""
    for letter in word:
        if letter in "AEIOU":
            output += "Z"
        elif letter in "aeiou":
            output += "z"
        else:
            output += letter
    
    return  output.strip().title()

print(translate(input()))