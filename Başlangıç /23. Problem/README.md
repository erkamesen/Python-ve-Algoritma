# Soru 23 - Başlangıç



## Soru 23.1

'Kullanıcıdan bir gün bilgisi alıp eğer gün cumartesi yada pazar ise ekrana "Bugün tatil!" yazan programı tasarlayın.'

Adımlar:
1. Kullanıcıdan bir gün bilgisi al ve bir değişkene tüm harflerini küçülterek ata.
2. eğer değişkenin değeri "cumartesi" yada "pazar" a eşitse ekrana "Bugün tatil!" çıktısı ver.
3. eğer değilse ekran "Haydi işe!" yaz. <br>
End

 ```
gun = input("Lütfen bulunduğunuz günü girin: ").lower()
 if gun == "cumartesi" or gun == "pazar":
   print("Bugün tatil!")
else:
  print("Haydi işe!")
 ```
 
## Soru 23.2
 
'Kullanıcıdan bir gün bilgisi alıp hafta içi mi hafta sonu mu olduğunu ekrana çıktı olarak yazan programı tasarlayın. Eğer 7 günden farklı bir şey yazarsa program hata versin.'

Adımlar:
1. içinde hafta içine ait günlerin büyük harfler ile saklandığı bir liste oluştur.
2. içinde hafta sonuna ait günlerin büyük harfler ile saklandığı bir liste oluştur.
3. kullanıcıdan bir gün bilgisi al ve tüm harfleri büyük yapıp bir değişkene ata.
4. eğer değişken hafta içi listesinde varsa ekrana "Bugün hafta içi" çıktısı ver.
5. eğer değişken hafta sonu listesinde varsa ekrana "Bugün hafta sonu" çıktısı ver.
6. eğer değişken 2 listede de yoksa ekrana "Bu bir gün değil" çıktısı ver. <br>
End

```
hafta_ici = ["PAZARTESİ","SALI","ÇARŞAMBA","PERŞEMBE","CUMA"]
hafta_sonu = ["CUMARTESİ","PAZAR"]

gun = input("Lütfen bulunduğunuz günü girin: ").upper()

if gun in hafta_ici:
  print("Bugün hafta içi")
elif gun in hafta_sonu:
  print("Bugün hafta sonu")
else:
  print("Bu bir gün değil")
```
