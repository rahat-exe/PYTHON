x = 10
y = 0

# print(x / y)

try:
    print(x / y)
except:
    print("Something went wrong...")

print("Still running after exception handling...")


try:
    # Risky code
    number = int(input("Enter a number??"))
    result = 10 / number
except ValueError:
    # Handle error
    print("Please enter a valid number...")
except ZeroDivisionError:
    print("Cannot divide by zero...")
else: # Runs if no exception occurs.
    print("Result:",result)
finally: # Runs regardless of whether an exception occurred.
    print(f"You have entered {number}")