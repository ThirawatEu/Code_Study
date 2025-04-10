#1. 📝 สร้างไฟล์ชื่อ friends.txt แล้วเขียนชื่อเพื่อน 3 คนลงไป (แยกบรรทัด)

f = open("friends.txt", "w")
f.write("Tor \nNon \nY ")
f.close()

# tip
# แบบใช้ writelines() กับ list:

with open("friends.txt", "w") as f:
    f.writelines(["Tor\n", "Non\n", "Y\n"])
    
# หรือแบบที่ G ชอบใช้ (อ่านง่ายสุด):

#with open("friends.txt", "w") as f:
#    f.write("Tor\n")
#    f.write("Non\n")
#    f.write("Y\n")


#2. 📖 อ่านข้อมูลจาก friends.txt แล้วแสดงชื่อแต่ละคนออกมาทีละบรรทัด

f = open("friends.txt", "r")
content = f.read()
print(content)
f.close()


#3. ✍️ รับชื่อลูกค้าจากผู้ใช้ แล้วเขียนลงไฟล์ customers.txt โดยไม่ลบของเก่า (append)

ctm = input("Enter Customer Name: ")

f = open("List_Cm.txt", "a")
f.write(ctm)  # f.write(f"{ctm}\n")
f.write("\n")
f.close()

with open("List_Cm.txt", "r") as f:
    content = f.read()
    print(content)