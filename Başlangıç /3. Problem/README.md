# Soru 3 - Başlangıç

## Soru 3.1

Kullanıcıdan "isim" ve "yaş" bilgisi alıp ekrana alttaki formatta gösterecek programı yazın. <br>
> Merhaba benim adım Erkam ve 27 yaşındayım.

Adımlar:
- Kullanıcıdan isim bilgisi al ve bir değişkene ata.
- Kullanıcıdan yaş bilgisi al ve bir değişkene ata.
- Merhaba benim adım <isimDeğişkeni> ve <yaşDeğişkeni> yaşındayım. Şeklinde çıktı da göster.
Bitti.

```
ad = input("Adınız: ")
yas = input("Yaşınız: ")
print(f"Merhaba benim adım {ad} ve {yas} yaşındayım.")
&
print("Merhaba benim adım {} ve {} yaşındayım.".format(ad, yas))
```

## Soru 3.2

Kullanıcıdan ders bilgisi ve not bilgisini alıp ekrana alttaki formatta gösterecek programı yazın. <br>
> Diferansiyel Denklemler dersinden tam olarak 100 aldım.

Adımlar:
- Kullanıcıdan ders bilgisi al ve bir değişkene ata.
- Kullanıcıdan not bilgisi al ve bir değişkene ata.
- <dersDeğişkeni> dersinden tam olarak <notDeğişkeni> aldım.
Bitti.

```
ders = input("Lütfen bir ders giriniz: ")
not = input("Lütfen notunuzu giriniz: ")
print(f"{} dersinden tam olarak {} aldım.")
print("{} dersinden tam olarak {} aldım.".format(ders, not))
```
