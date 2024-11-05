string = input("Enter a string: ")
lst_alphabet = []
for i in string:
    if i not in lst_alphabet:
        lst_alphabet.append(i)
        print(f"{string.count(i)}{i}", end="")