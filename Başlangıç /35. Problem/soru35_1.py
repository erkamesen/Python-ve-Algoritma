"""
'Kullanıcıdan alınan 10 ismi sıralı şekilde alt alta gösteren programı tasarlayın.'
"""


isimler = []
for i in range(10):
  isimler.append(input("Lütfen bir isim giriniz: "))
new_list = isimler[::-1]
for isim in new_list:
  print(isim)
