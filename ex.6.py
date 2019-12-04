s = 0
for i in range(1000, 2300+1):
    if i % 5 == 0 or i % 7 == 0:
        s += i

print(s)
