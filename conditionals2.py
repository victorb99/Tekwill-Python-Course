print('Introduceti denumirea fisierului')
filename = input()
listfilename = filename.split('.')
extension = listfilename.pop()
if extension == 'py':
    print('Extensia fisierului este de tip Python')
else:
    print('Atentie, acesta nu este un fisier Python')