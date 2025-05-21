class MyClass:
    @classmethod
    def class_method(cls):
        return "Class"

    def instance_method(self):
        return "Instance"

obj = MyClass()

print(obj.instance_method())
print(obj.class_method())
print(MyClass.class_method())
