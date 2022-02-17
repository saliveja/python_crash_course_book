# while loop

current_number = 1
# assigning current number the value 1
while current_number <= 5:
    # as long as the current number is less than or equal to 5
    print(current_number)
    # printing the current number, which the first time is 1
    current_number += 1
    # adding 1 to the value of the current number, which then become two etc
    # the loop stops running when it reaches 5
print("\n\n")

# using continue in loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

print("\n\n")

x = 1
# variable equals x
while x <= 5:
    # while x is less than or equal to 5
    print(x)
    # x will be printed
    x += 1
    # every loop value 1 will be added
    # this ensures that the loop won't run forever
    # if we don't add the last line, the value will forever be 1
    # because the conditional text will always be True
