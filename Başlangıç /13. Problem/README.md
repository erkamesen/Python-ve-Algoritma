# Soru 13 - Başlangıç

## Soru 13.1

'Kullanıcıdan bir parola alıp parolanın harf veya rakam içeriyorsa kabul eden aksi halde hata veren programı tasarlayın. <br>
Eğer koşullar sağlanıyorsa "şifreniz ****** kabul edilmiştir" şeklinde şifreyi gizleyerek ekrana çıktı verin.'

Adımlar:
1. Kullanıcıdan bir parola girdisi al ve bir değişkene ata.
2. parolayı harf veya rakam içeriyor mu diye kontrol et.
3. eğer parola harf veya rakam içermiyorsa hata döndür.
4. eğer parola harf veya rakam içeriyorsa ekrana parolanın uzunluğu kadar "*" karakteri ile belirt. <br>
End

```
parola = input("Lütfen bir parola giriniz: ")
if parola.isalnum():
  print(f"Parolanız {len(parola)*'*'} başarılı şekilde oluşturuldu.")
else:
  print("Lütfen parolanızın içinde sadece harf veya rakam olsun.")
```

## Soru 13.2


'Kullanıcıdan bir parola alıp parolanın harf veya rakam içeriyorsa ayrıca parola 8 haeye eşit veya daha büyükse kabul eden aksi halde hata veren programı tasarlayın. <br>
Eğer koşullar sağlanıyorsa "şifreniz ****** kabul edilmiştir" şeklinde şifreyi gizleyerek ekrana çıktı verin.'

Adımlar:
1. Kullanıcıdan bir parola girdisi al ve bir değişkene ata
2. parolanın uzunluğunu al ve bir değişkene ata
3. parolanın uzunluğunu kontrol et.
4. eğer parola 8 haneden küçükse hata döndür.
5. eğer parola 8 veya daha büyük haneye sahipse 5. adıma git.
6. eğer parola harf veya rakam içermiyorsa hata döndür.
7. eğer parola harf veya rakam içeriyorsa ekrana parolanın uzunluğu kadar "*" karakteri ile belirt. <br>
End

```
parola = input("Lütfen parolanızı giriniz: ")
parola_uzunlugu = len(parola)
if parola_uzunlugu < 8:
  print("Lütfen 8 veya daha fazla haneli bir parola oluşturun.")
else:
  if parola.isalnum():
  print(f"Parolanız {parola_uzunlugu*'*'} başarılı şekilde oluşturuldu.")
else:
  print("Lütfen parolanızın içinde sadece harf veya rakam olsun.")
  
```
