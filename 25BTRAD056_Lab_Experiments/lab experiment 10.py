import string

sentence = input("Enter a sentence: ")

words = sentence.lower().translate(str.maketrans("", "", string.punctuation)).split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequency:")

for word, count in frequency.items():
    print(word, ":", count)
