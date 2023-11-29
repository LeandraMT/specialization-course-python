first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))
operator = input("Would you like to add + or subtract - the numbers entered?: ")

if operator == "+":
    print(first_number + second_number)

elif operator == "-":
    print(first_number - second_number)

else:
    print("Please choose either + or -")
