# Soru 40 - Başlangıç



## Soru 40.1

'kullanıcıdan alınan kullanıcı adının sadece harf veya rakamdan oluşup oluşmadığını kontrol eden fonksiyonla beraber programı tasarlayın.'

Adımlar:
1. 1 parametre alan bir fonksiyon tanımla.
- eğer kullanıcı adının içinde sadece harf veya rakam varsa True döndür.
- eğer değilse False döndür.
2. kullanıcıdan bir kullanıcı adı al ve bir değişkene ata.
3. fonksiyona parametre olarak bu değişkeni ver.
4. eğer sonuç True is ekrana "Bu kullanıcı adı kullanılabilir." çıktısı ver.
5. eğer sonuç Flase is ekrana "Bu kullanıcı adı kullanılamaz." çıktısı ver. <br>
End

```
def kontrol(kelime):
  if kelime.isalnum():
    return True
  else:
    return False

kullanici_adi = input("Lütfen bir kullanıcı adı giriniz: ")
if kontrol(kelime=kullanici_adi):
  print("Bu kullanıcı adı kullanılabilir.")
else:
  print("Bu kullanıcı adı kullanılamaz.")
```

## Soru 40.2

'kullanıcıdan alınan kullanıcı adının 8 karakterden daha fazla olup ayrıca sadece harf veya rakamdan oluşup oluşmadığını kontrol eden fonksiyonla beraber programı tasarlayın.'

Adımlar:
1. 1 parametre alan bir fonksiyon tanımla.
- eğer kullanıcı adı 8 karakter veya 8 karakterden kısa ise True döndür
- eğer kullanıcı adı 8 karakterden fazla ise devam et:
- eğer kullanıcı adının içinde sadece harf veya rakam varsa True döndür.
- eğer değilse False döndür.
2. kullanıcıdan bir kullanıcı adı al ve bir değişkene ata.
3. fonksiyona parametre olarak bu değişkeni ver.
4. eğer sonuç True is ekrana "Bu kullanıcı adı kullanılabilir." çıktısı ver.
5. eğer sonuç Flase is ekrana "Bu kullanıcı adı kullanılamaz." çıktısı ver. <br>
End

```
def kontrol(kelime):
  if len(kelime) <= 8:
    return False
  else:
    if kelime.isalnum():
      return True
    else:
      return False

kullanici_adi = input("Lütfen bir kullanıcı adı giriniz: ")
if kontrol(kelime=kullanici_adi):
  print("Bu kullanıcı adı kullanılabilir.")
else:
  print("Bu kullanıcı adı kullanılamaz.")
```
