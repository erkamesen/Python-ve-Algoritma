# Soru 65 - Başlangıç


## Soru 65.1

'Kullanıcıdan alınan bilgilere göre karenin alanını ve çevresini bulan fonksiyonları ve programı tasarlayın.A=a²P=4a'

Adımlar:
1. Alanı bulmak için bir parametre alan bir fonksiyon tanımla.
- parametrenin karesini al ve sonucu bir değişkene ata.
- sonucu döndür.
2. Çevreyi bulmak için bir parametre alan bir fonksiyon tanımla.
- parametreyi 4 ile çarp ve sonucu bir değişkee ata.
- sonucu döndür.
3. Kullanıcıdan bir kenar uzunluğu al ve bir değişkene ata.
4. Değişkeni alan fonksiyonuna parametre olarak ver ve sonucu ekrana yaz.
5. Değişkeni çevre fonksiyonuna parametre olarak ver ve sonucu ekrana yaz. <br>
End.

```
def alan_bul(kenar):
  sonuc = kenar**2
  return sonuc
  
def cevre_bul(kenar):
  sonuc = kenar*4
  return sonuc
  
kenar_uzunlugu = int(input("Lütfen bir kenar uzunluğunu giriniz: ")) # 5

print("Alan:",alan_bul(kenar_uzunlugu)) # 25
print("Çevre:",cevre_bul(kenar_uzunlugu)) # 20
```

## Soru 65.2
'Kullanıcıdan alınan kare alanı bilgisine göre kullanıcıya karenin çevresini çıktı olarak veren fonksiyonla programı tasarlayın.A=a²P=4a'

Adımlar:
1. Bir parametre alan bir fonksiyon tanımla:
- Parametrenin karekökünü al ve bir değişkene ata.
- Değişkeni 4 ile çarp ve sonucu bir değişkene ata.
- Sonucu döndür
2. Kullanıcıdan karenin alanını al ve bir değişkene ata.
3. Değişkeni fonksiyona parametre olarak ver ve sonucu bir dğeişkene ata.
4. Sonucu ekrana çıktı olarak ver. <br>
End.

```
def alandan_cevreye(alan):
  kenar_uzunlugu = alan**0.5
  cevre = kenar_uzunlugu *4
  return cevre
  
alan = int(input("Lütfen karenin alanını giriniz: ")) # 9

cevre = alandan_cevreye(alan)
print("Çevre:",cevre) # Çevre: 12.0
```
