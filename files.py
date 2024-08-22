# Write a program to read text file.

file1 = open("sample.txt","r")
data = file1.read()
print(data)
print()

file2 = open("myfile.txt","w")
str1 = 'Python'
file2.write(str1)
print()

file3 = open('sample.txt',"r+")
print(file3.readline(11))
print()

