class Calculator:
    num = 100
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when Object is created")
    def getData(self):
        print("I am now executing method in a class")
    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num

obj1 = Calculator(2,3)
obj1.getData()
print(obj1.num)
print(obj1.summation())

obj2 = Calculator(22,33)
obj2.getData()
print(obj2.num)
print(obj2.summation())