"""
'Kullanıcıdan 2 adet sayı alıp sayıların karelerinin toplamını kullanıcıya gösteren programı tasarlayın.'
"""


sayi1 = int(input("Lütfen ilk sayıyı giriniz: "))
sayi2 = int(input("Lütfen ikinci sayıyı giriniz: "))
sayi1_karesi = sayi1*sayi1
sayi2_karesi = sayi2*sayi2
toplam = sayi1_karesi + sayi2_karesi

print("Sonuç :",toplam)
