# Soru 24 - Başlangıç


## Soru24.1

'Kullanıcıdan 2 adet sayı ve bir adet operatör(+, -, *, /) alıp operatöre göre 2 sayı arasında işlem yapan programı tasarlayın.'

Adımlar:
1. Kullanıcıdan 2 adet sayı alıp değişkenlere ata.
2. kullanıcıya yapacağı işlemi sorup operatörü al ve bir değişkene ata.
3. eğer operatör + ise sayıları topla ve sonucu ekrana yaz.
4. eğer operatör - ise sayıları çıkar ve sonucu ekrana yaz.
5. eğer operatör * ise sayıları çarp ve sonucu ekrana yaz.
6. eğer operatör / ise sayıları böl ve sonucu ekrana yaz. <br>
End

```
num1 = int(input("Lütfen ilk sayıyı giriniz: "))
num2 = int(input("Lütfen ikinci sayıyı giriniz: "))
islem = input("Lütfen yapacağınız işlemi giriniz(+, -, *, /): )
if islem == "+":
  print(num1+num2)
elif islem == "-":
  print(num1-num2)
elif islem == "*":
  print(num1*num2)
elif islem == "/":
  print(num1/num2)
```
## Soru 24.2

'Kullanıcıdan alınan 2 si sayı biri operatör parametresine göre 2 sayı arasında işlem yapan fonksiyonu yazın ve programı tasarlayın.'

Adımlar:
1. 3 adet parametre alan fonksiyonu oluştur.
2. eğer 3. parametre + ise ilk 2 parametreyi topla ve sonucu döndür.
3. eğer 3. parametre - ise ilk 2 parametreyi çıkar ve sonucu döndür.
4. eğer 3. parametre * ise ilk 2 parametreyi çarp ve sonucu döndür.
5. eğer 3. parametre / ise ilk 2 parametreyi böl ve sonucu döndür.
6. fonksiyonu bitir.
8. Kullanıcıdan 2 adet sayı alıp değişkenlere ata.
9. kullanıcıya yapacağı işlemi sorup operatörü al ve bir değişkene ata.
10. fonksiyonu çağır ilk 2 parametreye sayı değişkenleri, son parametreye operatör değişkenini ver.
11. sonucu ekrana yaz. <br>
End

```
def hesap(n1, n2, islem)
  if islem == "+":
    return n1+n2
  elif islem == "-":
    return n1-n2
  elif islem == "*":
    return num1*num2
  elif islem == "/":
    return num1/num2
    
num1 = int(input("Lütfen ilk sayıyı giriniz: "))
num2 = int(input("Lütfen ikinci sayıyı giriniz: "))
islem = input("Lütfen yapacağınız işlemi giriniz(+, -, *, /): )
hesap(n1=num1, n2=num2, islem=islem)
```
