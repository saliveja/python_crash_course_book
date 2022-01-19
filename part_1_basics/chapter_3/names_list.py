

names_list = ['Louise' , 'Emma' , 'Marusha' , 'Lucy']
print(names_list[0].lower() + "\n")
print(names_list[1].upper() + "\n")
print(names_list[2].title() + "\n")
print(names_list[-1])

names_list = ['Louise Michel' , 'Emma' , 'Marusha' , 'Lucy']
message = '"Animals kill to live; the hunter destroys only to destroy"' + '\n' + '\t' + '\t' + '\t' + names_list[0].title() + '\n'
print(message)

names_list = ['Louise Michel' , 'Emma Goldman' , 'Marusha' , 'Lucy']
message = names_list[1].title() + ' said:' + '"If voting changed anything, they would make it illegal"' + '\n'
print(message)

names_list = ['Louise Michel' , 'Emma Goldman' , 'Maria Nikiforova' , 'Lucy']
message = names_list[2].title() + ' , who was also called Marusha, was an anarchist and a revolutionary. She is an inspiration for many until this day. She said: ' + '\n' '"The anarchists are not promising anything to anyone. The anarchists only want people to be conscious of their own situation and seize freedom for themselves"' + '\n'
print(message)

names_list = ['Louise Michel' , 'Emma Goldman' , 'Maria Nikiforova' , 'Lucy Parsons']
message = names_list[3].title() + ' was a leading figure in American anarchism and the radical labor movement. She was a writer, an agitator and organizer. Lucy Parson recognized how the different systems of oppressions were intertwined and could not accepting anything less than revolution. She said: ' + '\n\t' '"The coming change can only come through a revolution, because the possessing class will not allow a peaceful change to take place; still we are willing to work for peace at any price, except at the price of liberty"'
print(message)

