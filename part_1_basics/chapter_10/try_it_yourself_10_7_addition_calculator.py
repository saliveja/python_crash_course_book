# while loop with addition calculator

request = "If you enter two numbers, they will be added for you."
request += "If you want to quit, enter 'q'.\n\n"

number_1 = "First number: "
number_2 = "Second number: "

print(request)

while True:
    answer_1 = input(number_1)
    if answer_1 == 'q':
        break
    answer_2 = input(number_2)
    if answer_2 == 'q':
        break

    try:
        result = int(answer_1) + int(answer_2)
        print(f"{result}")
        # make sure the print is at try or no result will be displayed

    except ValueError:
        print("Addition isn't possible with text.")


