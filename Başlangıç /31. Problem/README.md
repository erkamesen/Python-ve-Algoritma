# Soru 31 - Başlangıç

## Soru 31.1

'Kullanıcıdan alınan notun aşağıdaki verilenlere göre karşılığını kullanıcıya gösteren programı tasarlayın. <br>
eğer 89 dan büyükse "A+" <br>
eğer 79 dan büyükse "A" <br>
eğer 69 dan büyükse "B" <br>
eğer 59 dan büyükse "C" <br>
eğer 49 den büyükse "D" <br>
Eğer hiç biri değilse "F"'


Adımlar:
1. Kullanıcıdan not bilgisini alıp ir değişkene ata.
2. eğer not 89 dan büyükse ekrana "A+" çıktısını ver.
3. eğer not 79 dan büyük ve 89 dan küçükse ekrana "A" çıktısını ver.
4. eğer not 69 dan büyük ve 79 dan küçükse ekrana "B" çıktısını ver.
5. eğer not 59 dan büyük ve 69 dan küçükse ekrana "C" çıktısını ver.
6. eğer not 49 dan büyük ve 59 dan küçükse ekrana "D" çıktısını ver.
7. eğer hiç biri değilse "F" çıktısını ver. <br>
End

```
ders_notu = int(input("Lütfen notunuzu giriniz: "))
if ders_notu >= 90:
  print("A+")
elif ders_notu >= 80 and ders_notu <= 90:
  print("A")
elif ders_notu >= 70 and ders_notu <= 80:
  print("B")
elif ders_notu >= 60 and ders_notu <= 70:
  print("C")
elif ders_notu >= 50 and ders_notu <= 60:
  print("D")
else:
  print("F")
```

## Soru 31.2

'bir yönetici çalışanlarına çalıştığı yıllara göre maaşına zam yapıyor. 1 sene ve üstü çalışanlara %10, 2 sene ve üstü çalışanlara %15, 3 sene ve üstü çalışanlara %20, 5 sene ve üstü çalışanlara ise %25 zam yaptığına göre kullanıcıdan alınan yıl ve maaş bilgisine göre kullanıcıya yeni maaşını ve zam oranını gösteren programı tasarlayın.'

Adımlar:
1. Kullanıcıdan maaş bilgisi al ve değişkene ata.
2. kullanıcıdan sene bilgisi al ve değişkene ata.
3. eğer kullanıcı 1 sene ve üstüyse maaşını %10 arttır ve sonucu kullanıcıya sonucu çıktı olarak göster.
4. eğer kullanıcı 2 sene ve üstüyse maaşını %15 arttır ve sonucu kullanıcıya sonucu çıktı olarak göster.
5. eğer kullanıcı 3 sene ve üstüyse maaşını %20 arttır ve sonucu kullanıcıya sonucu çıktı olarak göster.
6. eğer kullanıcı 5 sene ve üstüyse maaşını %25 arttır ve sonucu kullanıcıya sonucu çıktı olarak göster. <br>
End

```
maas = int(input("Lütfen güncel maaşınızı giriniz: "))
yil = float(input("Lütfen kaç yıldır çalıştığınızı giriniz: "))

if yil>1 and yil<2:
  yeni_maas = maas + maas*0.1
  print(f"Yeni Maaşınız:{yeni_maas}, zam oranı: %10")
elif yil>2 and yil<3:
  yeni_maas = maas + maas*0.15
  print(f"Yeni Maaşınız:{yeni_maas}, zam oranı: %15")
elif yil>3 and yil<5:
  yeni_maas = maas + maas*0.2
  print(f"Yeni Maaşınız:{yeni_maas}, zam oranı: %20")
elif yil>5:
  yeni_maas = maas + maas*0.25
  print(f"Yeni Maaşınız:{yeni_maas}, zam oranı: %25")
```


