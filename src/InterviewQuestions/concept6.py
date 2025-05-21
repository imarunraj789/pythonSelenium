def add(x,y):
    return x+y

add = lambda x, y : x+y

numbers = [1, 2, 3, 4, 5]

squared_numbers = map(lambda x : x*2, numbers)
print(numbers)
print(list(squared_numbers))

even_numbers = filter(lambda x : x % 2 == 0, numbers)
print(list(even_numbers))


num = [3,2,6,1]
print(num)
print(num[::-1]) #reverse the list
print(sorted(num))


