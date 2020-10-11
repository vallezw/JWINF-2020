import random
from random import choice
from random import randrange

konsonanten = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
Doppelkonsonanten = ['nn', 'mm', 'll', 'ss', 'tt', 'ff']
vokale = ["A", "E", "I", "O", "U"]

SonderFolgen = ["SCH", "SP", "ST", "CH", "PH"]

# Regeln: Abwechselnd Vokal & Konsonant
#         Außer: Doppelekonsonannten

def create_password(length):
    password = ""
    i = 0
    letter_num = False
    letter_konsfolge = False
    vokal = None
    letter = None

    while i < length:
        vok_exp = False
        if password == "":  # First char of password
            letter = _first_letter_algorithm(length, i)

        else:  # Folgezeichen
            rand_num = _random_num()
            if rand_num <= 20 and letter_num == False:  # Zahl
                letter = str(randrange(0, 9))
                letter_num = True

            else:
                if letter_num == True: # Voriges Zahl
                    letter_num = False
                    letter = _first_letter_algorithm(length, i)
                else:
                    if vokal: # Voriges Vokal
                        rand_num = _random_num()
                        if rand_num <= 20: # 'e' oder 'h' hinzufügen
                            if bool(random.getrandbits(1)):
                                letter = "e"
                            else:
                                letter = "h"
                                vok_exp = True

                        elif rand_num <= 50:  # Konsonantenfolge
                            if length - i >= 3 and letter_konsfolge == False:
                                letter = choice(SonderLetter).lower()
                                letter_konsfolge = True
                            else:
                                letter = _get_letter_kons(password)
                                letter_konsfolge = False

                        else:
                            letter = _get_letter_kons(password)
                            letter_konsfolge = False

                    else: # Voriges Kons
                        rand_num = _random_num()
                        if rand_num <= 15:
                            if length - i >= 2:
                                if letter.upper() in ['N', 'M', 'L', 'S', 'T', 'F'] and len(password) > 1:
                                    letter = letter.lower()
                            else:
                                letter = _get_letter_vok(password)
                        else:
                            letter = _get_letter_vok(password)


        password += letter

        test = letter[-1].upper()
        if test in vokale:
            vokal = True

        else:
            vokal = False

        if vok_exp:
            vokal = True
        i += len(letter)

    return password



def _get_letter_vok(password):
    letter = choice(vokale).lower()
    while password[-1] == letter:
        letter = choice(vokale).lower()
    return letter



def _get_letter_kons(password):
    letter = choice(konsonanten).lower()
    while password[-1] == letter:
        letter = choice(konsonanten).lower()
    return letter


def _first_letter_algorithm(length, i):
    random_num = _random_num()
    letter = ""
    if random_num <= 50:  # Vokal
        if _random_capital():  # Großbuchstabe
            letter = _kind_of_char_algorithm(length, i, True)
        else:
            letter = _kind_of_char_algorithm(length, i, False)

    elif random_num >= 90:  # Konsonantenfolge
        if length - i > 3:
            if _random_capital():
                letter = choice(SonderLetter).lower().capitalize()
            else:
                letter = choice(SonderLetter).lower()


        else:  # Konsonant
            letter = _get_kons_upper_or_lower()

    else:
        letter = _get_kons_upper_or_lower()

    return letter


def _get_kons_upper_or_lower():
    if _random_capital():
        letter = choice(konsonanten)

    else:
        letter = choice(konsonanten).lower()
    return letter

def _kind_of_char_algorithm(length, i, capital):
    if _random_num() > 15:  # Nichts ergänzen
        letter = choice(vokale)

    elif _random_num() >= 10:  # Umlaut  --- HIER IST WAS FISHY
        if length - i > 2:
            letter = 'e'
            while letter.lower() == 'e':
                if capital:
                    letter = choice(vokale)
                else:
                    letter = choice(vokale).lower()

            letter += choice(vokale).lower()
            exp = True

        else:
            letter = choice(vokale)

    else:  # 'h' hinzufügen
        if length - i != 0:
            if capital:
                letter = choice(vokale)
            else:
                letter = choice(vokale).lower()
            letter += "h"
            exp = True
        else:
            letter = choice(vokale)

    return letter

def _random_capital():
    return _random_num() > 25

# Random number between 1 and 100
def _random_num():
    return randrange(1, 100)


pw = create_password(10)
print(pw, len(pw))

