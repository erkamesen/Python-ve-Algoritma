"""
'Kullanıcıdan alınan 10 ismi sıralı şekilde ilk ve son isim olmadan alt alta gösteren programı tasarlayın.'
"""

isimler = []
for i in range(10):
  isimler.append(input("Lütfen bir isim giriniz: "))
isimler.pop()
new_list = isimler[::-1]
new_list.pop()
for isim in new_list:
  print(isim)
