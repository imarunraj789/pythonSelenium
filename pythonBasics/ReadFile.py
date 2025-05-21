file = open('Test.txt')

# Read all the contents of the file

# print(file.read(1)) #Read 1 byte or 1 character
# print(file.read(2)) #Read 2 byte or 2 characters

# print(file.readline()) #Reads 1st Line
# print(file.readline()) #Reads 2nd Line

AllLines = file.readlines() #Read all the lines from the file and stores in a list

for line in AllLines:
    print(line)
file.close()