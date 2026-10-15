zadania = []

while True:
    print("\n1 – Dodaj zadanie")
    print("2 – Wyświetl zadania")
    print("3 – Usuń zadanie")
    print("4 – Wyświetl liczbę zadań")
    print("0 – Zakończ")

    wybor_zadania = int(input("Wybierz opcje: "))

    if wybor_zadania == 0:
        print("Do widzenia!")
        break

    elif wybor_zadania == 1:
        zadanie = input("Podaj zadanie: ")
        zadania.append(zadanie)

    elif wybor_zadania == 2:
        for i in range(len(zadania)):
            print(f"{i+1}. {zadania[i]}")

    elif wybor_zadania == 3:
        indeks = int(input("Podaj indeks zadania do usunięcia: "))
        if indeks > 0 and indeks <= len(zadania):
            zadania.pop(indeks-1)
        else:
            print("Nieprawidłowy indeks zadania")

    elif wybor_zadania == 4:
        if len(zadania) > 0:
            print(f"Liczba zadań:  {len(zadania)}")
        else:
            print("Brak zadań")

    else:
        print("Nieprawidłowy wybór")
