# Soru 2 - Başlangıç

## Soru 2.1

Kullanıcıdan alınan yarıçap ile dairenin alanını bulan programı yazın. (πr²) <br>
Verilenler: 
- π = 3.14 

Adımlar:
1. Kullanıcıdan yarıçapı al ve bir değişkene ata
2. Dairenin alanını bulmak için değişkeni(yarıçapı) formülde yerine koy
3. Sonucu bir değişkene ata
4. Sonucu göster
Bitir

```
radius = float(input("Yarıçap :"))
dairenin_alani = 3.14*radius**2
print(dairenin_alani)
```

## Soru 2.2

Kullanıcıdan alınan kısa kenar ve uzun kenar ile dikdörtgenin alanını hesaplayan programı yazın. (A*B)

Adımlar:
1. Kullanıcıdan kısa kenarı al ve bir değişkene ata
2. Kullanıcıdan uzun kenarı al ve bir değişkene ata
3. Değişkenleri formülde yerine koy ve sonucu bir değişkene ata
4. Sonucu göster
Bitir

```
kisa_kenar = float(input("Lütfen kısa kenarın uzunluğunu giriniz: ")
uzun_kenar = float(input("Lütfen uzun kenarın uzunluğunu giriniz: ")
dikdortgen_alan = kisa_kenar * uzun_kenar
print(dikdortgen_alan)
```
