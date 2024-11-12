y = int(6)
print(y)
n = 10
for i in range(2,n):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i, 'i is prime number')