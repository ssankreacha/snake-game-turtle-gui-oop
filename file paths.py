file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

# Open and Read file

with open("my_file.txt") as file:     # Opened and read file
    contents = file.read()            # Saved it to a variable which is then printed
    print(contents)

# Open and Write to file - will change the text from file, to below

with open("new_file.txt", mode='a') as file:       # with will manage that file, once we're done it will close the file
    file.write("\nI love Rocket League. ")         # Writes to file
