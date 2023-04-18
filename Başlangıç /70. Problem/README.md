# Soru 70 - Başlangıç

## Soru 70.1

'Kullanıcıdan integer şekilde 10 adet ID alıp bunu bir listede saklayın. Ardından alınan verilerin liste içinde unique olup olmadığını kontrol eden fonksiyonu tasarlayıp ve eğer listede ki elemanlar unique ise listeyi eğer değil ise "ID ler unique olmalı" çıktısını kullanıcıya verin.'

Adımlar:
1. Boş bir liste oluştur ve değişkene ata.
2. 10 Adımlı bir for döngüsü başlat.
- Her adımda kullanıcıdan bir ID al ve listeye ekle. (int)
- Döngüyü bitir.
3. 1 Adet liste şeklinde parametre alan bir fonksiyon tanımla.
- Alınan parametrenin içinde dolaşıcak bir for döngüsü başlat.
- count() yardımıyla elemanların sayısını kontrol et.
- eğer sıradaki elemanın listedeki toplam adet sayısı 1 ise True döndür
- değilse False döndür.
- Döngüyü bitir.
- Fonksiyonu bitir.
4. fonksiyonu çağır ve parametre olarak listeyi ver sonucu değişkene ata.
5. eğer değişken True ise listeyi çıktı olarak ver.
6. eğer değişken False ise "ID ler unique olmalı" çıktısını ver. <br>
End.

```
ids = []

for i in range(10):
  ids.append(int(input("Lütfen ID yi giriniz: "))  # 1, 4, 4, 3, 5, 2, 7, 11, 52, 30

def unique_control(l):
  for i in(l):
    if l.count(i) == 1:
      return True
    else:
      return False
      
sonuc = unique_control(ids)
if sonuc:
  print(ids)
else:
  print("ID ler unique olmalı")
  
# ID ler unique olmalı
```

## Soru 70.2

'Kullanıcıdan alınan metinin içindeki harf veya rakamların sayısını sözlük yardımı ile kullanıcıya gösteren programı tasarlayın.'

Adımlar:
1. boş bir sözlük oluştur ve bir değişkene ata.
2. Kullanıcıdan bir string bilgi al ve küçük harflerle sağdan ve soldan boşluksuz şekilde değişkene ata.
3. String ifadenin içnide dolaşacak bir for döngüsü başlat.
- Eğer iterasyondan gelen değişken " " ise adımı atla.
- eğer değilse:
- sözlüğün keyini gelen değişkenle eşitle ve .get(değişken, 0) ile gelen değişkenin var olup olmadığını kontrol et ve yoksa değerini 0 alıp 1 arttır.
- eğer sözlük içinde var ise key zaten olacağından değerini bir arttır ve güncelle.
- Döngüyü bitir.
4. Sözlüğü çıktı olarak ver. <br>
End.

```
sozluk = dict()

giris = input("Lütfen bir metin giriniz:").lower().strip() #Erkam Esen

for i in giris:
    if i != "":
        sozluk[i] = sozluk.get(i, 0) + 1
print(sozluk)

# {'e': 3, 'r': 1, 'k': 1, 'a': 1, 'm': 1, ' ': 1, 's': 1, 'n': 1}
```

