def ducci_sequence(x):
    end_list = []
    check = 0
    while check != 1:
        temp_list = []
        for i in range (len(x)):
            diff = abs(x[i] - x[(i+1)%len(x)])
            temp_list.append(diff)
        end_list.append(temp_list)
        x = temp_list
        for i in x:
            if i == 0 :
                pass
            else:
                check += 2
        if check == 0:
            check = 1
        else:
            check = 0
    return end_list

x = [0, 653, 1854, 4063]
result = ducci_sequence(x)
n = int(input(f"Enter the number of process you want to process, it should be less than {len(result)}\n"))
print(result[n-1])
            