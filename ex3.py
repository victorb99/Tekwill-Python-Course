import os

pwd = os.getcwd()

files = os.scandir(pwd)

for f in files:
    info = f.stat()
    print(info.st_uid, 'User identifier of the file')
    print(info.st_size, 'Size in bytes')
    print(info.st_time, 'Last accessed time')
    print(info.st_mtime, 'Last edited')

