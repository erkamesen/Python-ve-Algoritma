"""
'Parametre olarak liste alan ve listeyi tam tersine çevirip kullanıcıya gösteren fonksiyonla programı tasarlayın.'
"""


def ters_liste(l):
  yeni_liste = []
  for i in range(len(l)):
    elem = l.pop()
    yeni_liste.append(elem)
  return yeni_liste

sonuc = ters_liste([1 ,2, 3, 4, 5]) 
print(sonuc) # [5, 4, 3, 2, 1]
