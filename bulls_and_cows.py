from Dictionary import *
import time

d = Dictionary()
m = Maszyna([0,50], 10)
v = Validator(0, 0)
zmienna=[0,50]
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
        w = m.Engine(d.Wczytaj_baze_s(zmienna))
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
        if(int(wybor3) == 1):
            m.proby = int(input("Ile chcesz mieć prób? "))
        elif(int(wybor3) == 2):
            print("Wybierz poziom: ")
            print("1. Łatwy (3-4 litery)\n2. Średni (5-6 liter)\n3. Trudny (7+ liter)")
            wyborl = int(input())
            zmienna = m.Zmiana_poziomu(wyborl)
            print(zmienna)

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