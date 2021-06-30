# with open('./textss.txt') as file_object:    
#     contents = file_object.read()   
   
#     print(contents)

# or you can loop through a file

# f = open('./textss.txt', "r")
# for x in f:
#   print(x)

#  with a simpler code open a file

f = open("textss.txt", "r")
print(f.read())

# read a single line

f = open("textss.txt", "r")
print(f.readline())

# read first five Characters
f = open("textss.txt", "r")
print(f.read(5))

# read and close file when you are done
f = open("textss.txt", "r")
print(f.readline())
f.close()