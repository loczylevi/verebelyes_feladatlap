#A Vasember;1;2008-05-02;140;585
"""
Fekete Párduc a film címe
3 a szám, mely jelzi, hogy a film hányadik ún. „fázisba” tartozik
2018-02-16 a film bemutatójának dátuma
205 a film gyártási költségei (millió $-ban)
1347 a film mozijegyek értékesítéséből származó bevétele (millió $-ban) 
"""

class Marvel:
  def __init__(self,sor):
    cim,fazis,bemutato,koltseg,bevetel = sor.strip().split(";")
    self.cim = cim
    self.fazis = int(fazis)
    self.bemutato = bemutato
    self.koltseg = int(koltseg)
    self.bevetel = int(bevetel)

with open("marvel.txt",encoding="utf-8") as f:
  lista = [Marvel(sor) for sor in f]


def filmek_szama(lista):
  return len(lista)
  
print(f"3.1: {filmek_szama(lista)} filmje van a marvel moziverzumának")

def harmadik_fazis(lista):
  return len([sor for sor in lista if sor.fazis < 3])
  
print(f"3.2: a 3.fázis elötti filmek száma: {harmadik_fazis(lista)} db.")

def legkisebb(lista):
  k = [sor.bevetel - sor.koltseg for sor in lista][0]
  for sor in lista:
    if sor.bevetel - sor.koltseg < k:
      k = sor.bevetel - sor.koltseg
      cim = sor.cim
  return cim
  
print(f"3.3: a legalacsonyabb hasznot a(z): {legkisebb(lista)} c. film hozta")
  
    
def film_cimreszlet(lista,cimreszlet):
  tarolo = ""
  kereso = [sor.cim for sor in lista if cimreszlet in sor.cim]
  for sor in kereso:
    tarolo += "  " + sor + "\n"
  return tarolo


print(f"3.4: alábbi filmek címében szerepel ez a kifejezés:")

film_cimreszlet = film_cimreszlet(lista,"Pókember")
print(film_cimreszlet)





