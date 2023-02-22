# Soru 48 - Başlangıç


## Soru 48.1

'Kullanıcıdan 2 sayı alıp bir değişkene atayan ve ardından bu değişkenlerin değerini hazfıza değeri yardımı ile birbiri arasında değiştiren programı tasarlayın.'

Adımlar:
1. Kullanıcıdan 2 adet sayı al ve değişkenlere ata.
2. sayıları kullanıcıya göster.
2. birinci sayının değerini yeni bir hafıza değişkeni oluşturup ona ata.
3. ikinci sayının değerini birinci sayıya ata.
4. hafıza değişkeninin değerini ikinci sayıya ata.
5. sonuçları yazdır. <br>
End


```
a = int(input("Lütfen ilk sayıyı giriniz: ")) # 3
b = int(input("Lütfen ikinci sayıyı gitiniz: ")) # 5
Print(f"Birinci sayı: {a}\nİkinci sayı: {b}")

c = a # c = 3
a = b # a = 5
b = c # b = 3 

Print(f"Birinci sayı: {b}\nİkinci sayı: {a}")
```

## Soru 48.2

'Kullanıcıdan 2 sayı alıp bir değişkene atayan ve ardından bu değişkenlerin değerini hazıfa değeri olmadan birbiri ile değiştiren programı tasarlayın.'

Adımlar:
1. Kullanıcıdan 2 adet sayı al ve değişkenlere ata.
2. sayıları kullanıcıya göster.
3. birinci sayının değerini ikinci sayı, ikinci sayının değerini birinci sayıya ata.
4. sonuçları yazdır. <br>
End


```
a = int(input("Lütfen ilk sayıyı giriniz: ")) # 6
b = int(input("Lütfen ikinci sayıyı gitiniz: ")) # 7
Print(f"Birinci sayı: {a}\nİkinci sayı: {b}")

a, b = b, a

Print(f"Birinci sayı: {b}\nİkinci sayı: {a}")
```
