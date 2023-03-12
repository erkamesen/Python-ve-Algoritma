"""
'Parametre olarak liste alan ve listeyi tam tersine çevirip tuple şeklinde kullanıcıya gösteren fonksiyonla programı tasarlayın.'
"""


def ters_tuple(l):
  yeni_tuple = ()
  for i in range(len(l)):
    elem = l.pop()
    yeni_tuple += (elem,)
  return yeni_tuple

sonuc = ters_tuple([3 ,4, 1, 7, 13]) 
print(sonuc) # [13, 7, 1, 4, 3]
