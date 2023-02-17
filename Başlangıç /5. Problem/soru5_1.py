"""
'Kullanıcıdan 2 farklı sayıp alıp bu sayılar üzerinde tüm aritmetik işlemleri yapıp ekrana gösteren programı tasarlayın.
(Toplama, Çıkarma, Bölme, Çarpma)'
"""

sayi1 = float(input("Lütfen birinci sayıyı giriniz: ")
sayi2 = float(input("Lütfen ikinci sayıyı giriniz: ")

toplam = sayi1 + sayi2
print(f"{sayi1} + {sayi2} = {toplam}")

fark = sayi1 - sayi2
print(f"{sayi1} - {sayi2} = {fark}")

bolum = sayi1 / sayi2
print(f"{sayi1} / {sayi2} = {bolum}")

carpim = sayi1 * sayi2
print(f"{sayi1} * {sayi2} = {carpim}")
