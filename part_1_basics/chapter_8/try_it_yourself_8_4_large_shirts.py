def make_shirt(text="'I love Python'", size='large'):
    print(f"My tshirt is size {size} with the text {text}.")


print("\n**")
make_shirt()
print("\n**")
make_shirt(size='medium')
# if everything is defined in the definition,
# we don;t have to write any arguments
print("\n**")
make_shirt(size='small', text="'The state is a repressive organization'")
