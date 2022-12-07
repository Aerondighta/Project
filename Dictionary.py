import random
from Engine import *

class Dictionary:
    slowo = "puste"
    dlugosc = 0

    def Wczytaj_baze_s(self, zmienna):
        baza = open("dictionary.txt", "r")
        content = baza.readlines()
        baza.close()
        while (True):
            Dictionary.slowo = content[random.randint(0, len(content) - 1)]
            Dictionary.slowo = Dictionary.slowo.strip()
            Dictionary.dlugosc = len(Dictionary.slowo)
            if (self.dlugosc >= zmienna[0] and self.dlugosc <= zmienna[1]):
                return Dictionary

    def Dodawanie_slow(self, sprawdzenie_slowa):
        if Validator.Izogram(sprawdzenie_slowa):
            if self.Sprawdz_czy_jest(sprawdzenie_slowa):
                dodawanie = open("dictionary.txt", "a")
                sprawdzenie_slowa = sprawdzenie_slowa.strip()
                dodawanie.write(f"{sprawdzenie_slowa}\n")
                dodawanie.close()
                return 1
            else:
                print(f"Słowo {sprawdzenie_slowa} jest już w bazie!")
                time.sleep(1)
                return 0

    def Sprawdz_czy_jest(do_sprawdzenia):
        baza = open("dictionary.txt", "r")
        zawartosc = baza.readlines()
        baza.close()
        do_sprawdzenia = do_sprawdzenia.strip()
        for k in range(len(zawartosc)):
            if zawartosc[k].strip() == do_sprawdzenia:
                return False
        return True