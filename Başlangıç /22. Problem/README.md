# Soru 22 - Başlangıç

## Soru 22.1

'kullanınıcın girdiği harfin sesli mi sessiz mi olduğunu söyleren programı tasarlayın.'

Adımlar:
1. sesli harflerin saklandığı bir liste oluştur.
2. kullanıcıdan bir harf al ve bir değişkene ata.
3. eğer harf bu listede varsa ekrana "<harf> harfi sesli harftir.." yaz.
4. değilse "<harf> harfi sessiz harftir.." <br>
End

```
sesli_harfler = ["a","e","ı","i","o","ö","u","ü"]
harf = input("Lütfen bir harf giriniz")
if harf in sesli_harfler:
  print(f"{harf} harfi sesli bir harftir.")
else:
  print(f"{harf} harfi sessiz bir harftir.")
```

## Soru 22.2

'kullanınıcın girdiği harfin sesli mi sessiz mi olduğunu söyleyen ayrıca eğer kullanıcı rakam girerse rakam olduğunu ve 1 haneden fazla girerse hata döndüren programı tasarlayın.'

Adımlar:
1. sesli harflerin saklandığı bir liste oluştur.
2. rakamların string şekilde saklandığı bir liste oluştur.
3. kullanıcıdan bir giriş al ve bir değişkene ata.
4. eğer karakter uzunluğu 1 se devam et, değilse hata döndür
3. eğer girdi sesli harf listesinde varsa ekrana "<harf> harfi sesli harftir.." yaz.
6. eğer girdi rakam listesinde varsa ekrana "Bu bir rakamdır." yaz.
4. eğer hiç biri değilse "<harf> harfi sessiz harftir.." <br>
End

```
sesli_harfler = ["a","e","ı","i","o","ö","u","ü"]
rakamlar = ["0","1","2","3","4","5","6","7","8","9"]
giris = input("Lütfen bir harf giriniz")
if len(giris) == 1:
  if giris in sesli_harfler:
    print(f"{giris} harfi sesli bir harftir.")
  elif giris in rakamlar:
    print("Bu bir rakamdır.")
  else:
    print(f"{giris} harfi sessiz bir harftir.")
 else:
  print("Lütfen sadece 1 karakter giriniz.")
```
