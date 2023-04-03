"""
'Kullanıcıdan 6 adet sayı alıp bu sayıları liste içinde azalan şekilde gösteren programı tasarlayınız.'
"""


array = []
for i in range(6):
  sayi = int(input("Lütfen bir sayı giriniz: ")) # 4 87 2 41 11 5
  array.append(sayi)

array.sort(reverse=True)
print(array) # [87, 41, 11, 5, 4, 2]
