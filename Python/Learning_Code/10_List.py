# List (ลิสต์)

fruits = ["apple", "banana", "mango"]
print(fruits[0],fruits[1],fruits[2])  # แสดงผล fruits

print("------") 

fruits[1] = "orange"  # เปลี่ยน banana → orange
print(fruits[0],fruits[1],fruits[2]) # แสดงผล fruits


# คำสั่งที่ใช้กับ list

print("------") 

# เพิ่มท้าย

fruits.append("grape")

# แทรกตำแหน่งที่ 1

fruits.insert(1, "melon")  

# ลบ apple

fruits.remove("apple")

# ลบตัวสุดท้าย
fruits.pop()   
   
            
# Tuple (ทูเพิล)

colors = ("red", "green", "blue")
print(colors[1])  # green


# Dictionary (พจนานุกรม)
student = {
    "name": "Tor",
    "age": 25,
    "grade": "A"
}

print(student["name"])  # Tor

student["email"] = "tor@example.com"  # เพิ่ม
del student["age"]                    # ลบ


