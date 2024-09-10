def calculate(adult, child, day):
    price_of_adult = 37550.0
    service_tax = 7.0
    price_of_child = (1/3) * price_of_adult
    discount = 0.9
    if day == 0:
        total_price = (adult * price_of_adult + child *
                       price_of_child) * (1 + service_tax/100)
    elif day == 1:
        total_price = (adult * price_of_adult + child *
                       price_of_child) * (1 + service_tax/100) * discount
    else:
        print("Invalid day")
    return total_price

def calculate(adult, child):
    price_of_adult = 37550.0
    service_tax = 7.0
    price_of_child = (1/3) * price_of_adult
    discount = 0.9
    total_price = (adult * price_of_adult + child *
                    price_of_child) * (1 + service_tax/100) * discount
    return total_price

def main():
    adult = int(input("Enter the number of adults: "))
    child = int(input("Enter the number of children: "))
    day = int(input("Enter the day of booking:(0 for weekdays and 1 for weekends) "))
    total_price = calculate(adult, child, day)
    # total_price = calculate(adult, child)
    print(f"Total price of the ticket is: {total_price:.2f}" )

if __name__ == "__main__":
    main()