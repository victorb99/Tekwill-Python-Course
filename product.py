print('What is the size of the list?', )
list_length = int(input())

a = []
#max = int()

for i in range(list_length):
    print('Add the number')
    b = int(input())
    a.append(b)

print(a)

def product_list():
    product = 1
    for i in range(list_length):
        product = a[i] * product
        
    print(product)

product_list()