import re

file = open("test1.txt")
missing_words_string = file.readline()
words_list = sorted(file.readline().split(), key=len)

dict = {} # Key sind die Anzahl der buchstaben und value eine Liste von den Strings die so viele buchstaben haben
length = 0
for x in words_list:
    if length != len(x):
        length = len(x)
        dict.update({length: []})

    dict[length].append(x)

miss_split = missing_words_string.replace(',', '').replace('!', '').replace('.', '').replace('?', '.').split()

miss_dict = {}
for x in miss_split:
    if length != len(x):
        length = len(x)
        miss_dict.update({length: []})

    miss_dict[length].append(x)

final_dict = {}
for key, value in miss_dict.items():
    for miss_wort in value:
        letter = miss_wort.replace('_', '')
        used_index = []
#        last_word = ''
        used_words = []
        if letter == '':
            last_word = miss_wort
            continue
        index = miss_wort.find(letter)
        for x in dict[key]:
            if x[index] == letter:
                used_index.append(index)
                final_dict[miss_wort] = x
                used_words.append(x)

    find_last_word = [x for x in dict[key] if x not in used_words]
    if len(find_last_word) > 0:
        final_dict[last_word] = find_last_word[0]
        #print([x for x in dict[key] if x not in used_words][0], last_word)



def replace_all(text, dic):
    for i, j in dic.items():
        text = re.sub(r'\b'+i+r'\b', j, text)

    return text

print(replace_all(missing_words_string, final_dict))
