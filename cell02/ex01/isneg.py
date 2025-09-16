while True:
    user_input = input("Enter a number (or 'q' to quit): ")

    # ถ้าอยากให้หยุดโปรแกรม ให้พิมพ์ q
    if user_input.lower() == "q":
        print("Goodbye!")
        break

    number = float(user_input)

    if number < 0:
        print("This number is negative.")
    elif number > 0:
        print("This number is positive.")
    else:
        print("This number is both positive and negative.")