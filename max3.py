

print('What is the size of the list?', )
list_length = int(input())

a = []
#max = int()

for i in range(list_length):
    print('Add the number' i)
    b = int(input())
    a.append(b)

print('Your list is', a)

#for i in range(list_length):
#    if a[i] > max:
#        max = a[i]

print('Maximum in the list is ', max(a))


