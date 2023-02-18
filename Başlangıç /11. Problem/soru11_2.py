"""
'Kullanıcıdan 3 adet sayı alıp yüksek olan sayıyı kullanıcıya gösteren programı tasarlayın.(eğer sayılar eşitse "Sayılar Eşit!" yazsın.)'
"""

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
            
"Alternatif"
            
sayi1 = int(input("Lütfen birinci sayıyı giriniz: ")
sayi2 = int(input("Lütfen ikinci sayıyı giriniz: ")
sayi3 = int(input("Lütfen üçüncü sayıyı giriniz: ")
buyuk_sayi = max(sayi1, sayi2, sayi3)
print(f"en büyük sayi {buyuk_sayi}.")
