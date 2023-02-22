# Soru 46 - Başlangıç

## Soru 46.1

'Kullanıcıdan 5 adet not alıp bunları arrayde saklayan, ardından kullanıcının ismini de alıp, notların ortlaması hesaplayan ve notlarla sırasıyla aşağıdaki tabloyu dolduran programı tasarlayın.
```
Merhaba {kullanıcı adı}
Not Ortalaman: {notların ortalaması}
Tüm Notlar:
İngilizce: {not 1}
Matematik: {not 2}
Fizik: {not 3}
Türkçe: {not 4}
Kimya: {not 5}
```

Adımlar:
1. array modülünün içinden array fonksiyonunu import et.
2. bir array oluştur ve değişkene ata.
3. kullanıcıdan bir isim al ve değişkene ata.
4. değeri 0 olan bir değişken oluştur.
5. 5 adımlı bir for döngüsü başlat.
6. her adımda kullanıcıdan bir not alıp notu bir değişkene ata
7. array e alınan notu ekle.
8. her adımda alınan notu değeri 0 olan sayının değerinin üstüne ekle.
9. döngüyü bitir.
10. toplam değişkenini 5 e böl ve sonucu bir değişkene ata.
11. eldeki bilgiler ve index yardımı ile tabloyu oluştur. <br>
End

```
from array import array

a = array("i", [])

isim = input("Lütfen isminizi giriniz: ") # Erkam
toplam = 0
for i in range(5):
  ders_notu = int(input("Lütfen notunuzu giriniz: ")) # 50 80 80 60 70
  a.append(ders_notu)
  toplam += ders_notu
ortalama = toplam/5  
print(f"Merhaba {isim}\nNot Ortalaman: {ortalama}\nTüm Notlar:\nİngilizce: {a[0]}\nMatematik: {a[1]}\nFizik: {a[2]}\nTürkçe: {a[3]}\nKimya: {a[4]}")

"""
Merhaba Erkam
Not Ortalaman: 68.0
Tüm Notlar:
İngilizce: 50
Matematik: 80
Fizik: 80
Türkçe: 60
Kimya: 70
"""
```

## Soru 46.2

'Kullanıcıdan 6 adet sayı alıp bunları arraye ekleyen ardından tüm sayıların ortalamalarının 1 hariç ilk tam bölen sayısını bulan programı tasarlayın.'

Adımlar:
1. array modülünün içinden array fonksiyonunu import et.
2. değeri 0 olan br değişken oluştur.
3. bir array oluştur ve değişkene ata.
4. 6 adımlı bir for döngüsü başlat.
5. her adımda gelen sayıyı bir değişkene ata.
6. array e alınan sayıyı ekle.
7. her adımda alınan sayıyı değeri 0 olan sayının değerinin üstüne ekle.
8. döngüyü bitir.
9. toplam değişkenini 6 ile böl ve sonucu bir değişkene ata.
10. değeri 2 olan bir değişken oluştur.
11. doğruyken sonsuza kadar süren bir while döngüsü başlat.
12. eğer ortalama değişkeni değeri 2 olan değişkene tam bölünmüyorsa değerini 1 arttır başa sar.
13. eğer bölünüyorsa bölümün değerini çıktı olarak ekrana ver.
14. Döngüyü bitir. <br>
End

```
from array import array

toplam = 0
a = array("i", [])

for i in range(6):
  sayi = int(input("Lütfen bir sayı giriniz: ")) # 1444 23 32 767645 23 52342
  a.append(sayi)
  toplam += sayi
  
ortalama = toplam/6 # 136919
bolen = 2
while True:
  if ortalama %bolen != 0:
    bolen += 1
  else:
    print(bolen)
    break
# 23
```


