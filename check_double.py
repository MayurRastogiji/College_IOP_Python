def check_double(number):
    double_number = number * 2 
    return sorted(str(number)) == sorted(str(double_number))

print(check_double(125874))
print(check_double(123456))