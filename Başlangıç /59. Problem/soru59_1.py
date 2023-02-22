"""
'Kullanıcıdan alınan cümle içinde kaç karakter ve kaç kelime olduğunu hesaplayıp cüle ile birlikte
bu bilgileri de kullanıcıya gösteren programı tasarlayın.'
"""

cumle = input("Lütfen bir cümle giriniz: ") # merhaba benim adım erkam ve 15 senedir metal grubum var. gitar ve bateri çalabildiğim enstrumanlar.

toplam = 0
for karakter in cumle:
  toplam += 1
kelime_sayisi = len(cumle.split())
print(f"Senin cümlen:\n{cumle}\nToplam Karakter:\n{toplam}\nKelime Sayısı:\n{kelime_sayisi}")
"""
Senin cümlen:
merhaba benim adım erkam ve 15 senedir metal grubum var. gitar ve bateri çalabildiğim enstrumanlar.
Toplam Karakter:
99
Kelime Sayısı:
15
"""
