class Person:
    name = 'adam'

    def __init__(self):
        print('person is created as ', self.name)

    def hello(self):
        self.name = 'david'
        print('person is ', self.name)

    def __del__(self):
        print('person is destructed as', self.name)


person = Person()
person.hello()
person.hello()

person = 50
print('person is ', person)
