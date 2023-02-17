# Soru 4 - Başlangıç

## Soru 4.1

'
Kullanıcıdan yaş bilgisini alıp 18 yaşında veya daha büyükse "Oy kullanabilirsiniz!", eğer küçükse 18 e kalan seneyi hesaplayıp "Oy kullanamazsınız, lütfen <fark> sene bekleyiniz." çıktısı veren programı tasarlayın.'

Adımlar:
1. Kullanıcıdan yaş bilgisini alıp bir değişkene ata.
2. Eğer yaş 18 veya daha büyükse ekrana "Oy kullanabilirsiniz!" çıktısı ver.
3. Eğer yaş 18 den küçükse 18 den girilen yaş bilgisini çıkarıp bir değişkene ata.
4. Ekrana "Oy kullanamazsınız, lütfen <fark> sene bekleyiniz." çıktısını ver.
End


```
yas = int(input("Lütfen yaşınızı giriniz: "))
if yas >= 18:
  print("Oy kullanabilirsiniz!")
else:
  fark = 18 - yas
  print(f"Oy kullanamazsınız, lütfen {fark} sene bekleyiniz.")
```

## Soru 4.2

'Kullanıcıdan not bilgisini alıp not 60 veya fazla ise "Geçtiniz", eğer küçükse aldığı notun 60 ile farkını alıp ekrana "Kaldınız, <fark> puan daha lazım." 
çıktısını verecek programı tasarlayın.
'

Adımlar:
1. Kullanıcıdan not bilgisini alıp bir değişkene ata.
2. Eğer not 60 veya daha büyükse ekrana "Geçtiniz" çıktısı ver.
3. Eğer not 60 dan küçükse, 60 dan girilen not bilgisini çıkarıp bir değişkene ata.
4. Ekrana "Kaldınız, <fark> puan daha lazım." çıktısını ver.
End

```
not = int(input("Lütfen notunuzu giriniz: "))
if not >= 60:
  print("Geçtiniz")
else:
  fark = 60 - not
  print(f"Kaldınız, {fark} puan daha lazım.")
```

