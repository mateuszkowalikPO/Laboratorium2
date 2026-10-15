liczba_studentow = int(input("Podaj liczbe studentow: "))
punkty = []
zaliczeni = 0

for i in range(liczba_studentow):
    punkty_studenta = int(input(f"Punkty studenta {i + 1}: "))
    punkty.append(punkty_studenta)
    if punkty_studenta >= 0 and punkty_studenta <= 49:
        ocena = 2.0
    elif punkty_studenta >= 50 and punkty_studenta <= 59:
        ocena = 3.0
    elif punkty_studenta >= 60 and punkty_studenta <= 68:
        ocena = 3.5
    elif punkty_studenta >= 70 and punkty_studenta <= 79:
        ocena = 4.0
    elif punkty_studenta >= 80 and punkty_studenta <= 89:
        ocena = 4.5
    elif punkty_studenta >= 90 and punkty_studenta <= 100:
        ocena = 5.0

    if ocena >= 3.0:
        zaliczeni += 1

sum = sum(punkty)
len = len(punkty)
avg = sum / len

print(f"Średnia: {avg}")
print(f"Najwyzszy wynik: {max(punkty)}")
print(f"Najnizszy wynik: {min(punkty)}")
print(f"Wynik rosnaco: {sorted(punkty)}")
print(f"Liczba zaliczen: {zaliczeni}")