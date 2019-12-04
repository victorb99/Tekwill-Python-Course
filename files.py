f = open('my_write_file', 'w+')
for i in range(5):
    f.write(f'Line_{i}\n')
    f.flush()

f.seek(0)
data = f.read()
print(data)
f.seek(0)
data = f.read()
f.close()