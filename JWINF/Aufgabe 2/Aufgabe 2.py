# Routine zum Einlesen des Feldes
# Der Routine wird der File-Pointer übergeben
# Als Ergebnis liefert sie ein zweidimensionales Array aus Zeilen und Spalten gefüllt mit Nullen und Einsen
def get_file_stuff(file):
    file.readline()                 # Breiteninformation brauchen wir nicht
    hoehe = int(file.readline())

    datei_zeilen = []

    for i in range(0, hoehe):
        zeile = []
        for x in file.readline():
            if x == "X":
                zeile.append(True)
            else:
                zeile.append(False)
        datei_zeilen.append(zeile)

    return datei_zeilen

# Hauptroutine:
# - Übergeben wird das als Array gespeicherte Feld,
# - Ausgegeben die gezählte Zahl der Rechtecke
def count_baul(file_list):
# Erster Teil der Hauptroutine, in der ich die Dreierkombinationen im Array auffinde und die Positionen in die Liste speichere
    combs_middle = []
    combs_leer = []
    for x in range(len(file_list)):             # x durchläuft die Zeilen im Feld
        last_i = None                           # Flag
        last_i_2 = None
        comb = None                             # Variable, die mir 3er Kombo XXX anzeigt
        leer_combo = False                       # Flag, dass mir
        end = False                             # Diese Flag benutzt ich für ...
        # Zuerst checken, ob es in der Zeile eine dreier combo gibt
        # Dann checken ob man eine leerer combo hat
        for i in range(len(file_list[x])):      # i durchläuft die Spalten in der x'ten Zeile
            if file_list[x][i]:                 # True bedeutet Maulwurfhügel (als X in der ursprünglichen Textdatei)
                end = False                     # Flag, das ...
                if last_i is not None:          # In der letzen Spalte war ein Hügel
                    if last_i_2 is not None:    # In der vorletzen Spalte war ein Hügel --> Volle 3er Kombo gefunden!
                        if comb is not None:    # Wir haben vier oder mehr Hügel hintereinander, daher müssen wir den Start einer
                                                # neuen Kombo anzeigen mit der Flag end
                            print("Hallo", x, i, last_i, last_i_2, comb)
                            end = True
                            combs_middle.append([x, comb])
                            last_i = last_i_2
                            last_i_2 = comb
                        comb = i                # In jedem Fall halten wir in comb die Position fest, da XXX gefunden wurde
                    else:
                        last_i_2 = i
                else:                           # In der letzten Position war kein Baulwurfhügel
                                                # Wir schauen in den Zwischenspeicher leer_combo, ob der aktuelle Hügel eine Leerkombination vervoillständigt
                    if leer_combo:
                        combs_leer.append([x, i - 1])
                    last_i = i                  # Wir vemerken den letzten Hügel und weiter geht es
                    leer_combo = False

                if comb is not None and not end:
                    combs_middle.append([x, last_i_2])


            else:                                       # Wenn kein Baulwurfhügel auf der Postion ist, gibt es zwei Möglichkeiten
                if last_i is not None:
                    leer_combo = True                      # Es könnte noch eine X X Kombination sein, das merken wir uns für später
                else:
                    leer_combo = False                   # Es ist keine X X Kombination, da zwei Positionen hintereinader ohne Hügel sind

                last_i = None                           # In jedem Fall resetten wir jetzt wieder alle Flags/Variablen --> Suche beginnt neu
                last_i_2 = None
                comb = None

    print(combs_middle)
    print(combs_leer)


# Zweiter Teil der Hauptroutine, in der ich aus den Listen die Rechtecke identifiziere und zähle
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
