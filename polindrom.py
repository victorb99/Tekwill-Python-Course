print('Intorduceti un cuvant palindrom')
check_word = input()


while True:
    letters_list = list(check_word)
    #print(letters_list)
    reverse_letters = letters_list[::-1]
    palindrom = '' .join(reverse_letters)
    #print(palindrom)
    if check_word == palindrom:
        print(check_word, 'este un palindrom')
        break
    else:
        print(check_word, 'nu este un palindrom')
        print('Adauga alt cuvant')
        check_word = input()



