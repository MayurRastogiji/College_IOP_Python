lst = input("Enter various numbers: ").split(", ")
lst.sort()
str = ""
for i in range(1,len(lst)+1):
    str += (lst[-i])
print(str)