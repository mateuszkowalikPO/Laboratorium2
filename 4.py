temperatury = []
powyzej_sredniej = []
for i in range(7):
    podaj_temperature = int(input(f"Dzien {i+1}: "))
    temperatury.append(podaj_temperature)
avg = sum(temperatury)/len(temperatury)
for i in range(len(temperatury)):
    if temperatury[i] > avg:
        powyzej_sredniej.append(temperatury[i])
print(f"\nSrednia: {avg}")
print(f"Najwyzsza: {max(temperatury)} C")
print(f"Najnizsza: {min(temperatury)} C")
print(f"Powyzej sredniej: {powyzej_sredniej}")
print(f"Liczba dni: {len(powyzej_sredniej)}")