print('Type a number to find divisors')
test_number = int(input())

for i in range(1, test_number+1):
    if test_number % i ==0:
        print(i)
