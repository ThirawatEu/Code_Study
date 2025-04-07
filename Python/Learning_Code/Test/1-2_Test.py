#1. สร้างตัวแปรชื่อ name, age, is_student แล้ว print() ค่าทั้งหมดออกมา

name = "Tor"
age = 25 
is_student = True

print("Hello my name is", name,"In 10 years you will be",age + 10,"years old.")

#2. Tip เพิ่มเติม (ถ้าอยากลองเขียนแบบใหม่)
print(f"Hello my name is {name}. In 10 years you will be {age + 10} years old.")


#3. เขียนโปรแกรมรับอุณหภูมิ (Celsius) แล้วแปลงเป็น Fahrenheit
# สูตร: F = C * 9/5 + 32

celsius = int(input("Enter temperature(C):"))
print("Temperature:",celsius * 9 / 5 + 32 ,"Fahrenheit")

# Tip เพิ่มเติม (ถ้าอยากลองเขียนแบบใหม่)
print(f"Temperature: {celsius * 9 / 5 + 32} Fahrenheit")


