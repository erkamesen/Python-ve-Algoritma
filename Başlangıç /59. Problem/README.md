# Soru 59 - Başlangıç

## Soru 59.1

'Kullanıcıdan alınan cümle içinde kaç karakter ve kaç kelime olduğunu hesaplayıp cüle ile birlikte bu bilgileri de kullanıcıya gösteren programı tasarlayın.'


Adımlar:
1. Kullanıcıdan bir cümle al ve değişkene ata.
2. değeri 0 olan bir değişken oluştur.
3. cümle içinde dolaşacak bir for döngüsü başlat.
4. her adımda değişkenin değerini 1 arttır.
5. döngüyü bitir.
6. cümleyi boşluklarından ayır ve listeye çevir.
7. listenin eleman sayısını al ve değişkene ata.(kelime sayısı)
8. kullanıcıya bilgileri göster. <br>
End

```
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
```
## Soru 59.2

'Kullanıcıdan alınan cümle içinde kullanıcının belirlendiği kelimenin kaç tane olduğunu kullanıcıya gösteren programı tasarlayın.'

Adımlar:
1. Kullanıcıdan bir cümle al ve değişkene ata.
2. kullanıcıdan bir kelime al ve değişkene ata.
3. cümleyi boşluklarından ayır ve listeye çevirip bir değişkene ata.
4. değeri 0 olan bir değişken oluştur.
5. liste içerisinde dolşacak bir for döngüsü başlat.
6. eğer kullanıcının belirlediği kelime listede varsa değişkenin değerini 1 arttır.
7. kullanıcıya sonucu göster. <br>

```
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
```
