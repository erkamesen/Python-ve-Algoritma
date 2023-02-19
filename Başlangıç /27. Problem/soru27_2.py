"""
'kullanıcıdan alınan 5 adet sayıyı bir array de saklayıp ardından kullanıcıya
sadece artık yılları(sadece 4 e bölünebilmesi yeterli) gösteren programı tasarlayın.'
"""


import array as arr

def artik_yil(year):
  if year %4 == 0:
    return True
  else:
    return False

a = arr.array("i", [])
for i in range(5):
  a.append(int(input("Lütfen bir yıl giriniz: "))

for i in range(5):
  yil = a[i]
  if artik_yil(year=yil):
    print(f"{yıl} Artık Yıldır.")
  else:
    print(f"{yıl} Artık Yıl Değildir.")
