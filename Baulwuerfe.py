def get_file_stuff(file):
    breite = int(file.readline())
    hoehe = int(file.readline())

    file_list = []

    for i in range(0, hoehe):
        list = []
        for x in file.readline():
            if x == "X":
                list.append(1)
            else:
                list.append(0)
        file_list.append(list)

    return file_list


def count_baul(file_list):

    combs_middle = []

    for x in range(len(file_list)):
        last_i = None
        last_i_2 = None
        comb = None
        i = 0
        for i in range(len(file_list[x])):
            if file_list[x][i] == 1:
                if last_i is not None:
                    if last_i_2 is not None:
                        comb = i
                    else:
                        last_i_2 = i
                else:
                    last_i = i
                    last_i_2 = None
                    comb = None

                if comb is not None:
                    combs_middle.append([x, last_i_2])
            else:
                last_i = None
                last_i_2 = None
                comb = None

    print(combs_middle)

def main(filename):
    file1 = open(filename, "r")
    file_list = get_file_stuff(file1)
    count_baul(file_list)


if __name__ == '__main__':
    main(filename="karte0.txt")

