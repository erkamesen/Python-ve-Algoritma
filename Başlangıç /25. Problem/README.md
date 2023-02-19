# Soru 25 - Başlangıç

## Soru 25.1

'Kullanıcıdan notunu alıp eğer not 50 den düşükse "Kaldın", fazla ise "Geçtin" yazan programı tasarlayın.'

Adımlar:
1. Kullanıcıdan not bilgisi al ve bir değişkene ata.
2. eğer not 50 veya daha fazla ise ekrana "Geçtin" çıktısı ver.
3. değilse ekrana "Kaldın" çıktısı ver. <br>
End

```
not = int(input("Lütfen notunuzu giriniz: "))
if not >= 50:
  print("Geçtin")
else:
  print("Kaldın")
```

## Soru 25.1

'Kullanıcıya öğrenci olup olmadığını sorup eğer öğretmense alttaki not listesini gösteren eğer öğrenciyse "Not sistemimize hoşgeldiniz" yazan programı tasarlayın. <br>
not_listesi = [("ahmet", 44), ("ali", 20), ("erkam", 100)]'

Adımlar:
1. Kullanıcıdan meslek bilgisi al ve bir değişkene ata.
2. eğer mesleği öğretmense for döngüsü ile not_liestesini yan yana yazdır.
3. değilse ekrana "Not sistemimize hoşgeldiniz" çıktısı ver. <br>
End

```
meslek = input("Lütfen mesleğinizi giriniz: ").lower()
if meslek == "öğretmen":
  for not in not_listesi:
    print(not, end=" ")
else:
  print("Not sistemimize hoşgeldiniz")
```
