with open("./Input/Letters/starting_letter.txt") as default_letter:
    letter = default_letter.read()

with open("./Input/Names/invited_names.txt") as names:
    for name in names.readlines():
        with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", "w") as final:
            final.write(letter.replace("[name]", name.strip()))

