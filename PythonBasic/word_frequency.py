input_sentence = input("Enter a sentence: ")

words = input_sentence.split(' ')
word_dict = {}
for word in words:
    word = word.strip('.,!?')
    word = word.lower()
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
    
sorted_words = sorted(word_dict.items())
for word, freq in sorted_words:
    print(f"{word}:{freq}")
    



