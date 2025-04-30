def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")

    print("4. Division (/)")

    while True:
        # Get the user's choice
        choice = input("Enter the number corresponding to the operation (1/2/3/4) or 'q' to quit: ")

        if choice.lower() == 'q':  # Quit the program
            print("Exiting the calculator. Goodbye!")
            break

        # Check if the input is valid
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select a valid operation.")
            continue

        try:
            # Input two numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform the chosen operation
            if choice == '1':
                print(f"The result of {num1} + {num2} is: {num1 + num2}")
            elif choice == '2':
                print(f"The result of {num1} - {num2} is: {num1 - num2}")
            elif choice == '3':
                print(f"The result of {num1} * {num2} is: {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print(f"The result of {num1} / {num2} is: {num1 / num2}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")

# Call the calculator function
calculator()