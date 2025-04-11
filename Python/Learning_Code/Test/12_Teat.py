# 1. 👤 สร้าง class ชื่อ Student มีคุณสมบัติ: name, grade
# แล้วสร้าง object นักเรียน 2 คน พร้อมแสดงชื่อและเกรด

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        
    def show_info(self):
        print(f"Name: {self.name}, Grade: {self.gpa}")

# สร้างนักเรียน 2 คน

s1 = Student("Tor", "A")
s2 = Student("Non", "B")

s1.show_info() # show_info() คือ method ไว้แสดงข้อมูลนักเรียน
s2.show_info()


# 2. 💸 สร้าง class Product มี name, price และ method show_info() ที่แสดงข้อมูลสินค้า

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        print(f"Product: {self.name}, Price: {self.price} baht")

# สร้างสินค้า

p = Product("Iphone", 30000)
p.show_info()


# 3. 🏦 สร้าง class BankAccount มี owner, balance และ method:
# deposit(amount)
# withdraw(amount)
# show_balance()    

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} baht deposited.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} baht withdrawn.")
        else:
            print("Insufficient funds.")

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance} baht")

# สร้างบัญชี
acc = BankAccount("Tor", 5000)

acc.show_balance()
acc.deposit(2000)
acc.withdraw(3000)
acc.withdraw(6000)
acc.show_balance()
