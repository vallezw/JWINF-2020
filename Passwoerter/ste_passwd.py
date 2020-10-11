import random
from random import choice
from random import randrange

# Konsonanten
konsonanten = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "R", "S", "T", "V", "W", "X", "Y", "Z"]
doppelkonsonanten = ['nn', 'mm', 'll', 'ss', 'tt', 'ff']
sonderfolgen = ["SCH", "SP", "ST", "CH", "PH"]
sonderfolgen_2 = ["SP", "ST", "CH", "PH", "QU"]
# Vokale
vokale = ["A", "E", "I", "O", "U"]
umlaute = ["AE", "UE", "OE", "AU", "EU", "EI", "AI"]
doppelvokale = ["AA", "AH", "EE", "EH", "UH", "OH", "OO", "IE"]

# Regeln:
# 0) Allgemein gilt bei Zeichen: Zufall
# 1) In der Regel abwechselnd Vokal & Konsonant
#    - Außer: Doppelekonsonannten, Umlaute gedehnte Vokale (Doppelvokale), Sonderfolgen von Konsonanten
# 2) Am Anfang oder nach einer Zahl 75% Wahrsch. groß
# 3) Mit Wahrsch 15% kommt eine Zahl, Zahl nach Zahl möglich, aber unwahrscheinlich
# 4) Nach einer Zahl wie am Wortanfang starten (Groß / Klein etc)
# 5) Passwort enthält immer eine Zahl, wenn nicht per Zufall beim generieren der ersten Zeichen, dann am Ende
# 6) Passwort enthält immer einen Großbuchstaben, wenn nicht per Zufallsalgo, wird der erste groß gesetzt


class PasswordGenerator:
    def __init__(self):
        self.password = ""
        self.i = 0
        self.letter_num = False
        self.jemals_num = False
        self.jemals_gross = False
        self.vokal = None

    def create_password(self, length):
        if length < 3:
            print("Length too short")
            return "error"

        # First char of password
        letter = self._first_letter_algorithm(length)
        self.password += letter

        while self.i < length - 1:
            if self.letter_num:
                self.letter_num = False
                letter = self._first_letter_algorithm(length)
            else:
                self.letter_num = False
                random_num = self._random_num()  # Zufallszahl zwischen 1 und 100
                # letter = ""
                if random_num <= 15:             # Mit 15% Wahrsch eine Zahl
                    letter = str(randrange(0, 9))
                    self.letter_num = True
                    self.jemals_num = True
                    self.i += 1
                elif self.vokal:                # Vorher Vokal, also nun Konsonant
                    self.vokal = False
                    if random_num <= 70: # Einfacher Konsonant mit 70-15%= 55% Wahrsch
                        letter = choice(konsonanten).lower()
                        self.i += 1
                    elif random_num <= 90: # Doppelkonsonant
                        letter = choice(doppelkonsonanten).lower()
                        self.i += 2
                    else:
                        if length-self.i > 3:
                            letter = choice(sonderfolgen).lower()
                        else:
                            letter = choice(sonderfolgen_2).lower()
                        self.i += len(letter)

                else:                     # Vorher Konsonant, also nun Vokal
                    self.vokal = True
                    if random_num <= 70:  # Einfacher Vokal mit 70-15%= 55% Wahrsch
                        letter = choice(vokale).lower()
                        self.i += 1
                    elif random_num <= 90:  # Doppelvokal
                        letter = choice(doppelvokale).lower()
                        self.i += 2
                    else:
                        letter = choice(umlaute).lower()
                        self.i += 2
            self.password += letter

        if len(self.password) < length:
            if  self.jemals_num == False:
                letter = str(randrange(0, 9))
                self.letter_num = True
                self.jemals_num = True

            else:
                if self.vokal == True:
                    letter = choice(konsonanten).lower()
                else:
                    letter = choice(vokale).lower()
            self.i += 1
            self.password += letter

        if self.jemals_gross == False:
            self.password = self.password.capitalize()
            print("Ersten Buchstaben groß gemacht")

        if self.jemals_num == False:
            self.password = self.password[:-1] + str(randrange(0, 9))
            print("Letzte Buchstaben zur Zahl gemacht")

        return self.password

    def _first_letter_algorithm(self, length):
        # Liefert einen zufälliges erstes Zeichen bzw. eine Zeichenfolge
        random_num = self._random_num()         # Zufallszahl zwischen 1 und 100
        letter = ""
        self.letter_num = False
        self.vokal = False

        if random_num <= 30:                        # Einfacher Vokal mit 30% Wahrsch
            if self._random_capital():              # Großbuchstabe
                letter = choice(vokale)
                self.jemals_gross = True
            else:                                   # Kleinbuschstabe
                letter = choice(vokale).lower()
            self.vokal = True
            self.i += 1

        elif random_num <= 40:                      # Umlaut mit 10% (am Anfang eher kein Doppelvokal)
            if self._random_capital():              # Großbuchstabe am Anfang
                letter = choice(umlaute).lower().capitalize()
                self.jemals_gross = True
            else:                                   # Kleinbuchstabe am Anfang
                letter = choice(umlaute).lower()
            self.vokal = True
            self.i += 2

        elif random_num <= 75:                      # Einfacher Konsonant mit 35%
            if self._random_capital():              # Großbuchstabe
                letter = choice(konsonanten)
                self.jemals_gross = True
            else:                                   # Kleinbuschstabe
                letter = choice(konsonanten).lower()
            self.i += 1

        elif random_num <= 85:                      # Sonderfolge mit 10%
            if length-self.i < 3:
                if self._random_capital():
                    letter = choice(sonderfolgen_2).lower().capitalize()
                    self.jemals_gross = True
                else:
                    letter = choice(sonderfolgen_2).lower()
            else:
                if self._random_capital():
                    letter = choice(sonderfolgen).lower().capitalize()
                    self.jemals_gross = True
                else:
                    letter = choice(sonderfolgen).lower()
            self.i+= len(letter)

        else:                               # also 15% Wahrsch. --> Zahl
            letter = str(randrange(0, 9))
            self.letter_num = True
            self.jemals_num = True
            self.i += 1

        return letter

    def _random_capital(self):
        # Liefert mit 25% Wahrscheinlichkeit True, sonst False
        return self._random_num() > 25

    def _random_num(self):
        # Random number between 1 and 100
        return randrange(1, 100)


client = PasswordGenerator()
pw = client.create_password(10)
print(pw, len(pw))

