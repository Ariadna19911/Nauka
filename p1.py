koszyk = [
    {'produkt': 'mleko', 'ilosc': 4, 'cena':2},
    {'produkt': 'czekolada', 'ilosc': 2, 'cena': 2.5},
    {'produkt': 'konserwa', 'ilosc': 1, 'cena' :3.5 }
    ]

suma = 0
for poz in koszyk:
        il = poz ['ilosc']
        c = poz['cena']
        suma= suma + (c* il)
print(suma)
