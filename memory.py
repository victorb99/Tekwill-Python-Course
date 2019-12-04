import io

f = io.BytesIO()

f.seek(0, 2)
f.write('\nMYDATA\n')


print(f.getvalue())