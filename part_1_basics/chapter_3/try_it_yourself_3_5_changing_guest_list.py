
guests = ['Kerstin' , 'Elsa' , 'Erika' , 'mother' , 'beloved comrade' , 'Marie' , 'Birgitta' , 'Sandra']
print(guests)

comrade_not_coming_1 = guests.pop(4)
print(guests)
message = "I so much wanted to see you and was hoping you would have time to come for dinner on Sunday, but I heard that are traveling at the moment. Give me a call when you are back."
print(comrade_not_coming_1.title() + ", " + message + "\n")

guests.insert(4, 'Louise')
print(guests)

message = "Jiyan cant' make it to the dinner, but the time and place is the same, 1900 at our place"
print("Dear " + guests[0] + ", " + message + ". " + guests[1] + ", " + guests[2] + ", " + guests[3] + ", " + guests[5] + ", " + guests[6] + ", " + guests[7] + " will be there." + "\n")

print("Dear " + guests[1].title() + ", " + message + "\n")

print("Dear " + guests[2].title() + ", " + message + "\n")

print("My beloved " + guests[3].lower() + ", " + message + "\n")

print("Dear " + guests[4].title() + ", so much looking forward to see you, hope you can make it. We're meeting up at 1900 at our place. see you!" + "\n")

print("Dear " + guests[5].title() + ", " + message + "\n")

print("Dear " + guests[6].title() + ", " + message + "\n")

print("Dear " + guests[7].title() + ", " + message + ". Louise is probably also coming.\n")
