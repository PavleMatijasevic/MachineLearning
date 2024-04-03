input_str = "Python program to split and join a string"
word_list = input_str.split()

separator = " "
separator1 = "/"

output_str = separator.join(word_list)
output_str1 = separator1.join(word_list)

print("Original string: ", input_str)
print("List od split Words: ", word_list)
print("Joined String by separator : ", output_str)
print("Joined String by separator / : ", output_str1)


