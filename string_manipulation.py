'''Adding "ing" at the end of any single word given,
adding "ly" if the string is ending with "ing",
if the length of string is less than 3 leave as it is.'''

def manipulation(str):
    if len(str) < 3:
        output = str
    else:
        if str[-3:] == "ing":
            output = str + "ly"
        else:
            output = str + "ing"
    return output

str = input("Enter your word\n")
output = manipulation(str)
print(output)