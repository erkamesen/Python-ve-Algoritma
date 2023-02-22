"""
'Kullanıcıdan alınan cümle içinde kullanıcının belirlendiği kelimenin kaç tane olduğunu kullanıcıya gösteren programı tasarlayın.'
"""


cumle = input("Lütfen bir cümle giriniz: ") # bir mumdur, iki mumdur, üç mumdur, dört mumdur
kelime_kontrol = input("Lütfen aranacak kelimeyi giriniz: ") # mumdur

kelime_listesi = cumle.split()

toplam = 0
for kelime in kelime_listesi:
  if kelime_kontrol == kelime:
    toplam +=1
  else:
    continue
print(f"{kelime_kontrol} kelimesinden toplam {toplam} adet mevcut.") # 4
# mumdur kelimesinden toplam 4 adet mevcut.
