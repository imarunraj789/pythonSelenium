str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str3 = "RahulShetty"

print(str[1])   #a

print(str[0:5])  # if you want substring in python

print(str+str1)   # concatenation

print(str3 in str)  # substring check

var = str.split(".")
print(var)
print(var[0])
str4 = " great "
print(str4.strip()) #Trims the leading and trailing white spaces
print(str4.lstrip()) #Trims left white spaces

print(str4.rstrip()) #Trims right white spaces