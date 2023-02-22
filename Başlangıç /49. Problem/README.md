# Soru 49 - Başlangıç


## Soru 49.1
'Kullanıcıdan alınan saati saniyeye çeviren programı tasarlayın.'

Adımlar:
1. Kullanıcıdan bir saat bilgisi al ve bir değişkene ata.
2. değişkeni 3600 ile çarpıp saati saniyeye çevir.
3. sonucu ekrana çıktı olarak ver. <br>
End

```
saat = float(input("Lütfen çevirmek istediğiniz saati giriniz: ")) # 3.5
saniye = saat*3600
print(f"{saat} saat tam olarak {saniye} sn ediyor.") # 12600.0
```


## Soru 49.2
'Kullanıcıdan alınan saniyeyi saate çeviren programı tasarlayın.'

Adımlar:
1. Kullanıcıdan bir saniye bilgisi al ve bir değişkene ata.
2. değişkeni 3600 ile bölüp saniyeyi saate çevir.
3. sonucu ekrana çıktı olarak ver. <br>
End

```
saniye = float(input("Lütfen çevirmek istediğiniz saniyeyi giriniz: ")) # 452322
saat = saniye/3600
print(f"{saniye} sn tam olarak {saat} saat ediyor.") # 1256.45
```
