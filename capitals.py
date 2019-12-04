def letters_count():
    print('Please write your text')
    input_text = input()
    count_lower = 0
    count_upper = 0

    for i in input_text:
        if (i.islower()):
            count_lower = count_lower + 1 
        elif (i.isupper()):
            count_upper = count_upper + 1
    print('There are {} uppercase letters'.format(count_upper))
    print('There are', count_lower, ' lowercase letters')

letters_count()
