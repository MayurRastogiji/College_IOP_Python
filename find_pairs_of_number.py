def find_pairs(lst, n):
    count = 0
    seen = set()
    for i in lst:
        if n - i in seen:
            count += 1
        seen.add(i)
    return count
lst = [1,2,7,4,5,6,0,3]
n = 6
print(find_pairs(lst,n))