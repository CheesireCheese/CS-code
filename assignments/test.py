class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}") 
        

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.value = 0
    def increment(self):
        self.value += 1

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

mmb = Dog("a",67)
mmb.increment()
print(mmb.value)

memaybeo = Rectangle(6, 7)
print(memaybeo.area())

class BankAccount:
    def __init__(self):
        self.__balance = 0
    def deposit(self, ammount):
        self.__balance = ammount
    def withdraw(self, ammount):
        if ammount < self.__balance:
            self.__balance -= ammount
    def GetBalance(self):
        return self.__balance

bank = BankAccount()
bank.deposit(69420)
bank.withdraw(67)
bank.withdraw(9999999999999999999999999)
print(bank.GetBalance())