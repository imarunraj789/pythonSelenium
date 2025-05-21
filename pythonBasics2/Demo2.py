values = [1,2,"rahul",4,5]

#List is a data type that allows multiple values and can be different data types

print(values[0]) #1
print(values[3]) #4
print(values[-1]) #Reference to last index

print(values[1:3]) #[2, 'rahul'] starting index and index-1 position

values.insert(3, "Shetty") #adding/inserting values in the specified index

print(values)

values.append("Last Value") #append the value at the end of the list
print(values)

values[2] = "RAHUL"

print(values)

del values[0]  # deletes the value from 1st index
print(values)

# Tuple Validation

val = (1,2,3,"rahul",4.5)  #braces () will be used for tuple
print(val)

# val[3] = "RAHUL"

print(val) #TypeError: 'tuple' object does not support item assignment


# Dictionary

dic = {"a":2, 4:"bcd", "c":"Hello World"}

print(dic[4])
print(dic["c"])
print(dic["a"])

dict = {}

dict["firstName"] = "Rahul"
dict["lastName"] = "Shetty"
dict["gender"] = "Male"

print(dict)
print(dict["lastName"])
