# 1. 🔢 แสดงเลข 1 ถึง 10 ด้วย for loop

for i1 in range(1,11):
    print(i1)
    
    
# 2. 🧮 รับตัวเลขจากผู้ใช้ แล้วคำนวณผลรวมเลข 1 ถึงค่านั้น
# เช่น input = 5 → 1+2+3+4+5 = 15

i2 = 1
num1 = 0
num2 = 0

num = int(input("Enter Number:"))

while i2 <= num:
    num2 = i2 + num2
    i2 += 1
    print(num2)
    
#tip
print(f"Total is: {num2}")
    
    
#3. 🔁 รับข้อความจากผู้ใช้ และจำนวนรอบที่ต้องการแสดง แล้วใช้ลูปพิมพ์ข้อความนั้นซ้ำ

i3 = 1

String = input("Enter Word:")
num3 = int(input("Enter Number:"))

print("While Loop")

while i3 <= num3:
    print(String)
    i3 += 1

print("ForLoop")

for i4 in range(num3):
    print(String)
    
    
#4. 🛑 เขียนลูปที่ถามชื่อเพื่อนไปเรื่อยๆ จนผู้ใช้พิมพ์คำว่า "stop" → แล้วค่อยหยุด

while True:
    name = input("Enter your friend's name (or type 'stop' to end): ")
    if name.lower() == "stop":
        break
    print(f"Hello {name}!")

    