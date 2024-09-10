# numberofcars = int(input("Enter the number of cars:"))
# print("Enter the last digit of the registration number:")
# x = list(map(int,input("Enter the values").split()))
# print("List of registration number", x)
# even = 0
# odd = 0
# for i in x:
#     if(i%2==0):
#         even +=1
#     else:
#         odd+=1
# day = int(input("Enter the date of day:"))
# if(day%2 == 0):
#     totalcharge = odd*200
# else:
#     totalcharge = even*200
# print(totalcharge)


# n=4
# for i in range(1,n+1):
#     for j in range(1,2*n):
#         if(i==n or i+j == n+1 or j-i == n-1):
#             print("*",end = " ")
#         else:
#             print(" ",end = " ")
#     print()


# def display_ranks(numbers):
#     sorted_numbers = sorted(numbers)
#     ranks = {num: sorted_numbers.index(num) + 1 for num in numbers}
#     for num in numbers:
#         print(f"Number {num} has rank {ranks[num]}")
# numbers = [15, 10, 25, 20, 5]
# display_ranks(numbers)


# def hollow_diamond_pattern(rows):
#   """Prints a hollow diamond pattern with the given number of rows.

#   Args:
#       rows: The number of rows in the diamond pattern (must be odd).
#   """
#   if rows % 2 == 0:
#     raise ValueError("Number of rows must be odd")

#   mid = rows // 2  # Integer division for center row

#   # Upper half
#   for i in range(mid):
#     spaces = " " * (mid - i)
#     stars = "*" * (2 * i + 1)
#     print(spaces + stars + spaces)

#   # Lower half (excluding the middle row)
#   for i in range(mid - 1, 0, -1):
#     spaces = " " * (mid - i)
#     stars = "*" * (2 * i + 1)
#     print(spaces + stars + spaces)

# # Example usage
# rows = 5
# hollow_diamond_pattern(rows)
# def right_angled_triangle(rows):
#   """Prints a right-angled triangle pattern with the given number of rows.

#   Args:
#       rows: The number of rows in the triangle pattern.
#   """
#   for i in range(1, rows + 1):
#     stars = "*" * i
#     print(stars)

# # Example usage
# rows = 5
# right_angled_triangle(rows)



n = int(input("Enter the number of rows"))
k = 0
for i in range(1, n+1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        if k == 0 or k == 2 * i - 2:
            print('*', end='')
        else:
            if i == n:
                print('*', end='')
            else:
                print(' ', end='')
    print()
