# Soru 18 - Başlangıç

## Soru 18.1

'
Kullanıcıdan ad, adres ve telefon bilgisini alıp verilen şablon sözlüğü yeni bilgilerle update eden programı yazın.
```
bilgi={"ad":"Müşterinin Adı",
       "adres":"Müşterinin Adresi",
       "telefon":"Müşterinin Telefonu"}
     
```
'

Verilenler:
```
bilgi={"ad":"Müşterinin Adı", <br>
       "adres":"Müşterinin Adresi",<br>
       "telefon":"Müşterinin Telefonu"}
       
Adımlar:
1. kullanıcıdan ad bilgisini alıp değişkene ata.
2. kullanıcıdan adres bilgisini alıp değişkene ata.
3. kullanıcıdan telefon bilgisini alıp değişkene ata.
4. sözlüğün ad, adres ve telefon değerlerini değişkenler ile güncelle.
5. ekrana sözlüğün çıktısını ver. <br>
End

```
bilgi={"ad":"Müşterinin Adı",
       "adres":"Müşterinin Adresi",
       "telefon":"Müşterinin Telefonu"}
ad = input("Lütfen adınızı giriniz: ")
adres = input("Lütfen adresinizi giriniz: ")
telefon = input("Lütfen telefonunuzu giriniz: ")
bilgi["ad"] = ad
bilgi["adres"] = adres
bilgi["telefon"] = telefon
print(bilgi)
```
## Soru 18.2

'kullanıcının adını, okul numarasını ve 3 ders bilgisi alıp dersleri liste şeklinde sözlükte saklayıp kullanıcıya gösteren programı tasarlayın.'

Adımlar:
1. Bilgileri saklamak için boş bir sözlük oluştur ve bir değişkene ata.
2. Dersler için boş bir liste oluştur ve bir değişkene ata
2. kullanıcıdan adını alıp bir değişkene ata.
3. kullancııdan okul numarasını alıp bir değişkene ata.
4. 3 adımlı bir for döngüsü oluştur.
5. her adımda kullanıcıdan bir ders alıp listeye ekle.
6. kullanıcıdan aldığın tüm bilgilerle sözlüğü oluştur.
7. kullanıcıya sözlüğü göster. <br>
End

```
bilgiler = {}
dersler = []
ad = input("Lütfen adınızı giriniz: ")
okul_numarasi = input("Lütfen okul numarasınızı giriniz: ")
for i in range(3):
  dersler.append(input("Lütfen bir ders giriniz: "))
bilgiler["Adı"] = ad
bilgiler["Okul Numarası"]
bilgiler["Alınan Dersler"] = dersler
```
