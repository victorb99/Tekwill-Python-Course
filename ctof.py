test_list_c = ['c','C']
test_list_f = ['f', 'F']

print('Do you want to convert in Celsius or Fahrenheit? Type C or type F')
t = input()
while True:
    if t in test_list_c: 
        print('Type Fahrenheit value you want to convert to Celsius')
        v = input()
        while True:
            if str.isdigit(v) == False:
                print('Incorect format. Please type a number')
                v = input()
            else:
                v = int(v)
                break
        celsius = (v - 32) * (5/9) 
        print('Temperature in Celsius is', celsius, ' C')
        break
                        
    elif t in test_list_f:
        print('Type Celsius value you want to convert to Fahrenheit')
        v = input()
        while True:
            if str.isdigit(v) == False:
                print('Incorect format. Please type a number')
                v = input()
            else:
                v = int(v)
                break
        fahrenheit = (v * (9 / 5)) + 32
        print('Temperature in Fahrenheit is', fahrenheit, ' F')
        break

    else:
        print('Incorrect format. Please type C or F to choose your input temperature')
        t = input()