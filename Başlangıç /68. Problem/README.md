# Soru 68 - Başlangıç


## Soru 68.1 

'Kullanıcıdan 6 adet sayı alıp bu sayıları liste içinde azalan şekilde gösteren programı tasarlayınız.'

Adımlar:
1. Boş bir liste oluştur ve bir değişkene ata.
2. 6 adımlı bir for döngüsü başlat.
3. Her adımda kullanıcıdan bir sayı girişi al ve sayıyı listeye ekle.
4. Döngüyü bitir.
5. listeyi azalan biçimde sırala ve sonucu çıktı olarak ekrana ver. -sort() <br>
End.

```
array = []
for i in range(6):
  sayi = int(input("Lütfen bir sayı giriniz: ")) # 4 87 2 41 11 5
  array.append(sayi)

array.sort(reverse=True)
print(array) # [87, 41, 11, 5, 4, 2]
```

## Soru 68.2 

'Kullanıcıdan 6 adet sayı alıp bu sayıları liste içinde artan şekilde gösteren programı tasarlayınız.'

Adımlar:
1. Boş bir liste oluştur ve bir değişkene ata.
2. 6 adımlı bir for döngüsü başlat.
3. Her adımda kullanıcıdan bir sayı girişi al ve sayıyı listeye ekle.
4. Döngüyü bitir.
5. listeyi artan biçimde sırala ve sonucu çıktı olarak ekrana ver. -sort() <br>
End.

```
array = []
for i in range(6):
  sayi = int(input("Lütfen bir sayı giriniz: ")) # 3 21 72 413 51 25
  array.append(sayi)

array.sort(reverse=True)
print(array) # [3, 21, 25, 51, 72, 413]
```
