request = "If you enter two numbers, they will be added for you."
request += "If you want to quit, enter 'q'.\n\n"

number_1 = "First number: "
number_2 = "Second number: "

print(request)

answer_1 = input(number_1)
answer_2 = input(number_2)

try:
    result = int(answer_1) + int(answer_2)

except ValueError:
    print("Addition isn't possible with text.")

print(f"The result is {result}")
