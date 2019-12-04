from functools import reduce
a=[1,2,3,4,5,6,7,8]

c = reduce(lambda x,y: x+y, map(lambda x: x*10, filter (lambda x: x %2 ==0, a)))

print (c)

c = []
for i in a:
    if i % 2 ==0:
        c.append(i)

print(c)
c = [x * 10 for x in c]
print(c)
print(sum(c))