def check_multiple(ls):
    modified_ls = []
    for i in ls:
        if i % 5 == 0:
            modified_ls.append(i)
    return modified_ls

def check_sum(ls):
    modified_ls = []
    for i in ls:
        j = str(i)
        sum = 0
        for k in j:
            sum += int(k)
        if sum % 3 == 0:
            modified_ls.append(i)
        else:
            continue
    return modified_ls

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
ls = []
trim_1 = 0
trim_2 = 0
if num_1 > num_2:
    print(f"{num_1} is greater, it should be smaller than {num_2}")
    exit()
else:
    for i in range(num_1, num_2+1):
        ls.append(i)
    for i in range(len(ls)):
        if len(str(ls[i])) == 2:
            if trim_1 == 0:
                trim_1 = i
        if len(str(ls[i])) == 3:
            trim_2 = i
        else:
            continue
    print(ls)
    ls = ls[trim_1:trim_2]
    print(ls)
    ls = check_multiple(ls)
    print(ls)
    ls = check_sum(ls)
    print(ls)
    print(f"The largest number is {max(ls)}")
