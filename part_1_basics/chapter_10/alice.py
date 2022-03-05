# try, except when the file cannot be found
filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        # 'utf-8' is needed to be specified when system's default encoding doesn't
        # match the encoding of the file
        contents = f.read()

except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
