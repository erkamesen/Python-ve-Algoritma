"""
'Kullanıcıdan 2 adet sayı alıp yüksek olan sayıyı kullanıcıya gösteren programı tasarlayın.(eğer sayılar eşitse "Sayılar Eşit!" yazsın.)'
"""

sayi1 = int(input("Lütfen birinci sayıyı giriniz: ")
sayi2 = int(input("Lütfen ikinci sayıyı giriniz: ")
if sayi1>sayi2:
  print(f"{sayi1} daha büyük.")
elif sayi2>sayi1:
  print(f"{sayi1} daha büyük.")
else:
  print("Sayılar Eşit!)
        
 "Alternatif"
        
sayi1 = int(input("Lütfen birinci sayıyı giriniz: ")
sayi2 = int(input("Lütfen ikinci sayıyı giriniz: ")
buyuk_sayi = max(sayi1, sayi2)
print(f"{buyuk_sayi} daha büyük.")
