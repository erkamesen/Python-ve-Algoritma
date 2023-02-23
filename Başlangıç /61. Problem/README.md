# Soru 61 - Başlangıç


## Soru 61.1

'Kullanıcıdan alınan GB yi byte a çeviren programı tasarlayın. 1 GB = 1.073.741.824 Bayt.'


Adımlar:
1. Kullanıcıdan bir GB bilgisi al ve değişkene ata.
2. değişkeni byte a dönüştürmek için 1.073.741.824 ile çarp ve bir değişkne ata.
3. sonucu kullanıcıya göster. <br>
End

```
gb = int(input("Lütfen dönüştürmek istedğiniz GB yi giriniz: ")) # 15.5

byte = gb * 1073741824

print(f"{gb} GB = {bytes} byte")
# 15.5 GB = 16106127360 byte
```

## Soru 61.2

'Kullanıcıdan alınan byte ı GB ye çeviren programı tasarlayın. 1 GB = 1.073.741.824 Bayt.'


Adımlar:
1. Kullanıcıdan bir byte bilgisi al ve değişkene ata.
2. değişkeni GB ye dönüştürmek için 1.073.741.824 e böl ve bir değişkne ata.
3. sonucu kullanıcıya göster. <br>
End

```
byte = int(input("Lütfen dönüştürmek istedğiniz byte miktarını giriniz: ")) # 1073741824000

gb = byte / 1073741824

print(f"{byte} byte = {gb} GB")
# 1073741824000 byte = 1000.0 GB
```
