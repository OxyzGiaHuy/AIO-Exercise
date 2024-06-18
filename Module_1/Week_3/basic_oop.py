class MyClass:
    def __init__(self, value, number):
        self.__value = value

    def display(self):
        print(self.__value)

    def public_method(self):
        self.display()


obj = MyClass(20)
print(obj.__value)
obj.public_method()
obj.display()
