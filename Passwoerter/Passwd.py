import random
from random import randrange
from random import choice

# import string

# Regeln, um ein ausprechbares Wort zu erstellen:
# 1. Geringe Wahrscheinlichkeit, dass 2 Zahlen hintereinander kommen, noch geringer mehr als 2
# 2. Keine zwei gleichen Buchstaben hintereinander
# 3. Anfang immer mit Buchstabe, mit 75% Wahrscheinlichkeit groß, sonst klein
# 4. Nach Vokal immer Konsonant oder Sonderzeichen/Zahl, nach Konsonant mit hoher Wahrscheinlichkeit Vokal
# 5. mit geringer Wahrscheinlichkeit nach Vokal ein e, liefert ae oe ue ee ie, alles existierende Kombis

# Vokal Vok Kons Vok kons vok kons vok kons


konsonanten = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
vokale = ["A", "E", "I", "O", "U"]
SonderLetter = ["SCH", "SP", "ST"]


def get_new_random_string(length):
    password = ""

    before_letter = None
    kons = False
    has_sonder = False

    how_many_sonder = 0

    #  TODO: Mindetslänge checken
    #  TODO: Am Ende prüfen, ob eine Zahl drin. Wenn nicht, letztes Zeichen Zahl (als Option, wenn Passwortregel das fordert)
    #  TODO: Nach Zahl mit 50% Wahrscheinlichkeit Groß oder Klein, 75% am PasswortAnfang

    for i in range(0, length):
        if has_sonder:
            if how_many_sonder > 0:
                how_many_sonder -= 1
                continue

        if before_letter is None: # Fangen wir mit dem ersten Zeichen an ... entweder Vokal oder Konsonant, entweder groß oder klein
            if bool(random.getrandbits(1)):  # True oder False
                if bool(random.getrandbits(1)):
                    before_letter = choice(vokale)
                else:
                    before_letter = choice(vokale).lower()
                kons = False
            else:
                if bool(random.getrandbits(1)):
                    before_letter = choice(konsonanten)
                else:
                    before_letter = choice(konsonanten).lower()
                kons = True

            password += before_letter # hiermit festlegen, dass erste Zeichen fertig ist

        else: # jetzt sind wir beim zweiten oder allen Folgezeichen
            if random.randint(1, 10) == 10: # Mit Wahrscheinlichkeit 1/10 wird eine Zahl genommen
                letter = str(randrange(0, 9))
                kons = bool(random.getrandbits(1))

            elif kons: # Wenn vorheriger Buchstabe Konsonant war, wird der nächste ein Vokal
                letter = get_vokal_letter(before_letter)
                kons = False

            else:
                if bool(random.getrandbits(1)) and not has_sonder and length > 7 and i < length - 3:
                    letter = choice(SonderLetter)
                    if letter == "SCH":
                        how_many_sonder = 2
                    else:
                        how_many_sonder = 1

                    kons = True
                    has_sonder = True

            #   elif random.randint(0, 10) == 10:
            #       letter = str(randrange(0, 9))

                elif random.randint(1, 8) == 8:
                    letter = get_vokal_letter(before_letter)
                    kons = False
                else:
                    letter = get_kons_letter(before_letter)
                    kons = True

            before_letter = letter.lower()
            password += letter.lower()

    return password


def get_kons_letter(before_letter):
    letter = choice(konsonanten)
    while letter.lower() == before_letter.lower():
        letter = choice(vokale)
    return letter


def get_vokal_letter(before_letter):
    letter = choice(vokale)
    while letter.lower() == before_letter.lower():
        letter = choice(vokale)
    return letter


print(get_new_random_string(10))
