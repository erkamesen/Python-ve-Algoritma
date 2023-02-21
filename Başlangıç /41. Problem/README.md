# Soru 41 - Başlangıç


## Soru 41.1

'Kullanıcıdan alınan açının sin ve cos değerlerini bulan programı tasarlayın.'


Adımlar:
1. math kütüphanesinden sin ve cos fonksiyonlarını import et.
2. kullanıcıdan bir sayı al ve değişkene ata.
3. alınan açıyı sin() fonksiyonuna parametre olarak ver ve sonucu bir değişkene ata.
4. alınan açıyı cos() fonksiyonuna parametre olarak ver ve sonucu bir değişkene ata.
5. değişkenleri çıktı olarak göster. <br>

```
from math import sin, cos

aci = float(input("Lütfen dönüştürmek üzere bir açı giriniz: "))

sin_aci = sin(aci)
cos_aci = cos(aci)
print(f"sin değeri: {sin_aci}\ncos değeri: {cos_aci}")
```

## Soru 41.2

'Kullanıcıdan alınan 2 kenar ile dik üçgenin uzunluğunu bulan programı tasarlayın.'

Adımlar:
1. Kullanıcıdan 2 adet sayı al ve değişkenlere ata.
2. değişkenleri "h2 = b² + c²" formülünde b ve c yerine koy.
3. sonucu ekrana yaz. <br>
End

```
# h² = b² + c² => h = (b**2+c**2)**0.5
b = float(input("Lütfen bir kenarı giriniz: "))
c = float(input("Lütfen bir kenarı giriniz: "))
h = (b**2+c**2)**0.5
print(h)
```
