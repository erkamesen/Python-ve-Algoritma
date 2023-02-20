# Soru 35 - Başlangıç

## Soru 35.1

'Kullanıcıdan alınan 10 ismi sıralı şekilde alt alta gösteren programı tasarlayın.'

Adımlar:
1. boş bir liste oluştur ve değişkene ata.
2. 10 adımlı bir for döngüsü başlat.
3. her adımda listeye kullanıcıdan bir isim alıp ekle.
4. döngüyü bitir.
5. listeyi ters çevir ve bir değişkene ata.
6. liste içinde dolaşıcak bir for döngüsü başlat.
7. her adımda sonucu ekrana yaz. <br>
End


```
isimler = []
for i in range(10):
  isimler.append(input("Lütfen bir isim giriniz: "))
new_list = isimler[::-1]
for isim in new_list:
  print(isim)
```

## Soru 35.2

'Kullanıcıdan alınan 10 ismi sıralı şekilde ilk ve son isim olmadan alt alta gösteren programı tasarlayın.'

Adımlar:
1. boş bir liste oluştur ve değişkene ata.
2. 10 adımlı bir for döngüsü başlat.
3. her adımda listeye kullanıcıdan bir isim alıp ekle
4. döngüyü bitir.
5. listenin son itemini at.
6. listeyi ters çevir ve bir değişkene ata.
7. listenin son itemini at.
8. liste içinde dolaşıcak bir for döngüsü başlat.
9. her adımda sonucu ekrana yaz. <br>
End


```
isimler = []
for i in range(10):
  isimler.append(input("Lütfen bir isim giriniz: "))
isimler.pop()
new_list = isimler[::-1]
new_list.pop()
for isim in new_list:
  print(isim)
```

