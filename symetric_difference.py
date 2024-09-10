a = set(input("Enter your str 1"))
b = input("Enter your str 2")
# pallindrome
# if a == b[::-1]:
#     print("str a is reversed of str b")
# else:
#     print("str a is not reversed of str b")
# #rotation
# if len(a) != len(b):
#     print("str a is not rotation of str b")
# c = b+b
# print(c)
# if a in c:
#     print("str b is rotation of str a")
# else:
#     print("str b is not rotation of str a")
a,b = set(a),set(b)
#symmetric difference
print(a-b)
#anagram
if a == b:
    print("sets are anagram.")
else:
    print("not a anagram")
# result = ""
# lenght = len(b)
# for i in range(lenght):
#     # print(b[i])
#     if a[i] != b[i]:
#         result = result + a[i]
#         break
# if result == "":
#     result = a[i+1]
# print(result)

