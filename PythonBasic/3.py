users = []
users.append('Paul')
users.append('John')
users.append('Ted')
users.insert(2, 'Luke')

users.remove('Ted')
#del users[-1]
print(users)

lastUser = users.pop()
print(lastUser)
firstUser = users.pop(0)
print(firstUser)

























