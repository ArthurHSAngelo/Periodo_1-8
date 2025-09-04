class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print('Ola, meu nome é ' + self.name)

p1 = Person('Arthur', 36)
p1.myfunc()
