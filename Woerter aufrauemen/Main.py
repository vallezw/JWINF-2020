def get_file_stuff(file):
    line1= file.readline()
    words = file.readline()
    get_text(line1, words)

def get_text(line1, words):
    gap_words = line1.split(' ')


    for x in range(0, len(gap_words)):
        for i in words:
            possib = []
            if len(i) == len(gap_words[x]):
                for j in range(0, len(x)):
                    if gap_words[x][j] is not '_':
                        possib.append([gap_words[x][j], j])

                for k in range(0, len(i)):
                    if [i[k], k] in possib:


if __name__ == '__main__':
    file1 = open("raetsel0.txt", "r")
    get_file_stuff(file1)
