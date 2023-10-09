import os

path = '/path/to/target/file.txt'
start = 'path/to/start/directory'


relative_path = os.path.relpath(path, start)
print(relative_path)

print 'copy {} to {}'.format(key, dest_key)
