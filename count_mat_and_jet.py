'''Count number of mat and jet in a string (case-insensitive) if number of mat and jet are equal return true else return false'''


str = "Jet on the Mat but mat is too long"
# str = "mat jet Jet Mat"

def boolean(str):
    str_1 = str.lower().split()
    mat_count = 0
    jet_count = 0
    for i in str_1:
        # print(i)
        if i == "mat":
            mat_count += 1
            # print(mat_count)
        if i == "jet":
            jet_count += 1
            # print(jet_count)

    if mat_count == jet_count:
        return True
    else:
        return False


if boolean(str):
    print("true")
else:
    print("false")