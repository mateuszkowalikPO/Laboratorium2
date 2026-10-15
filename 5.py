haslo = "Python123"
licznik = 0

while licznik < 3:
    haslo_uzytkownika = input("Podaj haslo: ")

    if haslo_uzytkownika == haslo:
        print("Logowanie udane")
        break

    else:
        licznik += 1
        print("Niepoprawne haslo. Pozostale proby: ", 3 - licznik)