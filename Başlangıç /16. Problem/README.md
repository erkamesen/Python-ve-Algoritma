# Soru 16 - Başlangıç

## Soru 16.1

'Kullanıcıdan alınan bir sayının compound(bileşik) operatörler ile işlemlerini ve sonuçlarını gösteren programı tasarlayın. <br>
(+=, -= vb.)'

Adımlar:
1. Kullanıcıdan bir sayı al
2. Alınan sayıyı bir değişkene ata
3. Compound operatörler ile işlemleri yaz.
4. sonuçları kullanıcıya göster. <br>
End

```
sayi = int(input("Lütfen bir sayı giriniz: "))
print(sayi += 5) # sayi = sayi + 5
print(sayi -= 5) # sayi = sayi - 5
print(sayi /= 5) # sayi = sayi / 5
print(sayi *= 5) # sayi = sayi * 5
print(sayi %= 5) # sayi = sayi % 5
```

## Soru 16.2

'Kullanıcıdan alınan iki sayının kendi aralarında compound(bileşik) operatörler ile işlemlerini ve sonuçlarını gösteren programı tasarlayın. <br>
(+=, -= vb.)'

Adımlar:
1. Kullanıcıdan iki adet sayı al
2. Alınan sayıları değişkenlere ata
3. Compound operatörler ile kendi aralarında işlem yap.
4. sonuçları kullanıcıya göster. <br>
End

```
sayi1 = int(input("Lütfen ilk sayı giriniz: "))
sayi2 = int(input("Lütfen ikinci sayı giriniz: "))
print(sayi1 += sayi2) # sayi1 = sayi1 + sayi2
print(sayi1 -= sayi2) # sayi1 = sayi1 - sayi2
print(sayi1 /= sayi2) # sayi1 = sayi1 / sayi2
print(sayi1 *= sayi2) # sayi1 = sayi1 * sayi2
print(sayi1 %= sayi2) # sayi1 = sayi % sayi2
```
