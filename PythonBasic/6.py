def greet_user():
    print('Hello!')

greet_user()

def greet_user(usrnm):
    print('Hello '+usrnm+" !")

greet_user('Pavle')

def describe_yourself(usrnm, age):
    print("\nMy name is " , usrnm , " and I have ", age, " years.")

describe_yourself('John', 30)

def describe_pet(name, animal):
    print("I have a " + animal + ".")
    print("It's name is "+ name + ".")

describe_pet('Sophie', 'dog')

def describe_pet(name, animal='cat'):
    print("I have a " + animal + ".")
    print("It's name is "+ name + ".")

describe_pet('Leny')


def describe_pet(animal,name=None):
    print("I have a " + animal + ".")
    if name:
        print("It's name is "+ name + ".")
describe_pet('fish', 'Kelly')
describe_pet('snake')


def get_full_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name

print(get_full_name('Pavle', 'Matijasevic'))


def greet_users(names):
    for name in names:
        msg = "Hello " + name
        print(msg)
usrnms = ['Pavle', 'Mina', 'Vladan', 'Tanja']
greet_users(usrnms)























