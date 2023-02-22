"""
'Kullanıcıdan alınan cümle içinde " " karakterleri hariç kaç karakterli olduğunu hesaplayan prgoramı tasarlayın.'
"""


cumle = input("Lütfen bir cümle giriniz: ") # Python yüksek seviye ve nesne yönelimli bir dildir.

toplam = 0
for karakter in cumle:
  if karakter == " ":
    continue
  else:
    toplam +=1
print(toplam) # 43
