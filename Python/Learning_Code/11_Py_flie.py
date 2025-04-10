# การจัดการไฟล์ใน Python

# "r"	อ่านไฟล์ (read)
# "w"	เขียนไฟล์ใหม่ (write) ลบข้อมูลเก่าออกหมด
# "a"	เขียนต่อท้ายไฟล์ (append)
# "x"	สร้างไฟล์ใหม่ ถ้ามีอยู่แล้วจะ error
# "r+"	อ่าน + เขียน

# เขียนไฟล์ (write)

file = open("data.txt", "w")
file.write("Hello, Tor!\n")
file.write("Nice to meet you.\n")
file.close()

# อ่านไฟล์ (read)

file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# วิธีที่ปลอดภัยกว่า → ใช้ with

with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# file.read()        # อ่านทั้งหมด (string เดียว)
# file.readline()    # อ่านทีละบรรทัด
# file.readlines()   # อ่านทั้งหมดเป็น list ทีละบรรทัด
