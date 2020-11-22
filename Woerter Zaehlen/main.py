file = open("test1.txt")
missing_words_string = file.readline()
words_list = sorted(file.readline().split(), key=len)

print(words_list)

dict = {} # Key sind die Anzahl der buchstaben und value eine Liste von den Strings die so viele buchstaben haben
length = 0
for x in words_list:
    if length != len(x):
        length = len(x)
        dict.update({length: []})

    dict[length].append(x)

print(dict)

miss_split = missing_words_string.replace(',', '').replace('!', '').replace('.', '').replace('?', '.').split()

miss_dict = {}
for x in miss_split:
    if length != len(x):
        length = len(x)
        miss_dict.update({length: []})

    miss_dict[length].append(x)
print(miss_dict)

for key, value in miss_dict.items():
    for miss_wort in value:
        letter = miss_wort.replace('_', '')#
        used_index = []
        if letter == '':
            last_word = miss_wort
            continue
        index = miss_wort.find(letter)
        for x in dict[key]:
            if x[index] == letter:
                print('trueee')
                used_index.append(index)
                print(x, miss_wort)
        if last_word
