def largest_prime_factor(n):
    def is_prime(n):
        if n <= 1:
            return False
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True
        
    ls = []
    for i in range(1,n+1):
        # print(i)
        if n % i == 0 and is_prime(i):
            print("inside if",i)
            ls.append(i)
            print(ls)
    return max(ls)
    # return 6

def sum(n):
    sum = 0
    for i in range(n,n+9):
        sum += largest_prime_factor(i)
    return sum

print(sum(10))
            