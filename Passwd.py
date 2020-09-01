from random import randrange
from random import choice
import random
import string

# Regeln um ein ausprechbares wort zu erstellen:
# 1. max 2 zahlen hintereinander
# 2. Gleiche buchstaben müssen mind 3 zeichen abstand haben
# 3. Anfangsbuhcstabe muss groß sein
# Vokal dann konsonant im abwechseln

# Vokal Vok Kons Vok kons vok kons vok kons
# Sch sp st hinzufügen

konsonanten = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
vokale = ["A", "E", "I", "O", "U"]
SonderLetter = ["SCH", "SP", "ST"]


def get_new_random_string(length):
    password = ""

    before_letter = None
    kons = False

    has_sonder = False

    how_many_sonder = 0

    for i in range(0, length):

        if has_sonder:
            if how_many_sonder > 0:
                how_many_sonder -= 1
                continue

        if before_letter is None:
            if bool(random.getrandbits(1)):
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

            password += before_letter

        else:
            if random.randint(0, 10) == 10:
                letter = str(randrange(0, 9))

            elif kons:
                letter = get_vokal_letter(before_letter)
                kons = False

            else:
                if random.randint(0, 1) == 1 and not has_sonder and length > 7 and i < length - 3:
                    letter = choice(SonderLetter)
                    if letter == "SCH":
                        how_many_sonder = 2
                    else:
                        how_many_sonder = 1

                    kons = True
                    has_sonder = True

                elif random.randint(0, 10) == 10:
                    letter = str(randrange(0, 9))

                elif random.randint(0, 8) == 8:
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


print(get_new_random_string(12))
