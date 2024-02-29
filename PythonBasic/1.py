print("Hello world")
msg = "Hello World!"
print(msg)

list1 = ['apple', 'banana', 'orange']
first_element = list1[0]
last_element = list1[-1]

for list_item in list1:
    print(list_item)

list2 = []
list2.append('red')
list2.append('blue')
list2.append('black')

list3 = []
for x in range(1,11):
    list3.append(x**2)

list1_copy = list1[:]
print(list1_copy)

#tuple
cordinates = (10, 3)

#dictionary
alien = {'color': 'green', 'points': 5}

favourite_numbers = {'eric': 17, 'ever': 4}
for name, number in favourite_numbers.items():
    print(name + " loves " + str(number))

def greet_user(username):
    print("Hello " + username + " !")

greet_user("Pavle")

def sumNumbers(x, y):
    return x + y

print(sumNumbers(2,5))

class Dog():

    def __init__(self, name):
        self.name = name

    def sit(self):
        print(self.name + " is sitting")

my_dog = Dog("Mrvica")
print(my_dog.name + " is a great dog!")
my_dog.sit()



filename = 'inputFile.txt'

with open(filename) as f:
    lines = f.readlines()
for line in lines:
    print(line)


filename = 'outputFile.txt'
with open(filename, 'w') as f:
    f.write("This is output file")























