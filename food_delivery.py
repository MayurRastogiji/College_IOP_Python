def bill_B(food_Quantity_v, food_Quantity_N, price_v, price_N, delivery_charge):
        if food_Quantity_v < 0 or food_Quantity_N < 0 :
            return '-1'
        else:
            total = food_Quantity_v * price_v + food_Quantity_N * price_N + delivery_charge
            if total > 0:
                return total
            else:
                return '-1'  
def bill_s(food,food_Quantity, price_v,price_N, delivery_charge):
    if (food_Quantity < 0):
        return '-1'
    else:
        if food == 'V':
            total = food_Quantity * price_v + delivery_charge
            if total > 0:
                return total
            else:
                return '-1'
        elif food == 'N':
            total = food_Quantity * price_N + delivery_charge
            if total > 0:
                return total
            else:
                return '-1'

food = input("Enter the food you want to order: \nV for Veg\nN for Non-Veg\nB for both\n")
if food == 'B':
    food_Quantity_v = int(input("Enter the quantity of Veg food you want to order: "))
    food_Quantity_N = int(input("Enter the quantity of totalNon-Veg food you want to order: "))
elif food == 'V' or food == 'N':
    food_Quantity = int(input("Enter the quantity of food you want to order: "))
else:
    print("Invalid entry")
    exit()
price_v = 120
price_N = 150
distance = int(input("Enter distance of your house in kms:"))
if (0 <= distance < 3):
    delivery_charge = 0
elif (3 <= distance < 6):
    delivery_charge = 3
elif (6 <= distance): 
    delivery_charge = 6
else:
    print("Invalid entry")
    exit()
if food == 'B':
    total = bill_B(food_Quantity_v, food_Quantity_N, price_v, price_N, delivery_charge)
else:
    total = bill_s(food,food_Quantity, price_v, price_N, delivery_charge)
print("Total amount to pay: ", total)