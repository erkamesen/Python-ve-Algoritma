# Soru 14 - Başlangıç

## Soru 14.1

'Kullanıcıdan 6 sayı alıp bunları liste şeklinde ve toplamlarını gösteren programı tasarlayın.'

Adımlar:
1. boş bir liste oluştur ve bir değişkene ata.
2. 0 değerinde bir değişken oluştur.
3. 6 adımlık bir döngü başlat.
4. her adımda kullanıcıdan bir sayı girişi al.
5. alınan sayıyı listenin en sonuna ekle.
6. alınan sayı ile oluşturulan 0 değerindeki değişkeni toplayıp sonucu değişkene aktar.
7. listeyi ve toplamı ekrana yaz. <br>
End

```
sayi_listesi = []
toplam = 0
for i in range(6):
  sayi = int(input("Lütfen bir sayı giriniz: "))
  sayi_listesi.append(sayi)
  toplam += sayi
print(f"Liste:\n{sayi_listesi}\nToplam: {toplam}")
```

## Soru 14.2



'Kullanıcıdan 8 sayı alıp bunları tuple şeklinde ve toplamlarını gösteren programı tasarlayın.'

Adımlar:
1. boş bir tuple oluştur ve bir değişkene ata.
2. 0 değerinde bir değişken oluştur.
3. 10 adımlık bir döngü başlat.
4. her adımda kullanıcıdan bir sayı girişi al.
5. alınan sayıyı tuple a ekle.
6. alınan sayı ile oluşturulan 0 değerindeki değişkeni toplayıp sonucu değişkene aktar.
7. listeyi ve toplamı ekrana yaz. <br>
End

```
sayi_demeti = tuple()
toplam = 0
for i in range(10):
  sayi = int(input("Lütfen bir sayı giriniz: "))
  sayi_demeti += (sayi, )
  toplam += sayi
print(f"Tuple:\n{sayi_listesi}\nToplam: {toplam}")
```

