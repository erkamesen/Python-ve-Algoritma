# Soru 11 - Başlangıç

## Soru 11.1

'Kullanıcıdan 2 adet sayı alıp yüksek olan sayıyı kullanıcıya gösteren programı tasarlayın.(eğer sayılar eşitse "Sayılar Eşit!" yazsın.)'

Adımlar:
1. kullanıcıdan 2 adet sayı al ve değişkenlere ata.
2. eğer birinci sayı ikinci sayıdan büyükse ekrana birinci sayıyı yaz.
3. eğer ikinci sayı birinci sayıdan büyükse ekrana ikinci sayıyı yaz.
4. 2 koşul da sağlanmıyorsa ekrana "Sayılar Eşit!" yaz. <br>
End

```
sayi1 = int(input("Lütfen birinci sayıyı giriniz: ")
sayi2 = int(input("Lütfen ikinci sayıyı giriniz: ")
if sayi1>sayi2:
  print(f"{sayi1} daha büyük.")
elif sayi2>sayi1:
  print(f"{sayi1} daha büyük.")
else:
  print("Sayılar Eşit!)
```
Alternatif: <br>
Adımlar:
1. kullanıcıdan 2 adet sayı al ve değişkenlere ata.
2. max() fonksiyonuna iki değişkeni parametre olarak ver.
3. çıkan sonucu ekrana yaz. <br>
End
```
sayi1 = int(input("Lütfen birinci sayıyı giriniz: ")
sayi2 = int(input("Lütfen ikinci sayıyı giriniz: ")
buyuk_sayi = max(sayi1, sayi2)
print(f"{buyuk_sayi} daha büyük.")
```
## Soru 11.2

'Kullanıcıdan 3 adet sayı alıp yüksek olan sayıyı kullanıcıya gösteren programı tasarlayın.(eğer sayılar eşitse "Sayılar Eşit!" yazsın.)'


Adımlar:
1. kullanıcıdan 3 adet sayı al ve değişkenlere ata.
2. eğer birinci sayı ikinci sayı ve üçüncü sayıdan büyükse ekrana birinci sayıyı yaz.
3. eğer ikinci sayı birinci sayıdan ve üçüncü sayıdan büyükse ekrana ikinci sayıyı yaz.
4. eğer üçüncü sayı birinci sayıdan ve ikinci sayıdan büyükse ekrana üçüncü sayıyı yaz.
5. 3 koşul da sağlanmıyorsa ekrana "Sayılar Eşit!" yaz. <br>
End
```
sayi1 = int(input("Lütfen birinci sayıyı giriniz: ")
sayi2 = int(input("Lütfen ikinci sayıyı giriniz: ")
sayi3 = int(input("Lütfen üçüncü sayıyı giriniz: ")
if sayi1>sayi2 and sayi1>sayi3:
  print(f"en büyük sayı {sayi1}.")
elif sayi2>sayi1 and sayi2>sayi3:
  print(f"en büyük sayı {sayi2}.")
elif sayi3>sayi2 and sayi3>sayi1:
  print(f"en büyük sayı {sayi3}.")
else:
  print("Sayılar Eşit!")
```

Alternatif: <br>
Adımlar:
1. kullanıcıdan 3 adet sayı al ve değişkenlere ata.
2. max() fonksiyonuna üç değişkeni parametre olarak ver.
3. çıkan sonucu ekrana yaz. <br>
End
```
sayi1 = int(input("Lütfen birinci sayıyı giriniz: ")
sayi2 = int(input("Lütfen ikinci sayıyı giriniz: ")
sayi3 = int(input("Lütfen üçüncü sayıyı giriniz: ")
buyuk_sayi = max(sayi1, sayi2, sayi3)
print(f"en büyük sayi {buyuk_sayi}.")
```


