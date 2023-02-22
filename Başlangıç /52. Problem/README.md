# Soru 52 - Başlangıç


## Soru 52.1

'Kullanıcıdan alınan cümleyi ters çevirip kullanıcıya gösteren programı tasarlayın.'

Adımlar:
1. Kullanıcıdan bir cümle al ve bir değişkene ata.
2. cümleyi ters çevir ve sonucu bir değişkene ata.
3. sonucu ekrana yaz. <br>
End

```
cumle = input("Lütfen çevirme kiçin bir cümle giriniz: ") # Python yüksek seviye ve nesne yöenlimli bir dildir.
ters_cumle = cumle[::-1]

print(ters_cumle) 

# .ridlid rib ilmilneöy ensen ev eyives kesküy nohtyP
```

## Soru 52.2

'Kullanıcıdan alınan cümleyi ters çevirip başına ve sonuna çift tırnak ekleyip kullanıcıya gösteren programı tasarlayın.'

Adımlar:
1. Kullanıcıdan bir cümle al ve bir değişkene ata.
2. cümleyi ters çevir ve sonucu bir değişkene ata.
3. cümlenin başına ve sonuna çift tırnak ekleyerek değişkeni güncelle.
3. sonucu ekrana yaz. <br>
End

```
cumle = input("Lütfen çevirme kiçin bir cümle giriniz: ") # Python yüksek seviye ve nesne yöenlimli bir dildir.
ters_cumle = cumle[::-1]
ters_cumle = '"'+ters_cumle+'"'
print(ters_cumle) 

# ".ridlid rib ilmilneöy ensen ev eyives kesküy nohtyP"
```
