# written in pep8 standards:
# ~ Add 4 spaces (an extra level of indentation) to distinguish arguments \
# ~ from the rest.
# ~ I'm using \ to break the line and two times tab as indent.
# ~ is this a correct understanding of pep8 standards that is referred to?


guests = ['Kerstin' , 'Elsa' , 'Erika' , 'mother' , 'beloved comrade' , \
    'Marie' , 'Birgitta' , 'Sandra']
        
print(guests)
# complete guest list before changes

comrade_not_coming_1 = guests.pop(4)
print(guests)
message = "I so much wanted to see you and was hoping you would have time to \
    come for dinner on Sunday, but I heard that are traveling at the \
    moment. Give me a call when you are back."
print(comrade_not_coming_1.title() + ", " + message + "\n")
# Pop() removing 'beloved comrade' from the list and printing message to them.


guests.insert(4, 'Louise')
print(guests)
# adding a new guest, Louise at position four in the list

message = "Jiyan cant' make it to the dinner, but the time and place is the \
    same, 1900 at our place"
print("Dear " + guests[0] + ", " + message + ". " + guests[1] + ", " + \
    guests[2] + ", " + guests[3] + ", " + guests[5] + ", " + guests[6] +\
    ", " + guests[7] + " will be there." + "\n")

print("Dear " + guests[1].title() + ", " + message + "\n")



numbers = [
    1, 2, 3,
    4, 5, 6, 
    7, 8, 9, 
    ]
# ~ organizing number with pep standards should look like this

999

