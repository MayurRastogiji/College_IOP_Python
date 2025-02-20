'''
example :
input : 2[a]3[b]
output : aabbb
'''

a = input("Enter your String\n")
stack_n = []
stack_s = []
string = ""
for i in a:
    if i.isnumeric():
        stack_n.append(i)
        # string = ""
    elif i == "[":
        stack_s.append(string)
        string = ""
    elif i.isalpha():
        string += i
    elif i == "]":
        outcome = ""
        outcome += int(stack_n.pop()) * string
        string = stack_s.pop() + outcome
    else:
        print("Invalid Input" + i)
print(outcome)