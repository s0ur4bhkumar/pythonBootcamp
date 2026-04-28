with open("./Input/Letters/starting_letter.txt") as file:
    content = file.readlines()

with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

for i in names:
    content[0] = f"Dear {i}".replace("\n", ",\n")
    letter = "".join(content)
    print(type(letter))
    with open(f"./Output/ReadyToSend/for_{i.strip('\n')}.docx", mode="x+") as file:
        file.write(letter)
