#1. 🏥 รับอุณหภูมิจากผู้ใช้ → ถ้าเกิน 37.5 ให้แสดงว่า "คุณอาจเป็นไข้"
#ถ้าไม่เกิน ให้แสดงว่า "อุณหภูมิปกติ"

tem = float(input("Enter your Temperature:"))

if tem > 37.5:
    print("You have a fever.")

else:
    print("Your temperature is normal.")
    

#2 🧾 รับคะแนนสอบจากผู้ใช้ → แล้วแสดงผลเกรด A B C D F (ตามช่วงคะแนนที่กำหนด)

score = int(input("Enter your score:"))

if score >= 80:
    print("You got A")

elif score >= 70:
    print("You got B")
    
elif score >= 60:
    print("You got C")
    
elif score >= 50:
    print("You got D")
    
else:
    print("You Failed")
    
    
#3. 🚗 รับอายุผู้ใช้ → ถ้าอายุ 18 ปีขึ้นไป แสดงว่า "คุณสามารถขับรถได้"
#ถ้าอายุน้อยกว่า แสดงว่า "ยังไม่สามารถขับรถได้"

age = int(input("Enter your age:"))

if age >= 18:
    print("You can drive.")

else:
    print("Your age is too young.")