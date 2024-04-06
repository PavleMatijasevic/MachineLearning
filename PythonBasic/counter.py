sentence = input("Enter a sentence: ")

letter_count = 0
digit_count = 0

for char in sentence:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
    
print("Letter number: ", letter_count)
print("Digit number: ", digit_count)




