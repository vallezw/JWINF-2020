def get_file_stuff(file):
    file.readline()
    hoehe = int(file.readline())

    datei_zeilen = []

    for i in range(0, hoehe):
        zeile = []
        for x in file.readline():
            if x == "X":
                zeile.append(1)
            else:
                zeile.append(0)
        datei_zeilen.append(zeile)

    return datei_zeilen


def count_baul(file_list):
    combs_middle = []
    combs_leer = []
    for x in range(len(file_list)):
        last_i = None
        last_i_2 = None
        comb = None
        leer_combo = None
        i = 0
        end = False
        # Zuerst checken obs eine dreier combo gibt
        # Dann checken ob man eine leerer combo hat
        for i in range(len(file_list[x])):
            if file_list[x][i] == 1:
                end = False
                if last_i is not None:
                    if last_i_2 is not None:
                        if comb is not None:
                            end = True
                            combs_middle.append([x, comb])
                            last_i = last_i_2
                            last_i_2 = comb
                            comb = i
                        else:
                            comb = i
                    else:
                        last_i_2 = i
                else:
                    if leer_combo is not None:
                        combs_leer.append([x, i - 1])
                    last_i = i
                    leer_combo = None

                if comb is not None and not end:
                    combs_middle.append([x, last_i_2])


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

    return count


def main(filename):
    file1 = open(filename, "r")
    file_list = get_file_stuff(file1)
    return count_baul(file_list)

if __name__ == '__main__':
    print(main(filename="karte0.txt"))
