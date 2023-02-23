# Soru 62 - Başlangıç


## Soru 62.1

'Kullanıcıdan aldığı isim, babasının ismi, yaş ve telefon bilgileri ile aşağıdaki tabloyu oluşturan programı tasarlayın.
```
Adı:           ...
Baba Adı:      ...
Yaş:           ...
Telefon:       ...
```
(2 alan arasında ilk alandaki yazılar dahil toplam 15 karakter uzunlukta boşluk var.)' <br>

Adımlar:
1. Kullanıcıdan bilgileri alıp değişkenlere ata.
2. tabloyu oluştur ve kullanıcıya göster. <br>
End

```
ad = input("Adınız: ") # Erkam
baba_adi = input("Babanızın Adı: ") # Muzaffer
yas = input("Yaşınız: ") # 27
telefon = input("Telefon Numarası: ") # 123123123

print("Adı:"+11*" "+ad+"\nBaba Adı:"+6*" "+baba_adi+"\nYaş:"+11*" "+yas+"\nTelefon:"+7*" "+telefon)
"""
Adı:           Erkam
Baba Adı:      Muzaffer
Yaş:           27
Telefon:       123123123
"""
```

## Soru 62.2

'Kullanıcıdan giriş için alınan kullanıcı adı ve parola kısmında eğer kullanıcı adı ve parola aşağıda verilen bilgiler ile aynı ise "Giriş Başarılı" çıktısı veren, eğer kullanıcı adı doğru şifre yanlış ise "Lütfen Şifrenizi Kontrol Ediniz!" yada tam tersi kullanıcı adı yanlış ise "Böyle Bir Kullanıcı Bulunamadı!" çıktısı veren programı tasarlayın.
```
kullanıcı adı: denemekullanici
sifre: 123123123abc
```
' <br>
Adımlar:
1. Kullanıcıdan kullanıcı adı ve şifre bilgisi alıp değişkenlere ata.
2. eğer kullanıcı adı ve şifre verilenle aynı ise başarılı çıktısı ver.
3. eğer kullanıcı ad yanlış ise kullanıcı bulunamadı çıktısı ver.
4. eğer şifre yanlış ise lütfen şifrenizi kontrol edin çıktısı ver. <br>
End

```

kullanici_adi = input("Lütfen kullanıcı adını giriniz: ")
parola = input("Lütfen şifrenizi giriniz: ")

if kullanici_adi == "denemekullanici" and parola == "123123123abc":
  print("Giriş Başarılı")
elif kullanici_adi != "denemekullanici":
  print("Böyle Bir Kullanıcı Bulunamadı!")
elif parola != "123123123abc":
  print("Lütfen Şifrenizi Kontrol Ediniz!")
```
