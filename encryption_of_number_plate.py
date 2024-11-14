'''Take car number plate as input and add it into a list.
XXXX-YYYY it should be in this format. In which XXXX is alphanumeric and there is either 1 aplhanumeric or 2 and YYYY is numeric.
encryption format is based on number of alphanumeric characters in XXXX.
CASE 1: If there is 1 alphanumeric character then rotate YYYY one time towards right and append it with alphabets in XXXX, then add it to the list.
CASE 2: If there are 2 alphanumeric characters then rotate YYYY two times towards right and append it with alphabets in XXXX, then add it to the list.'''
def check_alpha_numeric(string):
    count = 0
    for i in string:
        if i.isalpha():
            count += 1
    if count == 1 or count == 2:
        return True
    else: 
        return False

def encryption_of_number_plate(lst):
    enc_lst = []
    for i in lst:
        if check_alpha_numeric(i):
            alpha = ''
            num = i[5:]
            for j in i:
                if j.isalpha():
                     alpha += j
                else:
                    break
            if len(alpha) == 2:
                num = num[-2:] + num[:-2]
            elif len(alpha) == 1:
                num = num[1:] + num[0]
            car_number = alpha + num
            enc_lst.append(car_number)
    return enc_lst

lst = ['GT21-1011','S621-9699','GT21-1011','SA21-9699','G221-1011','S621-9699']
enc_lst = encryption_of_number_plate(lst)
print(enc_lst)

            