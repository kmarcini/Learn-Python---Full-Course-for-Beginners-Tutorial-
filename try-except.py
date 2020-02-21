
try:
    # num = 10 / 0
    number = int(input("Enter a number: "))
    print(number)

# catch specific errors
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")
