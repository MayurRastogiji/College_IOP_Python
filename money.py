a1 = int(input("Enter number of 1rs coins: "))
a5 = int(input("Enter number of 5rs coins: "))
amount_payable = int(input("Enter the amount to pay: "))
b5 = amount_payable // 5
b1 = amount_payable % 5
amount_available = a1 + 5*a5
if amount_available < amount_payable:
    print("Insufficient amount")
else:
    if(b5 <= a5 and b1 <= a1):
        print("5rs coin given:", b5)
        print("1rs coin given:", b1)
        print("Available amount after payment: ", amount_available - amount_payable)
        print("Payment successful")
    elif(b5 > a5):
        b3 = 5*(b5 - a5) + b1
        print("5rs coin given:", a5)
        print("1rs coin given:", b3)
        print("Available amount after payment: ", amount_available - amount_payable)
        print("Payment successful")
    elif(b1 > a1):
        print("5rs coin given:", b5+1)
        print("1rs coin given: 0")
        print("Money to take back:", 5-b1)
        print("Available amount after payment: ", amount_available - amount_payable)
        print("Payment successful")
    else:
        print("Please refill entries, something went wrong...")


        