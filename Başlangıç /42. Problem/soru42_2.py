"""
'kullanıcıdan alınan 10 adet sayının sadece çif olanları ile aşağıdaki gibi bir tablo oluşturan programı tasarlayın.

Sayı  Karesi  Küpü  Karesi+Küpü
2     4       8       12
..    ..      ..      ..
..    ..      ..
..    ..
..

'
"""


print("Sayı\tKaresi\tKüpü\tKaresi+küpü")
for i in range(10):
  sayi = int(input("Lütfen işlem yapılacak sayıyı giriniz: "))
  if sayi%2==0:
    karesi = sayi**2
    kupu = sayi**3
    toplam = karesi + kupu
    print(f"{sayi}\t\t{karesi}\t\t{kupu}\t\t{toplam}")
  else:
    continue
  
"""
Sayı	  Karesi	  Küpü	  Karesi+küpü
Lütfen işlem yapılacak sayıyı giriniz: 1
Lütfen işlem yapılacak sayıyı giriniz: 2
2		4		8		12
Lütfen işlem yapılacak sayıyı giriniz: 3
Lütfen işlem yapılacak sayıyı giriniz: 4
4		16		64		80
Lütfen işlem yapılacak sayıyı giriniz: 5
Lütfen işlem yapılacak sayıyı giriniz: 6
6		36		216		252
Lütfen işlem yapılacak sayıyı giriniz: 7
Lütfen işlem yapılacak sayıyı giriniz: 8
8		64		512		576
Lütfen işlem yapılacak sayıyı giriniz: 9
Lütfen işlem yapılacak sayıyı giriniz: 10
10		100		1000		1100
"""
