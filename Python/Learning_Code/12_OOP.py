# Object-Oriented Programming

#แนวคิดหลักของ OOP
#เขียนโปรแกรมโดยจำลองสิ่งต่างๆ ในชีวิตจริงเป็น “วัตถุ (Object)”
#เช่น: คน, สินค้า, รถ, ตัวละคร, ลูกค้า → มี "คุณสมบัติ" + "พฤติกรรม"

#🔧 คำศัพท์สำคัญ

#class	แบบพิมพ์ของ object
#object	ตัวจริงที่สร้างจาก class
#attribute	คุณสมบัติ (ข้อมูล)
#method	พฤติกรรม (ฟังก์ชันใน class)
#self	ตัวแทน object ตัวนั้น
#__init__	ตัวสร้าง (constructor) เรียกตอนสร้าง object

#ตัวอย่างพื้นฐาน: สร้าง class คน

class Person:                       # ประกาศ class
    def __init__(self, name, age):  # สร้าง object และเก็บข้อมูล
        self.name = name            # เก็บชื่อไว้ใน object
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

#สร้าง object และใช้งาน

p1 = Person("Tor", 25)
p1.say_hello()
