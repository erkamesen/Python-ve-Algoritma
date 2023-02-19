# Soru 27 - Başlangıç


## Soru 27.1

'Basit bir artık yıl uygulaması için kullanıcıdan alınan yılın artık yıl olup olmama durumunu sadece 4 e bölünebilen cinsten tasarlayın.'

Adımlar:
1. Kullanıcıdan bir yıl girişi alın ve değişkene atayın.
2. eğer yıl 4 e tam bölünebiliyorsa yıl artık yıldır.
3. sonucu çıktıyı ver.
4. eğer yıl 4 e tam bölünemiyorsa yıl artık yıl değildir.
5. sonucu çıktıya ver. <br>
End

```
year = int(input("Lütfen yılı giriniz: "))
if year %4 == 0:
  print("Artık yıl.")
else:
  print("Artık yıl değil.")
```

## Soru 27.2

'kullanıcıdan alınan 5 adet sayıyı bir array de saklayıp ardından kullanıcıya sadece artık yılları(sadece 4 e bölünebilmesi yeterli) gösteren programı tasarlayın.'

Adımlar:
1. array modülünü arr ismi ile import et
2. artık yılı kontrol etmek için yıl parametresi alan bir fonksiyon oluştur.
- eğer yıl 4 e tam bölünebiliyorsa yıl artık yıldır.
- sonucu True döndür
- eğer yıl 4 e tam bölünemiyorsa yıl artık yıl değildir.
- sonucu False döndür
3. arr nesnesinin array methodu ile bir array oluştur ve değişkene ata.
4. 5 adımlı bir for döngüsü başlat.
5. her adımda kullanıcıdan bir sayı alıp array e ekle.
6. döngüyü bitir.
7. 5 adımlı bir döngü başlat.
8. fonksiyonu çağır
9. her adımda arrayi indexle ve indexlenen değeri fonksiyona parametre olarak ver.
10. eğer True dönerse "<yıl> Artık Yıldır." sonucunu ekrana yaz.
11. eğer False dönerse "<yıl> Artık Yıl Değildir." sonucunu ekrana yaz. <br>
End

```
import array as arr

def artik_yil(year):
  if year %4 == 0:
    return True
  else:
    return False

a = arr.array("i", [])
for i in range(5):
  a.append(int(input("Lütfen bir yıl giriniz: "))

for i in range(5):
  yil = a[i]
  if artik_yil(year=yil):
    print(f"{yıl} Artık Yıldır.")
  else:
    print(f"{yıl} Artık Yıl Değildir.")

```
