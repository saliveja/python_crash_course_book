# creating a function with while statement
# attempting not save input info to a text file - NOT working
def make_album():
    info = "Press q if you want to exit."
    question_1 = 'Artist: '
    question_2 = 'Album: '
    question_3 = 'Tracks: '

    while True:
        print(info)
        answer = input(question_1)
        if answer == 'q':
            quit()

        else:
            store = open("test.txt", "w")
            store.writelines(answer)
            # store_1 = close('~/Desktop/test2.odt')
            print("\n")

            print(info)
            answer_2 = input(question_2)
            if answer_2 == 'q':
                quit()

            else:
                store.writelines(answer_2)
                print("\n")

                print(info)
                answer_3 = input(question_3)
            if answer_3 == 'q':
                quit()

            else:
                store.writelines(answer_3)
                print("Thank you for your participation.\n")


## NOT FINISHED
make_album()
print("Have a nice day!")
