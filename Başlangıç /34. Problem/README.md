# Soru 34 - Başlangıç


## Soru 34.1

'Kullanıcıdan 5 adet renk alıp listede saklayan ve ardından listenin son itemini atıp listeyi kullanıcıya gösteren programı tasarlayın.'

Adımlar:
1. boş bir liste oluştur ve bir değişkene ata
2. 5 adımlı bir fon döngüsü başlat.
3. kullanıcıdan her adımda bir renk alıp listeye rengi ekle.
4. döngüyü bitir.
5. listenin son itemini at.
6. listeyi çıktı olarak ekrana yaz. <br>
End

```
renkler = []
for i in range(5):
  renkler.append(input("Lütfen bir renk giriniz: "))
renkler.pop()
print(renkler)
```

## Soru 34.2

'Kullanıcıdan 5 adet renk alıp listede saklayan ve ardından listenin ilk itemini atıp listeyi kullanıcıya gösteren programı tasarlayın.'

Adımlar:
1. boş bir liste oluştur ve bir değişkene ata
2. 5 adımlı bir fon döngüsü başlat.
3. kullanıcıdan her adımda bir renk alıp listeye rengi ekle.
4. döngüyü bitir.
5. listenin ilk itemini bir değişkene ata.
6. değişkeni(son itemi) listeden sil.
6. listeyi çıktı olarak ekrana yaz. <br>
End

```
renkler = []
for i in range(5):
  renkler.append(input("Lütfen bir renk giriniz: "))
ilk_renk = renkler[0]
renkler.remove(ilk_renk)
print(renkler)
```
