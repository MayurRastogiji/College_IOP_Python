'''Take a list of even numbers of elements and return a list with second half of elements first than first half'''



lst = [1,2,3,4,5,6,7,8,9,10]

def shift(lst):
    if len(lst)%2 == 0:
        final_lst = lst[int(len(lst)/2):] + lst[:int(len(lst)/2)]
        return final_lst
    else:
        return "give even number of elements in list"

print(shift(lst))
