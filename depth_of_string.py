a = input("enter your string\n")
depth = 0
for i in a:
    if i == "(":
        depth += 1
    elif i == ")":
        depth -= 1
    else:
        print(f"depth of {i} is {depth}")