zakupy = []
ilosc_produktow = int(input("Ile produktów chcesz dodać?: "))

for i in range(ilosc_produktow):
    nowy_produkt = input(f"Produkt {i+1}: ")
    zakupy.append(nowy_produkt)

print(f"Lista: {zakupy}")
print(f"Liczba produktow: {len(zakupy)}")
produkt_do_usuniecia = input("Produktu do usuniecia: ")
zakupy.remove(produkt_do_usuniecia)
print(f"Nowa lista: {zakupy}")