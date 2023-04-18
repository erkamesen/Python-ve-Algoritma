"""
'Kullanıcıdan integer şekilde 10 adet ID alıp bunu bir listede saklayın. Ardından alınan verilerin
liste içinde unique olup olmadığını kontrol eden fonksiyonu tasarlayıp ve eğer listede
ki elemanlar unique ise listeyi eğer değil ise "ID ler unique olmalı" çıktısını kullanıcıya verin.'
"""


ids = []

for i in range(10):
  ids.append(int(input("Lütfen ID yi giriniz: "))  # 1, 4, 4, 3, 5, 2, 7, 11, 52, 30

def unique_control(l):
  for i in(l):
    if l.count(i) == 1:
      return True
    else:
      return False
      
sonuc = unique_control(ids)
if sonuc:
  print(ids)
else:
  print("ID ler unique olmalı")
  
# ID ler unique olmalı
