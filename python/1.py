while True:
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        result = numerator / denominator
        print("The result of the division is:" ,result)
        break
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed. Please enter a non-zero denominator.")
