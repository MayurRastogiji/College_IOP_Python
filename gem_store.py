gem_list = ["Emerald", "Ivory", "Jasper", "Ruby", "Garnet"]
price_list = [1760, 2119, 1599, 3920, 3999]

reqd_gem = input("Enter the name of the gem you want to purchase: ").split(", ")
reqd_quantity = input("Enter the quantity of the gem you want to purchase: ").split(", ")

for i in reqd_gem:
    if i not in gem_list:
        print("Total bill amount : -1")
        exit()

total_bill = 0
for i in range(len(reqd_gem)):
    total_bill += price_list[gem_list.index(reqd_gem[i])] * int(reqd_quantity[i])
print(f"Total bill amount : {total_bill}")