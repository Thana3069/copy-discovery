print("Enter a number less than 25")


user_input = input()


try:
   
    num = int(user_input)

   
    if num > 25:
        
        print("Error")
    else:
      
        while num <= 25:
            print(f"Inside the loop, my variable is {num}")
            
            num += 1

except ValueError:
    
    print("Error: Invalid input. Please enter an integer.")