''' find greatest product of possible continuous numbers in a list of numbers '''

def product_of_continous_number(arr):
    max_product = 1
    current_product = 1
    negative_num = dict()
    for i in range(len(arr)):
        if arr[i] <= 0:
           negative_num[i] = arr[i]
    # print(negative_num)
    if len(negative_num) % 2 == 0:    
        for i in arr:
            # print("value : ",i)
            current_product = current_product * i
            # print("current_product : ",current_product)
            if current_product > max_product:
                max_product = current_product
    else:
        for i in negative_num:
            # print(negative_num[i])
            current_product = 1
            # print("index i : ",i, "value : ",arr[i])
            for j in range(0,i):
                # print("index : ",j, "value : ",arr[j])
                current_product = current_product * arr[j]
                if current_product > max_product:
                    max_product = current_product
            # print(max_product)
            current_product = 1
            for j in range(i+1,len(arr)):
                # print("index : ",j, "value : ",arr[j])
                current_product = current_product * arr[j]
                if current_product > max_product:
                    max_product = current_product
            # print(max_product)
        

    return max_product
lst = [1, 2, 5, -3, 0, 6, -7, 8]
ans = product_of_continous_number(lst)
print(f"The greatest product of possible continuous numbers in the list is: {ans}")
 