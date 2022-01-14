class User:
    def __init__(self, name):
        self.name = name

    def greetings(self):
        print(f'Hello {self.name}')

    def call(self):
        print(f'Calling {self.name}')

#Inheritance/Extension of class User
class Cust(User):
    def __init__(self, name, age):
        super(Cust, self).__init__(name)
        self.age = age
        self.bal = 0

    def set_bal(self, bal):
        self.bal = bal

    def greetings(self):
        print(f'Hello {self.name}, {self.bal}, age: {self.age}')


custo = Cust('Josh', 26)
custo.set_bal(20000)
custo.greetings()
custo.call()
