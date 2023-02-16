# Python-ve-Algoritma

<div style="width:100%;height:0;padding-bottom:43%;position:relative;">
<img src="https://media.giphy.com/media/eChf44Gyj2VrO/giphy.gif">
</div>

# İçerik:
### Algoritma
1. [Algoritma](https://github.com/erkamesen/Python-ve-Algoritma#algoritma-1) <br>
1.1. [Algoritma Nedir ?](https://github.com/erkamesen/Python-ve-Algoritma#algoritma-nedir-) <br>
2. [Akış Diyagramları](https://github.com/erkamesen/Python-ve-Algoritma#ak%C4%B1%C5%9F-diyagramlar%C4%B1)
3. [Operatörler](https://github.com/erkamesen/Python-ve-Algoritma#operat%C3%B6rler) <br>
3.1. [İşlem Operatörleri](https://github.com/erkamesen/Python-ve-Algoritma#i%CC%87%C5%9Flem-operat%C3%B6rleri) <br>
3.1.1 [İşlem Önceliği](https://github.com/erkamesen/Python-ve-Algoritma#i%CC%87%C5%9Flem-%C3%B6nceli%C4%9Fi) <br>
3.2 [Karşılaştırma Operatörleri](https://github.com/erkamesen/Python-ve-Algoritma#kar%C5%9F%C4%B1la%C5%9Ft%C4%B1rma-operat%C3%B6rleri) <br>
3.3 [Mantıksal Operatörler](https://github.com/erkamesen/Python-ve-Algoritma#mant%C4%B1ksal-operat%C3%B6rler)
### Python
1. [Python](https://github.com/erkamesen/Python-ve-Algoritma#python-1)
2. [Temel Veri Tipleri](https://github.com/erkamesen/Python-ve-Algoritma#temel-veri-tipleri)
3. [Container Veri Tipleri](https://github.com/erkamesen/Python-ve-Algoritma#container-veri-tipleri) <br>
3.1 [Sıralı Diziler](https://github.com/erkamesen/Python-ve-Algoritma#s%C4%B1ral%C4%B1-diziler) <br>
3.1 [Key Containers](https://github.com/erkamesen/Python-ve-Algoritma#key-containers) <br>
4. [Değişken Tanımlama](https://github.com/erkamesen/Python-ve-Algoritma#de%C4%9Fi%C5%9Fken-tan%C4%B1mlama) 
# Algoritma
## Algoritma Nedir ?

Problemlerin çözümünün mantıksal sıralamasıdır.Günlük hayatta yapacağımız işler için hazırladığımız planlar aslında algoritmanın günlük hayatta kullanıldığının ispatıdır.Tüm programlama dillerinin temeli algoritmadır. <br>
Önemli algoritma türleri: 
- Arama algoritmaları
- Bellek yönetimi algoritmaları
- Bilgisayar grafiği algoritmaları
- Birleşimsel algoritmalar
- Genetik algoritmalar
- Optimizasyon algoritmaları vb.



## Akış Diyagramları 

Algoritmanın belirli semboller yardımı ile görsel bir şekilde oluşturulmasında yardımcı olur. Programlamaya başlarken planlı hareket etmek ve uygulamanın karanlık yollarında kaybolmamak için önemlidir

<img src="https://user-images.githubusercontent.com/120065120/219083131-e7772ee6-5b96-4df3-adb2-9716348446c0.png" width=500px alt="Akış Diyagramı">

## Operatörler

### İşlem Operatörleri

- Toplama operatörü: **+ (artı)**
- Çarpma operatörü: **\* (yıldız)**
- Çıkarma operatörü: **– (eksi)** 
- Bölme operatörü: **/ (slash)** 
- Üs alma operatörü: **^ (caret)** 
- Mod operatörü: **% (yüzde)** 

#### İşlem Önceliği
1) Parantez içleri
2) Üs alma işlemleri
3) Çarpma ve bölme işlemleri
4) Toplama ve çıkarma işlemleri

### Karşılaştırma Operatörleri

- Eşit mi operatörü: **==** simgesi ile ifade edilir.
- Eşit değil mi operatörü: **!=** simgesi ile ifade edilir.
- Küçüktür operatörü: **<** simgesi ile ifade edilir.
- Büyüktür operatörü: **>** simgesi ile ifade edilir.
- Küçük veya eşittir operatörü: **<=** simgesi ile ifade edilir.
- Büyük veya eşittir operatörü: **>=** simgesi ile ifade edilir.

### Mantıksal Operatörler

- Ve(and) operatörü && simgesi ile ifade edilir.
- Veya(or) operatörü II simgesi ile ifade edilir.
- Değil (not) operatörü ! simgesi ile ifade edilir.

# Python
## Temel Veri Tipleri

integer, float, boolean, string, bytes 

- int: 783, 0, -192, 0b019(binary), 0o0642(octal), 0xF3(hexa)
- float: 9.23, 0.0, -1.7e-6
- bool: True, False
- str: "DörtBeş", "21", "Ben\nErkam"
- bytes: b"toto\xfe\775"

☝️☝️ immutables

## Container Veri Tipleri
### Sıralı Diziler
hızlı index erişimi ve tekrarlanabilir değer
- list: [7, 8, 3, 4], ["z", 5, 0.3], ["eko"] [] -> Mutable
- tuple: (7, 8, 3, 4), 5, 0.3, "z", ("eko",) () -> Immutable
- str bytes: b"" -> Immutable
### Key Containers
Hızlı anahtar erişimi ve her anahtar unique
- dictionary -> dict {"key":"value"} dict(a=2, b=0.3, c="sa") {}
- collection -> set {"key1", "key2"} {1, 9, 3, 0} set() 

## Değişken Tanımlama

Python programlarımızda bellekte geçici olarak veri saklamak için oluşturduğumuz alanlara değişken denir.Eşitliğin sağ tarafı değerimizi
sol tarafı ise değişkenimizin adını gösterir.

x=2 <br>
\# 2 -> integer

a=b=c=0 -> 3 Farklı değşkene aynı değeri atamak <br>
\# 0 -> integer

y, z, r=0.2, -7.6, 0 - Çoklu değişken atama
\# y=0.2, z=-7.6, r=0 

a, b=b, a değişken swap leme

- - - 
Dizi Açılımı
a, *b = seq <br>
*a , b = seq

```
a, *b = ["a", 2, True, 3.2, "c"]
# a = "a"
# b = [2, True, 3.2, 'c']
```
```
*a, b = ["a", 2, True, 3.2, "c"]
# a = ['a', 2, True, 3.2]
# b = "c"
```

x += 1 <-> x = x + 1 <br>
x -= 2 <-> x = x - 2 <br>
x *= 3 <-> x = x * 3 <br>
x /= 4 <-> x = x / 4 <br>
x %= 5 <-> x = x % 5 <br>
<br>

x = None  -> undefined

del x -> Değişkeni silme








