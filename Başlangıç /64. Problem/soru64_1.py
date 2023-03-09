"""
'kullanıcıdan alınan not miktarına göre aşağıda ki tabloda verilen burs miktarnı hesaplayıp kullanıcıya gösteren programı tasarlayın.

Not 1100'e eşitse 100% burs.
Not 1000'den büyükse 80% burs.
Not 900'den büyükse 60% burs.
Not 800'den büyükse 40% burs.
Not 700 veya 700'den büyükse 30% burs.
Not 700'den küçükse burs yok.

'
"""


ogrenci_notu = int(input("Lütfen notunuzu giriniz: "))
if ogrenci_notu == 1100:
  print("100% burs")
elif ogrenci_notu > 1000:
  print("80% burs")
elif ogrenci_notu > 900:
  print("60% burs")
elif ogrenci_notu > 800:
  print("40% burs")
elif ogrenci_notu >= 700:
  print("30% burs")
elif ogrenci_notu < 700:
  print("burs yok")
