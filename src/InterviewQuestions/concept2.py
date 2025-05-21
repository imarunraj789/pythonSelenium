class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def __init__(self,title):
        self.title = title

    def greet(self):
        return self.title + super().greet() + " Hello from Child"

c = Child("rahul shetty academy")
print(c.greet())