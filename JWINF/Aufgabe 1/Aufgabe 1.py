import random
from random import choice
from random import randrange

# Konsonanten
KONSONANTEN = ["B", "D", "F", "G", "H", "K", "L", "M", "N", "P", "R", "S", "T", "V", "W"]
KONSONANTEN_SELTEN = ["C", "J", "X", "Y", "Z"]
DOPPELKONSONANTEN = ["NN", "MM", "LL", "SS", "TT", "FF"]

SONDERFOLGEN_2 = ["SP", "ST", "CH", "PH", "QU", "CK"]
SONDERFOLGEN = SONDERFOLGEN_2 + ["SCH"]
SONDERFOLGEN_ANFANG_2 = ["SP", "ST", "CH", "PH", "QU"]
SONDERFOLGEN_ANFANG = SONDERFOLGEN_ANFANG_2 + ["SCH"]

# Vokale
VOKALE = ["A", "E", "I", "O", "U"]
UMLAUTE = ["AE", "UE", "OE", "AU", "EU", "EI", "AI"]
DOPPELVOKALE = ["AA", "AH", "EE", "EH", "UH", "OH", "OO", "IE"]

# Steuergroessen
MINLAENGE = 5

# Regeln:
# 0) Allgemein gilt bei Zeichen: Zufall
# 1) In der Regel abwechselnd Vokal & Konsonant
#    - Außer: Doppelekonsonannten, Umlaute gedehnte Vokale (Doppelvokale), Sonderfolgen von Konsonanten
# 2) Am Anfang oder nach einer Zahl 75% Wahrsch. groß
# 3) Mit Wahrsch 15% kommt eine Zahl, Zahl nach Zahl möglich, aber unwahrscheinlich
# 4) Nach einer Zahl wie am Wortanfang starten (Groß / Klein etc)
# 5) Passwort enthält immer eine Zahl, wenn nicht per Zufall beim Generieren der ersten Zeichen, dann am Ende
# 6) Passwort enthält immer einen Großbuchstaben, wenn nicht per Zufallsalgo, wird der erste groß gesetzt


