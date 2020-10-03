import random
from random import choice
from random import randrange

konsonanten = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
vokale = ["A", "E", "I", "O", "U"]
SonderLetter = ["SCH", "SP", "ST"]

def create_password(length):
    password = ""
    i = 0
    letter_num = False
    vokal = None
    while i < length:
        letter = None
        #exp = False # Wenn i geändert wurde

        if password == "":  # First char of passwd
            letter = _first_letter_algorithm(length, i)

        else:  # Folgezeichen
            if _random_num() <= 10:  # Zahl
                letter = str(randrange(0, 9))
                letter_num = True

            else:
                if letter_num == True: # Voriges Zahl
                    letter_num = False
                    letter = _first_letter_algorithm(length, i)
                else:
                    if vokal: # Voriges Vokal
                        print("IN VOKAL")
                        if _random_num() <= 5: # 'e' oder 'h' hinzufügen
                            if _random_num() <= 15: # Konsonanten folge
                                if length - i >= 3:
                                    letter = choice(SonderLetter).lower()
                                else:
                                    letter = choice(konsonanten).lower()
                            else:
                                letter = choice(konsonanten).lower()

                        else:
                            letter = choice(konsonanten).lower()

                    else: # Voriges Kons
                        print("IN KONS")
                        if _random_num() <= 15:
                            print("kleiner gliehc 15")
                            if length - i >= 2:
                                print("is oaky")
                                letter = choice(vokale).lower() * 2
                            else:
                                print("is not oaky")
                                letter = choice(vokale).lower()
                        else:
                            print("§is  elkse")
                            letter = choice(vokale).lower()


        if letter == None:
            print("TWF")
        password += letter
        print(vokal)
        if letter.upper() in vokale:
            vokal = True
        else:
            vokal = False

        i += len(letter)

    return password



def _first_letter_algorithm(length, i):
    random_num = _random_num()
    letter = ""
    if random_num < 50:  # Vokal
        if _random_capital():  # Großbuchstabe
            letter = _kind_of_char_algorithm(length, i, True)
        else:
            letter = _kind_of_char_algorithm(length, i, False)

    elif random_num >= 95:  # Konsonantenfolge
        if length - i > 3:
            if _random_capital():
                letter = choice(SonderLetter).lower()
                letter = letter[0].upper() + letter[:1]
            else:
                letter = choice(SonderLetter).lower()

        else:  # Konsonant
            if _random_capital():
                letter = _kind_of_char_algorithm(length, i, True)

            else:
                letter = _kind_of_char_algorithm(length, i, True)

    else:
        letter = choice(konsonanten).lower()

    return letter

def _kind_of_char_algorithm(length, i, capital):
    if _random_num() > 15:  # Nichts ergänzen
        letter = choice(vokale)

    elif _random_num() >= 10:  # Doppelvokal
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


print(create_password(10))

