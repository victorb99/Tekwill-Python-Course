import shelve

f = shelve.open('MyShelveFile')
f['age'] = 10
f['name'] = 'Alice'
