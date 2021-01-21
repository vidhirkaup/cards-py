class Person:

    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('person is created as ', self.name, ' with age ', self.age)

    def hello(self):
        print('hello ', self.name, ' Happy ', self.age)

    def __del__(self):
        print('person is destructed as', self.name, ' with age ', self.age)

person1 = Person('adam', 20)
person1.hello()
person1 = 50
print('person is ', person1)

print()

person2 = Person('david', 25)
person2.hello()
person2 = 50
print('person is ', person2)

