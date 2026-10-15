magazyn = {"Mysz": 5, "Klawiatura": 3, "Monitor": 2}

while True:
    print("\n1 – Stan magazynu")
    print("2 – Przyjecie towaru")
    print("3 – Wydanie towaru")
    print("0 – Zakończ")

    wybor = int(input("Wybierz opcję: "))

    if wybor == 0:
        print("Do widzenia!")
        break

    if wybor == 1:
        for przedmiot, ilosc in magazyn.items():
            print(f"{przedmiot} - {ilosc} szt.")

    elif wybor == 2:
        nazwa_produktu = input("Nazwa produktu: ")
        if nazwa_produktu in magazyn:
            ilosc = int(input("Ilość: "))
            magazyn[nazwa_produktu] += ilosc
        else:
            print("Nie ma takiego produktu w magazynie.")

    elif wybor == 3:
        nazwa_produktu = input("Nazwa produktu: ")
        if nazwa_produktu in magazyn:
            ilosc = int(input("Ilość: "))
            if ilosc > magazyn[nazwa_produktu]:
                print("Nie ma wystarczającej ilości produktu w magazynie.")
            else:
                magazyn[nazwa_produktu] -= ilosc
        else:
            print("Nie ma takiego produktu w magazynie.")


