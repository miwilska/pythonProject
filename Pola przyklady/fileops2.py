import os

directory = os.getcwd()

file = 't.txt'

my_file = os.path.join(directory, file)
print(my_file)
print(os.path.exists(my_file))
print(os.path.isfile(my_file))
print(os.path.isdir(my_file))


print('Current working dir: ' + os.getcwd())
# os.mkdir('mydir')
# os.rmdir('mydir')


print(os.getenv('PATH'))

