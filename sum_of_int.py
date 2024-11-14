'''Sum of integer in a given list only left the given number and number to its left and to its right'''

def dum(lst,n):
    total_sum = 0
    for i in range(len(lst)):
        if lst[(i+1) % len(lst)] != n and lst[i-1] != n and lst[i] != n: 
            total_sum += lst[i]
    return total_sum

lst = [1,2,3,4,5,2,3,4,5,6,7,8,9,10]
n = 5
print(dum(lst,n))