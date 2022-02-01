
guests = ['Kerstin' , 'Erika' , 'mother' , 'beloved comrade' , 'Marie' , 'Birgitta']
print(guests)

guests.append('Sandra')
print(guests)

guests.insert(1, 'Elsa')
print(guests)

print("Dear " + guests[1] + ", I'm putting together a dinner on Sunday and hope you'll have time to come. " + guests[0] + " will also come and I know you wanted to se each other for some time. Hope to see you then <3" + "\n") 

message = "you are welcome for dinner on Sunday at our place at 1900. If it's a nice day we'll be outside. Send a text so we know if you can come or not. Greetings"
print("Dear " + guests[0].title() + ", " + message + "\n")

message = "you are welcome for dinner on Sunday at our place at 1900. If it's a nice day we'll be outside. Send a text so we know if you can come or not. Greetings"
print("My sweet " + guests[3] + ", " + message)

not_coming_1 = guests.pop(4)
print(guests)
message = "I so much wanted to see you and was hoping you would have time to come for dinner on Sunday, but I heard that are traveling at the moment. Give me a call when you are back."
print(not_coming_1 + ", " + message + "\n")

message = "you are welcome for dinner on Sunday at our place at 1900. If it's a nice day we'll be outside. Send a text so we know if you can come or not. Greetings"
print("Dear " + guests[4] + " and " + guests[5] + ", " + message)
