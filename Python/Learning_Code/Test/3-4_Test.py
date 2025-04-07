#1. 📐 เขียนโปรแกรมรับความกว้าง (width) และความยาว (length) ของสี่เหลี่ยม → แล้วคำนวณพื้นที่
#สูตร: area = width * length

width = int(input("Enter Width:"))
length = int(input("Enter Length"))

print(f"Area is {width * length}")


#2. 💸 เขียนโปรแกรมรับราคาสินค้าและจำนวนเงินที่มี → คำนวณจำนวนสินค้าที่ซื้อได้ และเงินทอน
#แสดงผลทั้งจำนวนที่ซื้อได้ (//) และเงินทอน (%)

money = int(input("Enter your money: "))
product = int(input("Enter your product price: "))

amount = money // product
change = money % product

print(f"You can buy {amount} item(s)")
print(f"Your change is {change} baht")
 
 
#3. 📊 เขียนโปรแกรมรับตัวเลข 3 ตัว แล้วหาค่าเฉลี่ย

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

average = (num1 + num2 + num3) / 3
print(f"Average is: {average}")