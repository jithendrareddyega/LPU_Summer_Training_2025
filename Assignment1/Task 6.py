while True:
    try:
        number = int(input("Enter a valid integer: "))
        print(f"Valid integer entered: {number}")
        break
    except ValueError:
        print("Invalid input. Please try again.")
