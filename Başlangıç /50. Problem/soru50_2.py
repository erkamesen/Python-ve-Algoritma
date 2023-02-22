"""
'Kullanıcıdan alınan taban uzunluğu ve yükseklik ile üçgenin alanını bulan ardından kullanıcıdan
bir sayı alıp sayının karesini alanın değerinin üstüne ekleyen programı tasarlayın. alan=(taban uzunluğu*yükseklik)/2'
"""

taban_uzunlugu = float(input("Lütfen üçgenin taban uzunluğunu giriniz: ")) # 5
yukseklik = float(input("Lütfen üçgenin yüksekliğini giriniz: ")) # 10

alan = (taban_uzunlugu*yukseklik)/2 #25
alan_karesi = alan**2 # 625
toplam = alan + alan_karesi 
print(toplam) # 675
