from Validator import *
import time

class Maszyna:
    level = [0,50]
    proby = 10
    probyl = proby
    def __init__(self, x=[0,50], y=10):
        self.level = x
        self.proby = y

    zasady = "Zasady gry:\n Tekstowa gra w której komputer (Host) losuje słowo, które jest izogramem i informuje użytkownika (Guesser)\n o ilości liter w słowie. Użytkownik (Guesser) stara się zgadnąć co to za słowo. Komputer (Host) po każdej\n próbie zwraca liczbe Cows i Bulls. Liczba Cows oznacza poprawną literę występującą w słowie lecz na złej pozycji,\n"" liczba przy słowie Bulls oznacza poprawną literę na poprawnej pozycji. Gra kończy się kiedy liczba przy Bulls będzie\n taka sama jak długość słowa wylosowanego przez komputer.\n"

    def BiC(slowo1, g, stats1):
        for i in range(slowo1.dlugosc):
            for j in (range(slowo1.dlugosc)):
                if (slowo1.slowo[i] == g[j]):
                    Validator.cows += 1
            if (slowo1.slowo[i] == g[i]):
                Validator.cows -= 1
                Validator.bulls += 1
        return stats1

    def Engine(self, slowo1):
        print(f"Wylosowano słowo o długości: {slowo1.dlugosc} znaków.")
        self.probyl = self.proby
        while (True):
            Validator.cows = 0
            Validator.bulls = 0
            g = input("Zgadni jakie to słowo. ")
            if(Validator.Izogram(g) == False):
                continue
            elif(slowo1.dlugosc != len(g)):
                print("Podaj słowo o takiej samej ilości liter jak wylosowane!")
                continue

            Maszyna.BiC(slowo1, g, Validator)

            print(f"cows: {Validator.cows}, bulls: {Validator.bulls}")
            time.sleep(1.5)

            if(Validator.bulls == slowo1.dlugosc):
                print("Wygrałeś!!!")
                time.sleep(1.5)
                return True
            self.probyl -= 1
            print(f"Pozostało {self.probyl} prób.")
            time.sleep(1.5)
            if(self.probyl <= 0):
                print("Koniec prób. Przegrałeś!!!")
                print(f"Poprawne słowo to {slowo1.slowo}")
                time.sleep(1)
                return False

    def Zapis_i_wyswietlenie(self, ziw):
        print(f"Wygrane: {ziw[0]} przegrane: {ziw[1]}")
        wynik = open("highscores.txt", "a")
        wynik.write(f"\n{ziw[0]}/{ziw[1]}")
        wynik.close()
        time.sleep(1)
        return 0

    def Zmiana_poziomu(poziomtt):
        tab=[0,50]
        if poziomtt == 1:
            tab=[3,4]
        elif poziomtt == 2:
            tab=[5,6]
        elif poziomtt == 3:
            tab=[7,50]
        else:
            print("Nie ma takiego poziomu!")
        return tab

    def zmiana_ustawien(self, wybor3):
        if(int(wybor3) == 1):
            self.proby = int(input("Ile chcesz mieć prób? "))
        elif(int(wybor3) == 2):
            print("Wybierz poziom: ")
            print("1. Łatwy (3-4 litery)\n2. Średni (5-6 liter)\n3. Trudny (7+ liter)")
            wyborl = int(input())
            return self.Zmiana_poziomu(wyborl)