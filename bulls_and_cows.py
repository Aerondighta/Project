from Dictionary import *
import time

d = Dictionary()
m = Maszyna([0,50], 10)
v = Validator(0, 0)
poziom=[0,50]
wyniki = [0,0]
while(True):
    print("\n\n1. Nowa gra.")
    print("2. Zasady.")
    print("3. Zmiana trudności.")
    print("4. Wyswietl i zapisz wyniki.")
    print("5. Dodaj nowe słowa do bazy.")
    print("6. Koniec.")
    wybor = input("Podaj swoj wybor: \n")
    if(int(wybor) == 1):
        w = m.Engine(d.Wczytaj_baze_s(poziom))
        if w == True:
            wyniki[0] += 1
        else:
            wyniki[1] += 1
    elif(int(wybor) == 2):
        print(f"{m.zasady}")

    elif(int(wybor) == 3):
        print("1. Zmiana ilości prób.")
        print("2. Zmiana trudności (długości) hasła.")
        wybor3 = input("Podaj wybór: ")
        poziom = m.zmiana_ustawien(wybor3)

    elif(int(wybor) == 4):
        m.Zapis_i_wyswietlenie(wyniki)

    elif(int(wybor) == 5):
        dodanie_slowa = input("Jakie slowo chcesz dodać? ")
        d.Dodawanie_slow(dodanie_slowa)

    elif(int(wybor) == 6):
        break

    else:
        print("Nie ma takiej opcji do wyboru!")
        time.sleep(1)