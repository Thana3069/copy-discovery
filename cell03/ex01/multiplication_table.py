print("Enter a number")


user_input = input()


try:
  
    number = int(user_input)

 
    for i in range(10):
       
        result = i * number
       
        print(f"{i} x {number} = {result}")

except ValueError:
   
    print("Error: Invalid input. Please enter an integer.")