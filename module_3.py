# Program: poem mixer
# This program takes string input and then prints out a mixed order version of the string



string_input = input("Enter a saying or a poem: ")
words_list = string_input.split()
list_length = len(words_list)

for word in range(list_length):
    if len(words_list[word]) <= 3:
        words_list[word] = words_list[word].lower()
    elif len(words_list[word]) >= 7:
        words_list[word] = words_list[word].upper()

def word_mixer(words):
    words_list.sort()
    new_list = []
    while len(words_list) > 5:
        new_list.append(words_list.pop(-5))
        new_list.append(words_list.pop(0))
        new_list.append(words_list.pop(-1))
    return (" ".join(new_list))

print(word_mixer(words_list))
