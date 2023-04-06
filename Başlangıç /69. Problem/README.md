# Soru 69 - Başlangıç

'kullanıcıdan alınan isimle bir .txt dosyası oluşturup bu dosyanın içine kullanıcının yaşını yazan programı tasarlayın.'


## Soru 69.1

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
