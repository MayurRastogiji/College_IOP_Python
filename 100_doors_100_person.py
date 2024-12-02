doors = [0 for _ in range(100)]
for i in range(1,101):
    for j in range(i-1,100,i):
        doors[j] = not doors[j]
print([i+1 for i in range(100) if doors[i]])

