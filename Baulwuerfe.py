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
    combs_leer = []
    for x in range(len(file_list)):
        last_i = None
        last_i_2 = None
        comb = None
        leer_combo = None
        i = 0

        # Zuerst checken obs eine dreier combo gibt
        # Dann checken ob man eine leerer combo hat
        for i in range(len(file_list[x])):
            if file_list[x][i] == 1:
                if last_i is not None:
                    if last_i_2 is not None:
                        comb = i
                    else:
                        last_i_2 = i
                else:
                    if leer_combo is not None:
                        combs_leer.append([x, i - 1])
                        leer_combo = None
                    last_i = i
                    leer_combo = None

                if comb is not None:
                    combs_middle.append([x, last_i_2])
                    last_i = None
                    last_i_2 = None
                    comb = None


            else:
                if last_i is not None:
                    leer_combo = i
                else:
                    leer_combo = None

                last_i = None
                last_i_2 = None
                comb = None

    count = 0
    half_comb = False
    full_leer_comb = []
    for comb in combs_middle:
        for new_comb in combs_leer:
            if new_comb[0] == comb[0] + 1 and new_comb[1] == comb[1]:
                if not half_comb:
                    half_comb = True
                    continue

            elif new_comb[0] == comb[0] + 2 and new_comb[1] == comb[1] and half_comb:
                full_leer_comb.append([comb[0] + 3, comb[1]])
                half_comb = False

        if comb in full_leer_comb:
            count += 1

    print(count)


def main(filename):
    file1 = open(filename, "r")
    file_list = get_file_stuff(file1)
    count_baul(file_list)


if __name__ == '__main__':
    main(filename="karte0.txt")
