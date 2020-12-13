Koty =[
    {'kot':'rudy', 'ilosc' :1,'wiek': 4, 'cena':1000},
    {'kot':'szary','ilosc':2, 'wiek': 2, 'cena': 2500},
    {'kot':'bialy','ilosc':3, 'wiek': 1, 'cena' :1500 }
    ]
suma = 0
for poz in Koty:
            i = poz['ilosc']
            c = poz['cena']
            suma= suma + (c* i)
print(suma)

suma=0
for poz in Koty:
    i=poz['ilosc']
    w=  poz ['wiek']
    suma1= suma+ (w*i)
    print(suma1)

for caly_kot in Koty:

    if caly_kot['cena'] <1500:
        print(caly_kot['kot'])
