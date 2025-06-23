num_str = input("Enter a number: ")
try:
    number = int(num_str)
    print(f"Integer value: {number}")
except ValueError:
    print("Error: Please enter a valid number.")
