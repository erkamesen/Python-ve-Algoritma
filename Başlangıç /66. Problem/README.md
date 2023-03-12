# Soru 66 - Başlangıç


## Soru 66.1 

'Parametre olarak liste alan ve listeyi tam tersine çevirip kullanıcıya gösteren fonksiyonla programı tasarlayın.'

Adımlar:
1. Bir adet parametre alan bir fonksiyon tanımla.
- boş bir liste oluştur ve bir değişkene ata
- parametre olarak alınan listenin uzunluğu kadar bir for döngüsü başlat.
- her adımda listenin son elemanını al ve bir değişkene ata. 
- değişkeni oluşturulan listenin sonuna ekle.
- döngüyü bitir.
- listeyi döndür
2. Fonksiyonu çağır ve sonucu bir değişkene ata.
3. değişkeni çıktı olarak ver. <br>
End.

```
def ters_liste(l):
  yeni_liste = []
  for i in range(len(l)):
    elem = l.pop()
    yeni_liste.append(elem)
  return yeni_liste

sonuc = ters_liste([1 ,2, 3, 4, 5]) 
print(sonuc) # [5, 4, 3, 2, 1]
```

## Soru 66.2 

'Parametre olarak liste alan ve listeyi tam tersine çevirip tuple şeklinde kullanıcıya gösteren fonksiyonla programı tasarlayın.'

Adımlar:
1. Bir adet parametre alan bir fonksiyon tanımla.
- boş bir tuple oluştur ve bir değişkene ata
- parametre olarak alınan listenin uzunluğu kadar bir for döngüsü başlat.
- her adımda listenin son elemanını al ve bir değişkene ata. 
- değişkeni oluşturulan tuple a ekle.
- döngüyü bitir.
- tuple ı döndür
2. Fonksiyonu çağır ve sonucu bir değişkene ata.
3. değişkeni çıktı olarak ver. <br>
End.

```
def ters_tuple(l):
  yeni_tuple = ()
  for i in range(len(l)):
    elem = l.pop()
    yeni_tuple += (elem,)
  return yeni_tuple

sonuc = ters_tuple([3 ,4, 1, 7, 13]) 
print(sonuc) # [13, 7, 1, 4, 3]
```
