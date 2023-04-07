# Soru 69 - Başlangıç




## Soru 69.1

'kullanıcıdan alınan isimle bir .txt dosyası oluşturup bu dosyanın içine kullanıcının yaşını yazan programı tasarlayın.'

Adımlar:
1. Kullanıcıdan bir isim girdisi al ve değişkene ata.
2. with bloğu başlat
- "w" (write) yazma modunda bir dosya aç ve dosyanın ismini kullanıcının ismi yap.
- kullanıcıdan bir yaş girdisi al ve bir değişkene ata.
- dosyanın içine kullanıcının yaşını yaz.
- with bloğunu bitir. <br>
End

```
isim = input("Lütfen isminizi giriniz: "))
with open(isim, "w") as f:
  age = input("Lütfen yaşınızı giriniz: "))
  f.write(age)
```

## Soru 69.2

'kullanıcıdan alınan isimle bir .txt dosyası oluşturup bu dosyanın içine kullanıcıdan alınan 2 adet sayının toplamını yazan programı tasarlayın.'

Adımlar:
1. Kullanıcıdan bir isim girdisi al ve değişkene ata.
2. with bloğu başlat
- "w" (write) yazma modunda bir dosya aç ve dosyanın ismini kullanıcının ismi yap.
- kullanıcıdan iki adet sayı al ve değişkenlere ata.
- sayıları topla ve sonucu bir değişkene ata.
- dosyanın içine sonucu yaz.
- with bloğunu bitir. <br>
End

```
isim = input("Lütfen isminizi giriniz: "))
with open(isim, "w") as f:
  num1 = input("Lütfen ilk sayıyı giriniz: "))
  num2 = input("Lütfen ikinci sayıyı giriniz: "))
  sonuc = num1 + num2
  f.write(sonuc)
```
