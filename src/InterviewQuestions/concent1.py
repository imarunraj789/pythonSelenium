# Lists are mutable, tuples are immutable

my_list = [1, 2, 3]
print(my_list)
my_list[0] = 100
my_list.append(4)
print(my_list)
my_list.pop(0)
print(my_list)
my_tuple = (1,2,3)

print(my_tuple)

my_tuple[0] = 100 #'tuple' object does not support item assignment

print(my_tuple)

x = 10 # int
y = 3.14 #float
d = {"a":1} # dictionary Key Value Pair
s = "hello" #String
z = True # booleanS
