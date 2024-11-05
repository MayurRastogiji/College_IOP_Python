'''Write a code that accepts any number from 1 to 4999 both inclusive and give the corresponding roman number as output'''

roman_lst = [
    [1000, "M"],
    [900, "CM"],
    [500, "D"],
    [400, "CD"],
    [100, "C"],
    [90, "XC"],
    [50, "L"],
    [40, "XL"],
    [10, "X"],
    [9, "IX"],
    [5, "V"],
    [4, "IV"],
    [1, "I"]
]
def roman_converter(num):
    if 0 < num <5000:
        result = ""
        for value, symbol in roman_lst:
            while num >= value:
                result += symbol
                num -= value
        return result
    else:
        return "Out of bound"
num = int(input("Enter your number\n"))
output = roman_converter(num)
print(output)
# for key, values in roman_lst:
#     print(f"value of {key} is {values} in roman number system")