class PasswordGenerator:
    def __init__(self):
        self.password = ""              # Initialisierung des Passwort-Strings
        self.i = 0                      # Laufvariable, Position im Password-String
        self.letter_num = False         # Flag, dass sagt, dass das letzte Zeichen eine Zahl war
        self.jemals_num = False         # Flag, dass ich setze, wenn eine Zahl kommt
        self.jemals_gross = False       # Flag, dass ich setze, wenn ein Grossbuchstabe kommt
        self.vokal = None               # Flag, dass sagt, dass das letze Zeichen ein Vokal war

    def create_password(self, length):
        # Prüfung, ob die minimale Passwortlänge gegeben ist
        if length < MINLAENGE:
            print(f"Length too short, minimum {MINLAENGE} letters!")
            return "error"

        # Erstes Zeichen des Passworts
        letter = self._first_letter_algorithm(length)
        self.password += letter

        # Mittlere Zeichen (meist zweites, ggf. 3./4. je nach Länge ersten Zeichenfolge)
        while self.i < length - 1:
            if self.letter_num:                     # Wenn letztes Zeichen Zahl, wieder die Fkt des ersten Zeichens
                self.letter_num = False
                letter = self._first_letter_algorithm(length)
            else:
                self.letter_num = False
                random_num = self._random_num()     # Zufallszahl zwischen 1 und 100
                if random_num <= 10:                # Mit 10% Wahrsch eine Zahl
                    letter = str(randrange(0, 9))
                    self.letter_num = True
                    self.jemals_num = True
                    self.i += 1
                elif self.vokal:                    # Vorher Vokal, also nun Konsonant
                    self.vokal = False
                    if random_num <= 75:            # Einfacher Konsonant mit (75-10)%= 65% Wahrsch
                        if self._random_konsonant():
                            letter = choice(KONSONANTEN).lower()
                        else:
                            letter = choice(KONSONANTEN_SELTEN).lower()
                        self.i += 1
                    elif random_num <= 90:          # Doppelkonsonant mit (90-75)%= 15% Wahrsch
                        letter = choice(DOPPELKONSONANTEN).lower()
                        self.i += 2
                    else:                           # Sonderfolge mit 10% Wahrsch.
                        if length-self.i > 3:       # inkl. 3-Zeichen langer Sonderfolgen nur, wenn es noch passt
                            letter = choice(SONDERFOLGEN).lower()
                        else:
                            letter = choice(SONDERFOLGEN_2).lower()
                        self.i += len(letter)

                else:                               # Vorher Konsonant, also nun Vokal
                    self.vokal = True
                    if random_num <= 80:            # Einfacher Vokal mit 80-15%= 65% Wahrsch
                        letter = choice(VOKALE).lower()
                        self.i += 1
                    elif random_num <= 90:          # Doppelvokal mit 10% Wahrsch
                        letter = choice(DOPPELVOKALE).lower()
                        self.i += 2
                    else:                           # Umlaut mit 10% Wahrsch
                        letter = choice(UMLAUTE).lower()
                        self.i += 2
            self.password += letter

        # Da ich Doppelfolgen von Buchstaben zulasse, kann es bei der vorherigen while-Schleife sein,
        # dass schon die geforderte Anzahl an Buchstaben erreicht ist.
        # In der Regel ist aber noch eine Stelle frei.
        # Diese wird nun besetzt. Ich nutze dies, um eine Zahl zu vergeben, wenn noch keine im Wort ist
        if len(self.password) < length:         # Noch ein Zeichen Platz am Ende
            if  self.jemals_num == False:
                letter = str(randrange(0, 9))
                self.letter_num = True
                self.jemals_num = True

            else:
                if self.vokal == True:
                    if self._random_konsonant():
                        letter = choice(KONSONANTEN).lower()
                    else:
                        letter = choice(KONSONANTEN_SELTEN).lower()
                else:
                    letter = choice(VOKALE).lower()
            self.i += 1
            self.password += letter

        else:                                   # Alle zeichen schon voll
            if self.jemals_num == False:        # Sonderfall keine Zahl --> Zahl ans Ende
                # self.password = str(randrange(0, 9)) + self.password[1:]
                self.password = self.password[:-1] + str(randrange(0, 9))
                # print("Letzten Buchstaben zur Zahl gemacht")

        if self.jemals_gross == False:          # Sonderfall kein großer Buchstabe --> ersten ersetzen
            if not self.password[0].isnumeric():
                self.password = self.password.capitalize()
            else:
                str1 = ""
                cap = False
                for x in self.password:
                    if not cap and not x.isnumeric():
                        x = x.upper()
                        cap = True
                    str1 += x
                self.password = str1

        return self.password

    # Liefert ein zufälliges erstes Zeichen bzw. eine Zeichenfolge;
    # Wird auch aufgerufen nach Zahl im Passwort
    def _first_letter_algorithm(self, length):
        random_num = self._random_num()             # Zufallszahl zwischen 1 und 100
        letter = ""
        self.letter_num = False
        self.vokal = False

        if random_num <= 30:                        # Einfacher Vokal mit 30% Wahrsch
            if self._random_capital():              # Großbuchstabe mit gewisser Wahrsch. (aktuell 75%)
                letter = choice(VOKALE)
                self.jemals_gross = True
            else:                                   # Kleinbuschstabe mit gewisser Wahrsch
                letter = choice(VOKALE).lower()
            self.vokal = True
            self.i += 1

        elif random_num <= 40:                      # Umlaut mit 10% (am Anfang kein Doppelvokal)
            if self._random_capital():              # Großbuchstabe am Anfang
                letter = choice(UMLAUTE).lower().capitalize()
                self.jemals_gross = True
            else:                                   # Kleinbuchstabe am Anfang
                letter = choice(UMLAUTE).lower()
            self.vokal = True
            self.i += 2

        elif random_num <= 75:                      # Einfacher Konsonant mit 35%
            if self._random_konsonant():
                kons = choice(KONSONANTEN)
            else:
                kons = choice(KONSONANTEN_SELTEN)
            if self._random_capital():              # Großbuchstabe
                letter = kons
                self.jemals_gross = True
            else:                                   # Kleinbuchstabe
                letter = kons.lower()
            self.i += 1

        elif random_num <= 85:                      # Sonderfolge mit 10%
            if length-self.i < 3:                   # Diese Abfrage braucht es eigentlich nicht mehr
                if self._random_capital():
                    letter = choice(SONDERFOLGEN_ANFANG_2).lower().capitalize()
                    self.jemals_gross = True
                else:
                    letter = choice(SONDERFOLGEN_ANFANG_2).lower()
            else:
                if self._random_capital():
                    letter = choice(SONDERFOLGEN_ANFANG).lower().capitalize()
                    self.jemals_gross = True
                else:
                    letter = choice(SONDERFOLGEN_ANFANG).lower()
            self.i+= len(letter)

        else:                                   # also 15% Wahrsch. --> Zahl
            letter = str(randrange(0, 9))
            self.letter_num = True
            self.jemals_num = True
            self.i += 1

        return letter

    def _random_capital(self):
        # Liefert mit 75% Wahrscheinlichkeit True, sonst False
        return self._random_num() > 25

    def _random_konsonant(self):
        # Liefert mit 90% Wahrscheinlichkeit True, sonst False
        return self._random_num() > 10

    def _random_num(self):
        # Zufallszahl zwischen 1 und 100
        return randrange(1, 100)


for x in range(25):
    client = PasswordGenerator()
    pw = client.create_password(8)
    print(pw, len(pw))
    client = PasswordGenerator()
    pw = client.create_password(10)
    print(pw, len(pw))
    client = PasswordGenerator()
    pw = client.create_password(14)
    print(pw, len(pw))

