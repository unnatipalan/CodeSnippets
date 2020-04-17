import os

#hows us all of the attributes and methods that we have access to within this module.
print(dir(os))

#print the current work directory
print(os.getcwd())

#to change the directory
#os.chdir('C:/Users/user/')

#list the files and folders within the current directory
print(os.listdir())

#creating a new file for read and write
fd = "abc.txt"

# popen() is similar to open()
file = open(fd, 'w')
file.write("Hello")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)

fd = "abc.txt"
file = open(fd, 'r')
text = file.read()
print(text)
os.close(file)
#NOTE: Error is thrown for the non-existence of the file or the permission privileges.





