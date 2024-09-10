num = input("Enter your string: \n")
for i in num:
    if i != '0' and i != '1':
        print("invalid binary string")
        break
if i == '0' or i == '1':
    print("valid binary string")