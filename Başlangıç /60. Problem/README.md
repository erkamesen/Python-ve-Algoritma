# Soru 60 - Başlangıç

## Soru 60.1

'kullanıcıdan 5 isim ve notlarını alan ve sözlük biçiminde kullanıcıya gösteren programı tasarlayın.'

Adımlar:
1. Boş bir sözlük oluştur ve değişkene ata.
2. 5 adımlı bir for döngüsü başlat.
3. her adımda kullanıcıdan bir isim alıp değişkene ata.
4. her adımda kullanıcıdan bir not alıp değişkene ata.
5. sözlüğün anahtarı isim value su not olucak şekilde sözlüğe ekle.
6. döngüyü bitir.
7. sözlüğü ekrana çıktı olarak ver. <br>
End

```
sozluk = {}

for i in range(5):
  isim = input("Lütfen isminizi giriniz: ") # erkam ensar enes onur ulaş
  _not = int(input("Lütfen notunuzu giriniz: ")) # 100 21 95 60 43
  sozluk[isim] = _not
print(sozluk)
# {'erkam': 100, 'ensar': 21, 'enes': 95, 'onur': 60, 'ulaş': 43}
```
## Soru 60.2

'Aşağıda verilen sözlüğün value larını alt alta yazdıran programı tasarlayın.
```
sozluk = {1:"bir", 2:"iki", 3:"üç", 4:"dört", 5:"beş", 6:"altı", 7:"yedi", 8:"sekiz", 9:"dokuz", 10:"on"}
```
' <br>
Adımlar:
1. sözlüğün eleman sayısı kadar adımlı, 1 den eleman sayısının bir fazlasına kadar for döngüsü başlat.
2. her adımda sözlüğün keyine adım for döngüsünden gelen değişkeni vererek değerini al.
3. alınan değeri kullanıcıya göster. <br>
End

```
sozluk = {1:"bir",
                  2:"iki",
                  3:"üç",
                  4:"dört",
                  5:"beş",
                  6:"altı",
                  7:"yedi",
                  8:"sekiz",
                  9:"dokuz",
                  10:"on"
                  }
for i in range(1, len(sozluk)+1):
  sayi = sozluk[i]
  print(sayi)
"""
bir
iki
üç
dört
beş
altı
yedi
sekiz
dokuz
on
"""
```
