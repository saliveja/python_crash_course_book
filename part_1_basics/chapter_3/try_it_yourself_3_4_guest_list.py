
guests = ['Kerstin' , 'Erika' , 'mother' , 'beloved comrade' , 'Marie' , \
'Birgitta']
print(guests)
# guest list before changes

guests.append('Sandra')
print(guests)
# adding guest at the end of the list

guests.insert(1, 'Elsa')
print(guests)
# inserting guest at position 1 in the list

print("Dear " + guests[1] + ", I'm putting together a dinner on Sunday and \
hope you'll have time to come. " + guests[0] + " will also come and I know \
you wanted to se each other for some time. Hope to see you then <3" + "\n") 

message = "you are welcome for dinner on Sunday at our place at 1900. If it's \
a nice day we'll be outside. Send a text so we know if you can come or not. \
Greetings"
print("Dear " + guests[0].title() + ", " + message + "\n")

message = "you are welcome for dinner on Sunday at our place at 1900. If it's \
a nice day we'll be outside. Send a text so we know if you can come or not. \
Greetings"
print("My sweet " + guests[3] + ", " + message + "\n")

message = "you are welcome for dinner on Sunday at our place at 1900. If it's \
a nice day we'll be outside. Send a text so we know if you can come or not. \
Greetings"
print("Dear " + guests[4] + " and " + guests[5] + ", " + message)
# writing in plural even if it's a list can create unnecessary syntax errors
# for example writing guest instead of guests

guests = ['Kerstin' , 'Elsa' , 'Erika' , 'mother' , 'beloved comrade' , \
'Marie' , 'Birgitta' , 'Sandra']
print(guests)
comrade_not_coming_1 = guests.pop(4)
print(guests)
print("Our " + comrade_not_coming_1 + ", Jiyan, will unfortunately not be \
able to come due to travels.")
# 'beloved comrade' removed from the list and other guests are informed
