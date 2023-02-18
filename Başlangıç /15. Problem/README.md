# Soru 15 - Başlangıç

## Soru 15.1
'Kullanıcıdan 6 adet sayı alıp listeye ekleyen ve listeyi ilk düz ardından ters şekilde kullanıcıya gösteren programı tasarlayın.'

Adımlar:
1. Boş bir liste oluştur ve bir değişkene ata.
2. 6 adımlı bir for döngüsü başlat.
3. her adımda kullanıcıdan bir sayı girdisi alıp listeye ekle.
4. listeyi kullanıcıya göster .
5. listeyi ters çevir ve kulanıcıya göster. <br>
End

```
sayi_listesi = []
for i in range(6):
  sayi = int(input("Lütfen bir sayı giriniz: "))
  sayi_listesi.append(sayi)
print(sayi_listesi)
print(sayi_listesi[::-1])
```

## Soru 15.2

'Kullanıcıdan 6 adet sayı alıp tuple a ekleyen ve ardından tuple ı ilk kullanıcıya gösterdikten sonra temizleyen programı tasarlayın.'

Adımlar:
1. Boş bir tuple oluştur ve bir değişkene ata.
2. 6 adımlı bir for döngüsü başlat.
3. her adımda kullanıcıdan bir sayı girdisi alıp tuple a ekle.
4. tuple ı kullanıcıya göster .
5. tuple temizle. <br>
End

```
sayi_demeti = tuple()
for i in range(6):
  sayi = int(input("Lütfen bir sayı giriniz: "))
  sayi_demeti += (sayi,)
print(sayi_demeti)
sayi_demeti.clear()
```
