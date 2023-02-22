# Soru 51 - Başlangıç

## Soru 51.1

'Kullanıcıdan alınan 2 tarih arasında kaç gün olduğunu hesaplayıp kullanıcıya gösteren programı tasarlayın.'

Adımlar:
1. datetime.datetime modülünden strptime() fonksiyonunu import et
2. kullanıcıdan "dd/mm/yyyy" şeklinde ilk tarih bilgisini al ve değişkene ata.
3. kullanıcıdan "dd/mm/yyyy" şeklinde ikinci tarih bilgisini al ve değişkene ata.
4. formatı gün/ay/yıl("%d/&m/%Y") şeklinde bir değişkene ata.
5. strptime fonksiyonunun ilk parametresine tarih değişkenini ikinci parametresine formatı ver ve bir değişkene ata.
6. 4. adımın aynısını 2. değişken içinde uygula.
7. aralarındaki farkı almak için 2. tarih değişkeninden 1. tarih değişkenini çıkar ve sonucun gün kısmını değişkene ata.
8. çıkan sonucu ekrana yaz. <br>
End

```
from datetime.datetime import strptime()

tarih1 = input("Lütfen ilk tarihi giriniz: ")
tarih2 = input("Lütfen ikinci tarihi giriniz: ")

date_format = "%d/&m/%Y"
t1 = strptime(tarih1, date_format) # 25/10/1994
t2 = strptime(tarih2, date_format) # 25/10/2004
gun_farki = (t2-t1).days # 3653
print(gun_farki) 
```


## Soru 51.2

'Kullanıcıdan alınan 2 tarih arasında kaç saat olduğunu hesaplayıp kullanıcıya gösteren programı tasarlayın.'

Adımlar:
1. datetime.datetime modülünden strptime() fonksiyonunu import et
2. kullanıcıdan "dd/mm/yyyy" şeklinde ilk tarih bilgisini al ve değişkene ata.
3. kullanıcıdan "dd/mm/yyyy" şeklinde ikinci tarih bilgisini al ve değişkene ata.
4. formatı gün/ay/yıl("%d/&m/%Y") şeklinde bir değişkene ata.
5. strptime fonksiyonunun ilk parametresine tarih değişkenini ikinci parametresine formatı ver ve bir değişkene ata.
6. 4. adımın aynısını 2. değişken içinde uygula.
7. aralarındaki farkı almak için 2. tarih değişkeninden 1. tarih değişkenini çıkar ve sonucun gün kısmını değişkene ata.
8. günü saate çevir ve sonucu bir değişkene aktar.
8. çıkan sonucu ekrana yaz. <br>
End

```
from datetime.datetime import strptime()

tarih1 = input("Lütfen ilk tarihi giriniz: ") # 25/10/1994
tarih2 = input("Lütfen ikinci tarihi giriniz: ") # 25/10/2004

date_format = "%d/&m/%Y"
t1 = strptime(tarih1, date_format)
t2 = strptime(tarih2, date_format)
gun_farki = (t2-t1).days # 3653
saat_farki = gun_farki * 24 # 87672
print(saat_farki)
```
