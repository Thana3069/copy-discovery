for i in range(11):
    # ใช้ list comprehension เพื่อสร้างผลคูณของแม่นั้นๆ (0-10)
    # แล้วแปลงแต่ละผลลัพธ์เป็น string
    results = [str(i * j) for j in range(11)]
    
    # นำผลลัพธ์ใน list มาต่อกันด้วยช่องว่าง
    line = " ".join(results)
    
    # แสดงผลลัพธ์ตามรูปแบบที่ต้องการ
    print(f"Table de {i}: {line}")
