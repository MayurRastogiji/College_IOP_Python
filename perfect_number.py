#perfect number

# num = int(input("Enter your number"))
# ls = []
# for i in range(1,num):
#     if num%i == 0:
#         ls.append(i)
# if sum(ls) == num:
#     print("Perfect number")
# else:
#     print("Not a perfect number")

#strong number

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n*fact(n-1)
# num = input("Enter your number")
# ls = []
# for i in num:
#     ls.append(fact(int(i)))
# if sum(ls) == int(num):
#     print(f"{num} is a strong number")
# else:
#     print(f"{num} is not a strong number")

#prime number and prime factors

num = int(input("Enter your number"))
ls = []
for i in range(2,num):
    if num % i == 0:
        print("Not a prime number")
        break
for j in range(2,num):
    if num % i ==0:
        if i in ls:
            continue
        ls.append(i)
if i == num-1:
    i += 1
    print("Prime number")
    for j in range(2,num+1):
        if num % i ==0:
            if i in ls:
                continue
            ls.append(i)
for i in ls:
    if i == 2:
        continue
    for j in range(2,i):
        if i %j == 0:
            ls.remove(i)
            break

print(f"prime factors are {ls}")

    

