my_string = input("Enter a string: ")
words = [word.capitalize() for word in my_string.split() ]
words.sort()

print("Sorted words: ")
for word in words:
    print(word)



punctuations = '''!()-[]{};:'"\,<>./?@#$%^*&_~'''
my_string = input("Enter a string: ")

no_punct = ""
for char in my_string:
    if char not in punctuations:
        no_punct = no_punct + char
print(no_punct)

