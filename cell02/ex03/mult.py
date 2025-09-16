num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = num1 * num2


print(f"{num1} x {num2} = {result}")


if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else: # ถ้าไม่มากกว่า 0 และไม่น้อยกว่า 0 แสดงว่าเป็น 0
    print("The result is positive and negative.")