password = "000111"

# ขอให้ผู้ใช้กรอกรหัสผ่าน
user_input = input("Enter the password: ")

# ตรวจสอบรหัสผ่าน
if user_input == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")