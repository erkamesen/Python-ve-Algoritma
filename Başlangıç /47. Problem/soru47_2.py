"""
'Kullanıcıdan 2 adet sayı alıp sayıların küplerinin toplamını kullanıcıya gösteren programı tasarlayın.'
"""


sayi1 = int(input("Lütfen ilk sayıyı giriniz: "))
sayi2 = int(input("Lütfen ikinci sayıyı giriniz: "))
sayi1_kupu = sayi1***3
sayi2_kupu = sayi2***3
toplam = sayi1_kupu + sayi2_kupu

print("Sonuç :",toplam)
