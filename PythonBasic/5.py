age = 19
if age >= 18:
    print('You are old enough to vote!')
else:
    print('You are not old enough to vote!')


if age < 5:
    print('You are too young')
elif age < 15:
    print('You are school age')
elif age < 20:
    print('You are ready for study')
else:
    print('You are to old for this exame')

list_players = ['marcus', 'john', 'victor', 'luke']
if 'john' not in list_players:
    print('You are new player, good luck!')
else:
    print('Player with that name already exists')

new_age = (int)(input('How old are you: '))
print(new_age)


current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1


prompt = "\nTell me something, and I'll"
prompt += " repeat it back to you."
prompt += "\nEnter 'quit' to end the program!\n"

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

























