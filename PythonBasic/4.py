print('First print: ')
for number in range(11):
    print(number)

print('Second print')
for number in range(1,11):
    print(number)

list_numbers = list(range(1,11))
print('List numbers: ', list_numbers)



ages = [11, 4, 2, 5, 6, 7, 9, 12, 8]
min_ages = min(ages)
max_ages = max(ages)
sum_ages = sum(ages)
print('Minimum element of list ages is : ' , min_ages)
print('Maximum element of list ages is : ' , max_ages)
print('Sum element of list ages is : ' , sum_ages)


list1 = ['pavle', 'mina', 'vladan', 'tanja', 'pera', 'zika', 'laza']
print(list1[:3]) # first three
print(list1[1:3]) # from index 1 to the index 3
print(list1[-3:]) # last 3 element from list1
print(list1[:]) # print all elements

upper_name = [] # list1 but modify, all names is upper
for name in list1:
    upper_name.append(name.upper())
print(upper_name)


dic_1 = {}

dic_2 = {'Pavle': 'Python', 'Mina': 'Java', 'Vladan': 'C', 'Tanja': 'SQL'}
for first, second in dic_2.items():
    print(first + " favourite language is: " + second)

list_keys = ['Pavle', 'Mina', 'Vladan', 'Tanja']
list_values = [24, 21, 53, 49]














