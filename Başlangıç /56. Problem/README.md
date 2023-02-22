# Soru 56 - Başlangıç

## Soru 56.1

'Kullanıcıdan miktar ve alınacak yüzde(%) bilgisini alıp miktarın yüzdesini gösteren programı tasarlayın.'

Adımlar:
1. kullanıcıdan miktar bilgisini al ve bir değişkene ata.
2. kullanıcıdan yüzde bilgisini al ve bir değişkene ata.
3. miktarın yüzdesini al ve bir değişkene ata.
4. sonucu kullanıcıya göster. <br>
End

```
miktar = int(input("Lütfen miktarı giriniz: ")) # 1000
yuzde = int(input("Lütfen yüzde miktarını giriniz: ")) # 20

sonuc = (miktar*yuzde)/100
print(sonuc) # 200
```

## Soru 56.2

'Kullanıcıdan alınan onluk sayı sistemindeki(decimal) sayıyı ikili sayı sistemine(binary) çeviren programı tasarlayınız.'

Adımlar:
1. bir adet parametre alan bir fonksiyon tanımla:
- eğer sayı 1 veya 1 den den büyükse fonksiyonu fonksiyon içinde çağır ve parametre olarak: parametre // 2 ver.
- eğer sayı 1 den küçükse sayının 2 ye bölümünden kalanı yaz end parametresi yan yana olucak şekilde olsun.
2. Kullanıcıdan bir sayı al ve bir değişkene ata.
3. fonksiyona parametre olarak değişkeni ver.
4. sonucu ekrana çıktı olarak ver. <br>
End

```
def DecimalToBinary(num):
        if num >= 1:
            DecimalToBinary(num // 2)
        print(num % 2, end="")
sayi = int(input("Lütfen çevrilecek sayıyı giriniz: ")) # 15
DecimalToBinary(15) # 01111
```
