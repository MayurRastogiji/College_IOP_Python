marks = (12,18,25,24,2,5,18,20,20,21)

def find_more_than_average(marks):
    average = sum(marks) / len(marks)
    count = sum([1 for mark in marks if mark > average])
    return count*100/len(marks)

def generate_frequency(marks):
    frequency = [0] * 26 
    print(len(frequency))
    for mark in marks:
        frequency[mark] += 1
    return frequency

def sort_marks(marks):
    return sorted(marks, reverse=True)

print(find_more_than_average(marks))
print(generate_frequency(marks))
print(sort_marks(marks))