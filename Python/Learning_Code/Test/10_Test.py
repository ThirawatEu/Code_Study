#1. 📋 สร้าง list ชื่อ friends ที่เก็บชื่อเพื่อน 3 คน แล้วแสดงชื่อทั้งหมดทีละบรรทัด

fname = ["Timmy", "John", "Jim"]

print(fname[0])
print(fname[1])
print(fname[2])

# tip

for friend in fname:
    print(friend)

for i in range(len(fname)):
    print(f"{i+1}. {fname[i]}")

print("------") 

    
#2. 🛒 ใช้ dictionary เก็บข้อมูลสินค้าชิ้นหนึ่ง เช่น name, price, stock แล้วแสดงชื่อสินค้ากับราคามันออกมา

product = {
    "name": "iphong",
    "price": 5000,
    "stock": 10
}

print(product["name"], product["price"], product["stock"])

# tip

print(f"Product: {product['name']}")
print(f"Price: {product['price']} baht")
print(f"In stock: {product['stock']} units")

#3. 📊 ให้สร้าง list ชื่อ scores เก็บคะแนนสอบ 5 วิชา แล้วหาค่าเฉลี่ยทั้งหมด

scores = [80, 75, 90, 60, 85]  # คะแนน 5 วิชา

total = sum(scores)            # รวมคะแนนทั้งหมด
average = total / len(scores) # หาค่าเฉลี่ย

print(f"Total Score: {total}")
print(f"Average Score: {average}")

# sum(scores) → เอาคะแนนใน list มารวมกัน
# len(scores) → นับจำนวนวิชา (กี่ตัว)

scores = []

for i in range(5):
    score = int(input(f"Enter score for subject {i+1}: "))
    scores.append(score)

average = sum(scores) / len(scores)
print(f"Average Score: {average}")

