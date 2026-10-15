from operator import truediv

napoje = ["Woda", "Sok", "Cola"]
ceny = [3, 5, 6]
suma = []
i = 0
while i < len(napoje):
    print(f"{i+1}. {napoje[i]} - {ceny[i]} zl")
    i += 1
print("0. Zakoncz")
while True:
    opcja = int(input("Wybierz opcje: "))
    if opcja == 0:
        break
    else:
        suma.append(ceny[opcja-1])
        print(f"Wybranp: {napoje[opcja-1]}, cena {ceny[opcja-1]} zl")
print(f"Lacznie do zaplaty: {sum(suma)} zl")