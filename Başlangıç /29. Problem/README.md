# Soru 29 - Başlangıç


## Soru 29.1

'Kullanıcıdan alınan sayının negatif mi pozitif mi olduğunu kontrol eden programı tasarlayın.'

Adımlar:
1. Kullanıcıdan bir sayı al
2. sayıyı bir değişkene ata.
3. eğer sayı 0 dan küçükse "Negatif" çıktısını ekrana ver.
4. eğer sayı 0 dan büyükse "Pozitif" çıktısını ekrana ver. <br>
End

```
sayi = int(input("Lütfen kontrol edilecek sayıyı giriniz: ")
if sayi < 0:
  print(f"{sayi} Negatif")
elif sayi > 0:
  print(f"{sayi} Pozitif")
```

## Soru 29.2

'Kullanıcıdan alınan sayının negatif mi pozitif mi yada sıfır mı olduğunu kontrol eden programı tasarlayın.'

Adımlar:
1. Kullanıcıdan bir sayı al
2. sayıyı bir değişkene ata.
3. eğer sayı 0 dan küçükse "Negatif" çıktısını ekrana ver.
4. eğer sayı 0 sa "Sıfır" çıktısını ekrana ver.
4. eğer sayı 0 dan büyükse "Pozitif" çıktısını ekrana ver. <br>
End

```
sayi = int(input("Lütfen kontrol edilecek sayıyı giriniz: ")
if sayi < 0:
  print(f"{sayi} Negatif")
elif sayi == 0:
  print(f"{sayi} Sıfır")
else:
  print(f"{sayi} Pozitif")
```
