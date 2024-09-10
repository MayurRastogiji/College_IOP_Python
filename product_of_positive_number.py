def check_positive(x):
    y = 0
    for i in x:
        if i > 0:
            y += 1
        else:
            continue
    if y == len(x):
        return True
    else:
        return False
    
    
def product(x):
    i = None
    if check_positive(x):
        for n in range(len(x)):
            if x[n] == 7:
                i = n
            if n == len(x)-1 and i == None:    
                product = 1
                for j in x:
                    product *= j
                return product
            if n == len(x)-1 and i != None:
                y = x[i+1:]
                if y == []:
                    return -1
                else:
                    product = 1
                    for k in y:
                        product *= k
                    return product
            
        
def main():
    x = []
    for i in range(3):
        y = int(input("Enter a number: "))
        x.append(y)
    output = product(x)
    print(f"{output}")

if __name__ == "__main__":
    main()

# def find_product(a, b, c):
#   seven_index = None
#   if a == 7:
#     seven_index = 0
#   elif b == 7:
#     seven_index = 1
#   elif c == 7:
#     seven_index = 2

#   if seven_index is not None:
#     product = 1
#     if seven_index == 0:
#       product *= b * c
#     elif seven_index == 1:
#       product *= c
#     else:
#       product = 1
#   else:
#     product = a * b * c

#   if product == 1:
#     return -1
#   else:
#     return product

# # Get input from the user
# a = int(input("Enter the first positive integer: "))
# b = int(input("Enter the second positive integer: "))
# c = int(input("Enter the third positive integer: "))

# # Find and display the product
# result = find_product(a, b, c)
# print("The product is:", result)

     
    