# MATHEMATICAL CALCULATOR

while True:

    print('''
Here is a list of Arithmetic Operations:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Modulus
    6. Exponentiation
    7. Floor Division
    8. Clear
    9. Exit
''')

    user_entry = int(input("Choose an operation (1-9): "))

    if user_entry == 9:
        print("Calculator OFF")
        break

    elif user_entry == 8:
        print("\n" * 50)
        print("Calculator Cleared!")
        continue

    elif user_entry >= 1 and user_entry <= 7:

        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter second number: "))

        if user_entry == 1:
            print("Addition:", num_1 + num_2)

        elif user_entry == 2:
            print("Subtraction:", num_1 - num_2)

        elif user_entry == 3:
            print("Multiplication:", num_1 * num_2)

        elif user_entry == 4:
            if num_2 != 0:
                print("Division:", num_1 / num_2)
            else:
                print("Error! Cannot divide by zero.")

        elif user_entry == 5:
            print("Modulus:", num_1 % num_2)

        elif user_entry == 6:
            print("Exponentiation:", num_1 ** num_2)

        elif user_entry == 7:
            if num_2 != 0:
                print("Floor Division:", num_1 // num_2)
            else:
                print("Error! Cannot divide by zero.")

    else:
        print("Invalid choice!")

