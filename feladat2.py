banan = 569
szolo = 1698
dinnye = 499

amig = True
lista = []
while amig:
  bekeres = input("kíván valamit vásárolni? ")
  if bekeres == "igen":
    melyik = input("melyik termékből? ")
    if melyik == "banán":
      hany = float(input("Hány Kg banán(o)t szeretne? "))
      bananossz = hany * banan
      lista.append(bananossz)
    if melyik == "dinnye":
      hany = float(input("Hány Kg dinnye(o)t szeretne? "))
      dinnyeossz = hany * dinnye
      lista.append(dinnyeossz)
    if melyik == "szőlő":
      hany = float(input("Hány Kg szőlő(o)t szeretne? "))
      osszszolo = hany * szolo
      lista.append(osszszolo)
    elif melyik != "dinnye" and  melyik != "banán" and melyik != "szőlő":
      print("Nincs ilyen termék! ")
      continue
  elif bekeres == "nem":
    amig = False
    
print(f"Köszönjük a vásárlást! ")
if len(lista) > 0:
  print(f"Fizetendő összeg: {sum(lista)}Ft")
