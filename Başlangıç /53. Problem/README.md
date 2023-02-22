# Soru 53 - Başlangıç

## Soru 53.1

'Kullanıcıdan yaşını alıp saniyeye çevirerek kullancııya gösteren programı tasarlayın.'

Adımlar:
1. Kullanıcıdan bir yaş al ve değişkene ata.
2. yaşı *360(gün)*24(saat)*60(dakika)*60(saniye) ile çarpıp saniyeye çevir ve sonucu bir değişkene ata.
3. sonucu ekrana çıktı olarak ver. <br>
End

```
yas = float(input("Lütfen yaşınızı giriniz: ")) # 27

saniye_yas = yas*360*24*60*60 
print(f"Şu zamana kadar tam olarak {saniye_yas} saniye yaşadınız.")

# Şu zamana kadar tam olarak 839808000 saniye yaşadınız.
```

## Soru 53.2

'Kullanıcıdan yaşını alıp saniyeye, dakika ve saate çevirerek kullanıcıya gösteren programı tasarlayın.'

Adımlar:
1. Kullanıcıdan bir yaş al ve değişkene ata.
2. yaşı *360(gün)*24(saat) ile çarpıp saate çevir ve sonucu bir değişkene ata.
3. yaşı *360(gün)*24(saat)*60(dakika) ile çarpıp dakikaya çevir ve sonucu bir değişkene ata.
4. yaşı *360(gün)*24(saat)*60(dakika)*60(saniye) ile çarpıp saniyeye çevir ve sonucu bir değişkene ata.
5. sonucu ekrana çıktı olarak ver. <br>
End

```
yas = float(input("Lütfen yaşınızı giriniz: ")) # 27

saat_yas = yas*360*24 # 233280
dakika_yas = yas*360*24*60 # 13996800
saniye_yas = yas*360*24*60*60 # 839808000
print(f"Şu zamana kadar tam olarak {saat_yas} saat, {dakika_yas} dakika, {saniye_yas} saniye yaşadınız.")

# Şu zamana kadar tam olarak 233280 saat, 13996800 dakika, 839808000 saniye yaşadınız.
```
