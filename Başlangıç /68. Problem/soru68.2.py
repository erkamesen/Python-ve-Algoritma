"""
'Kullanıcıdan 6 adet sayı alıp bu sayıları liste içinde artan şekilde gösteren programı tasarlayınız.'
"""



array = []
for i in range(6):
  sayi = int(input("Lütfen bir sayı giriniz: ")) # 3 21 72 413 51 25
  array.append(sayi)

array.sort(reverse=True)
print(array) # [3, 21, 25, 51, 72, 413]
