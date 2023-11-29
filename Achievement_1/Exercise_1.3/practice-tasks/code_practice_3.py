# For Loop
numbers = [10, 20, 30, 40, 50]

for number in range(10, 51, 10):
    print(number)
    if number < 50:
        continue
    print("And we are done!")


# While Loop
number = 10

while number < 51:
    print(number)
    if number == 50:
        print("And we are done!")
