from random import randrange
from random import choice
import string


# Regeln um ein ausprechbares wort zu erstellen:
# 1. max 2 zahlen hintereinander
# 2. Gleiche buchstaben müssen mind 3 zeichen abstand haben
# 3. Anfangsbuhcstabe muss groß sein
# 4. Anzahl an buchstaben <= 6 : 2 Vokale im Wort, Anzahl an buchstaben > 6: 4
# Vokal dann konsonant im abwechseln

def get_random_string(length):
    letters = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
    vokale = ["A", "E", "I", "O", "U"]

    password = ""
    number_pos, vokal_pos = get_positions(length)
    print(number_pos)
    before_letter = None
    for i in range(0, length):
        letter = choice(letters)

        if i in number_pos:
            password += str(randrange(0, 10))
        elif i in vokal_pos:
            letter = choice(vokale)
            if before_letter == None:
                before_letter = letter
                password += before_letter
            while letter == before_letter:
                letter = choice(vokale)
            else:
                before_letter = choice(vokale).lower()
                password += before_letter

        elif before_letter is None:
            before_letter = choice(letters)
            password += before_letter

        else:
            if letter.lower() == before_letter:
                while letter is not None and letter == before_letter:
                    letter = choice(letters)

            before_letter = letter.lower()
            password += letter.lower()

    return password


def get_random_number():
    return randrange(10)


def get_positions(length):
    amount_of_numbers = 0
    if length < 6:
        amount_of_numbers = round(length / 2)

    if length >= 6:
        amount_of_numbers = round(length / 2 / 2)

    number_pos = []
    vokal_pos = []
    old_number = None
    old_vokal = None

    for i in range(0, amount_of_numbers):
        number = randrange(1, length)
        vokal = randrange(1, length)
        while number == vokal:
            number = randrange(1, length)

        while vokal is not None and old_vokal == number:
            vokal = randrange(1, length)

        while old_number is not None and old_number == number:
            number = randrange(1, length)

        number_pos.append(number)
        vokal_pos.append(vokal)

        old_number = number
        old_vokal = vokal

    return number_pos, vokal_pos


print(get_random_string(22))
